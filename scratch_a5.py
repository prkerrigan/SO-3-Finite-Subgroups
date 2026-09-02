"""
Scratch script (not part of the paper): computes all 60 elements of A5
using the generators P, D, R5 from the appendix, and the induced
permutation of the 5 inscribed tetrahedra, in exact arithmetic over
Z[phi]/(phi^2-phi-1).
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


# generators
P = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
D = Matrix([[1, 0, 0], [0, -1, 0], [0, 0, -1]])

vhat = Matrix([[0, -phi, 1], [phi, 0, 0], [-1, 0, 0]])
vhat2 = mat_reduce(vhat * vhat)
R5 = mat_reduce(Matrix.eye(3) + Rational(1, 2) * vhat + Rational(1, 2) * (2 - phi) * vhat2)

gens = {"P": P, "D": D, "R5": R5}

# --- generate the group by BFS closure ---
I3 = Matrix.eye(3)
elems = {mat_key(I3): I3}
frontier = [I3]
while frontier:
    new_frontier = []
    for M in frontier:
        for name, g in gens.items():
            cand = mat_mul(M, g)
            k = mat_key(cand)
            if k not in elems:
                elems[k] = cand
                new_frontier.append(cand)
    frontier = new_frontier

print("group order:", len(elems))

# --- orbit of the tetrahedron T1 under the group ---
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
for i, T in enumerate(tetrahedra, start=1):
    print(f"T{i} =", [tuple(v) for v in T])

# --- for each group element, compute induced permutation of {1..5} ---


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
    tr = reduce_phi(M.trace())
    results.append((ordv, cyc, tr, M))

results.sort(key=lambda r: (r[0], r[1]))

from collections import Counter
order_counts = Counter(r[0] for r in results)
print("order distribution:", dict(order_counts))

print()
for ordv, cyc, tr, M in results:
    print(f"order {ordv:2d}  perm {cyc:12s} trace {tr}")
