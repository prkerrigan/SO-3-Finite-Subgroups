"""
Scratch script (not part of the paper): for each of the 60 elements of
A5 = <P, D, R5>, print BOTH the exact matrix (entries as (a + b*phi)/2)
AND the induced permutation of the 5 tetrahedra, ready to paste into LaTeX.
"""
from sympy import symbols, Matrix, expand, Rational
from fractions import Fraction

phi = symbols('phi')


def reduce_phi(expr):
    e = expand(expr)
    while True:
        e2 = expand(e.replace(phi**2, phi + 1))
        if e2 == e:
            return e
        e = e2


def mat_reduce(M):
    return M.applyfunc(reduce_phi)


def mat_mul(A, B):
    return mat_reduce(A * B)


def entry_key(e):
    e = reduce_phi(e)
    a = e.coeff(phi, 1)
    b = e.coeff(phi, 0)
    return (Fraction(str(a)), Fraction(str(b)))


def mat_key(M):
    return tuple(entry_key(M[i, j]) for i in range(3) for j in range(3))


def vec_key(v):
    return tuple(entry_key(x) for x in v)


def term(n, sym):
    if n == 0:
        return None
    if sym and abs(n) == 1:
        s = sym
    elif sym:
        s = f"{abs(n)}{sym}"
    else:
        s = f"{abs(n)}"
    return ("-" if n < 0 else "+", s)


def body_str(an, bn):
    """an: integer coeff of phi, bn: integer constant term -> signed LaTeX string."""
    parts = []
    t = term(an, r"\phi")
    if t:
        parts.append(t)
    t = term(bn, "")
    if t:
        parts.append(t)
    if not parts:
        return "0"
    sign0, s0 = parts[0]
    body = (("-" if sign0 == "-" else "") + s0)
    for sign, s in parts[1:]:
        body += f"{sign}{s}"
    return body


def latex_matrix(M):
    """Render a 3x3 matrix, factoring a common 1/2 (or other common
    denominator) out in front whenever every entry shares one."""
    from math import gcd
    coeffs = []  # (a, b) Fractions per entry, row-major
    den = 1
    for i in range(3):
        for j in range(3):
            e = reduce_phi(M[i, j])
            a = Fraction(str(e.coeff(phi, 1)))
            b = Fraction(str(e.coeff(phi, 0)))
            coeffs.append((a, b))
            for d in (a.denominator, b.denominator):
                den = den * d // gcd(den, d)

    bodies = []
    for a, b in coeffs:
        an = a * den
        bn = b * den
        bodies.append(body_str(int(an), int(bn)))

    rows = [" & ".join(bodies[3 * i:3 * i + 3]) for i in range(3)]
    matrix_tex = r"\begin{bmatrix}" + r"\\[4pt] ".join(rows) + r"\end{bmatrix}"
    if den == 1:
        return matrix_tex
    return r"\dfrac{1}{" + str(den) + "}" + matrix_tex


# generators
P = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
D = Matrix([[1, 0, 0], [0, -1, 0], [0, 0, -1]])

vhat = Matrix([[0, -phi, 1], [phi, 0, 0], [-1, 0, 0]])
vhat2 = mat_reduce(vhat * vhat)
R5 = mat_reduce(Matrix.eye(3) + Rational(1, 2) * vhat + Rational(1, 2) * (2 - phi) * vhat2)

gens = {"P": P, "D": D, "R5": R5}

I3 = Matrix.eye(3)
elems = {mat_key(I3): I3}
words = {mat_key(I3): ""}
frontier = [I3]
while frontier:
    new_frontier = []
    for M in frontier:
        for name, g in gens.items():
            cand = mat_mul(M, g)
            k = mat_key(cand)
            if k not in elems:
                elems[k] = cand
                words[k] = words[mat_key(M)] + name
                new_frontier.append(cand)
    frontier = new_frontier

print("group order:", len(elems))

T1 = [Matrix([1, 1, 1]), Matrix([1, -1, -1]), Matrix([-1, 1, -1]), Matrix([-1, -1, 1])]


def apply_mat(M, T):
    return [mat_reduce(M * v) for v in T]


def tet_key(T):
    return frozenset(vec_key(v) for v in T)


tetrahedra = [T1]
tet_keys = [tet_key(T1)]
for M in elems.values():
    Tg = apply_mat(M, T1)
    k = tet_key(Tg)
    if k not in tet_keys:
        tetrahedra.append(Tg)
        tet_keys.append(k)

print("number of tetrahedra in orbit:", len(tetrahedra))


def perm_of(M):
    perm = []
    for T in tetrahedra:
        Tg = apply_mat(M, T)
        k = tet_key(Tg)
        idx = tet_keys.index(k)
        perm.append(idx + 1)
    return tuple(perm)


def cycle_notation(perm):
    n = len(perm)
    seen = [False] * n
    cycles = []
    for i in range(n):
        if seen[i]:
            continue
        cyc = [i + 1]
        seen[i] = True
        j = perm[i] - 1
        while j != i:
            seen[j] = True
            cyc.append(j + 1)
            j = perm[j] - 1
        if len(cyc) > 1:
            cycles.append(tuple(cyc))
    if not cycles:
        return "()"
    return "".join(str(c).replace(",)", ")").replace(" ", "") for c in cycles)


def order_of(M):
    cur = Matrix.eye(3)
    for n in range(1, 61):
        cur = mat_mul(cur, M)
        if cur == Matrix.eye(3):
            return n
    return None


results = []
for k, M in elems.items():
    perm = perm_of(M)
    cyc = cycle_notation(perm)
    ordv = order_of(M)
    if ordv == 5:
        tr = reduce_phi(M.trace())
        group = "5a" if tr == phi else "5b"
    else:
        group = ordv
    results.append((ordv, group, cyc, M, words[k]))

results.sort(key=lambda r: (r[0], str(r[1]), r[2]))

group_labels = {
    1: "identity (1 element)",
    2: "order 2, cycle type $(2,2)$ -- 15 elements",
    3: "order 3, cycle type $(3)$ -- 20 elements",
}

with open("a5_full_table.tex", "w", encoding="utf-8") as f:
    f.write(r"\begin{longtable}{c @{\hspace{3em}} c}" + "\n")
    f.write(r"\caption{All 60 elements of $A_5=\langle P,D,R_5\rangle$: the permutation $\rho(g)\in S_5$ of $\{T_1,\dots,T_5\}$ and the matrix $g$ itself, grouped by conjugacy class.}\label{tab:a5-elements}\\" + "\n")
    cur_group = None
    for ordv, group, cyc, M, w in results:
        if group != cur_group:
            if group == 1:
                label = group_labels[1]
            elif group == 2:
                label = group_labels[2]
            elif group == 3:
                label = group_labels[3]
            elif group == "5a":
                label = r"order 5, $k=1$, radius $2\pi/5$ -- 12 elements"
            else:
                label = r"order 5, $k=2$, radius $4\pi/5$ -- 12 elements"
            f.write(r"\hline" + "\n")
            f.write(r"\multicolumn{2}{c}{\textit{" + label + r"}} \\" + "\n")
            f.write(r"\hline" + "\n")
            cur_group = group
        f.write(f"${cyc}$ & ${latex_matrix(M)}$ \\\\[10pt]\n")
    f.write(r"\hline" + "\n")
    f.write(r"\end{longtable}" + "\n")
