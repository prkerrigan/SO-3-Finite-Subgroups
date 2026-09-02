# Visualizing Rotations of Space and its Finite Subgroups

This repository contains the LaTeX source (and a Vietnamese translation) of a paper
about the finite subgroups of $SO(3)$ — the cyclic groups $C_k$, dihedral groups
$D_k$, and the three exceptional groups $A_4$, $S_4$, $A_5$ — and how each one is
naturally visualized as the symmetry group of a family of "derived polyhedra" sitting
inside a single picture of rotation space, with conjugacy classes corresponding to
distinct copies of these polyhedra.

Comments, corrections, and suggestions are very welcome — please open an issue on
this repository, or email vice-president@pkeng.net directly. If you spot a
mathematical error, a citation that should be added, or a passage that's unclear,
that kind of feedback is exactly what this repo is for.

## AI assistance

Portions of this paper's exposition and editing, and the computer-algebra
verification underlying the explicit matrices in the appendix, were produced with
the assistance of large language models: Claude Sonnet 4.6, for translation-focused
editing of the Vietnamese version, and Claude Sonnet 5 (via GitHub Copilot), for
drafting and editing assistance and for exact symbolic computation and verification
of the group-theoretic and matrix claims throughout. All mathematical content was
reviewed and verified by the author.

## Contents

- [main.tex](main.tex) — the paper (English).
- [main_vi.tex](main_vi.tex) — a Vietnamese translation (paraphrased, not a literal
  translation; may lag behind the newest content in `main.tex`).
- [references.bib](references.bib) — bibliography.
- [patrick_custom.sty](patrick_custom.sty) — personal macro package (set notation,
  number systems, `\coloneqq`, etc.) used throughout the paper.
- [maa-monthly.sty](maa-monthly.sty) — house style for the *American Mathematical
  Monthly*, kept here in case the paper is ever submitted there. The public
  build (`main.tex`) currently uses the generic `amsart` class instead; swap the
  `\documentclass` line and re-add `\usepackage{maa-monthly}` to reproduce the
  Monthly-formatted version.
- `figures/` — TikZ/image assets included by the paper.
- [scratch_a5.py](scratch_a5.py) and [scratch_a5_matrices.py](scratch_a5_matrices.py)
  — reproducibility scripts, described in detail below. These are **not** part of
  the paper; they are the computer-algebra scratch work used to derive and verify
  the explicit $A_5$ results quoted in the appendix.

## Building the paper

Requires a standard TeX Live / MiKTeX installation with `latexmk`:

```
latexmk -pdf main.tex
```

## The `A_5` reproducibility scripts

The appendix of the paper realizes $A_5$ (order 60) as $\langle P, D, R_5\rangle$,
three explicit $3\times 3$ rotation matrices, and separately as permutations of five
tetrahedra inscribed in the dodecahedron. Every matrix entry lives in the ring
$\mathbb{Z}[\varphi]/(\varphi^2-\varphi-1)$, i.e. every entry has the form
$\tfrac{a+b\varphi}{2}$ for integers $a,b$, where $\varphi=\tfrac{1+\sqrt5}{2}$ is the
golden ratio. Both scripts use [SymPy](https://www.sympy.org/) to do this arithmetic
*exactly* (no floating point), which is what makes it possible to assert group
membership, matrix equality, and element order by direct symbolic comparison instead
of by numerical tolerance.

Both scripts require Python 3 with `sympy` installed (`pip install sympy`).

### `scratch_a5.py`

The original, minimal reproducibility script. It:

1. Defines the golden-ratio ring arithmetic:
   - `phi = symbols('phi')` — a SymPy symbol standing for $\varphi$.
   - `reduce_phi(expr)` — repeatedly rewrites $\varphi^2\to\varphi+1$ until the
     expression stabilizes, putting every element of the ring into the canonical
     form $a+b\varphi$. This is the workhorse function everything else relies on.
   - `mat_reduce` / `mat_mul` — apply `reduce_phi` entrywise, and multiply two
     matrices then reduce the result, respectively.
   - `entry_key` — turns a ring element into a hashable `(Fraction, Fraction)` pair
     (coefficient of $\varphi$, constant term) so matrices can be used as dictionary
     keys despite SymPy expressions not hashing the way you'd want for this purpose.
   - `mat_key` / `vec_key` — the same, for a whole $3\times3$ matrix or a vector.
2. Defines the three generators exactly as in the paper's appendix:
   - `P` — the order-3 cyclic coordinate permutation matrix.
   - `D = diag(1,-1,-1)` — the order-2 generator.
   - `R5` — built from Rodrigues' rotation formula applied to the hat-map matrix
     `vhat` of the icosahedron vertex axis $(0,1,\varphi)$, exactly reproducing the
     closed form derived by hand in the appendix.
3. **Closes the group**: starting from the identity, repeatedly right-multiplies
   every element found so far by each of `P`, `D`, `R5`, adding any new matrix to a
   dictionary keyed by `mat_key`, until no new elements appear (a breadth-first
   search over the Cayley graph). This terminates with all 60 elements of $A_5$ and
   confirms the group order directly (`print("order distribution", ...)`) — this is
   the computational proof that $\langle P,D,R_5\rangle$ has order exactly 60.
4. **Computes the tetrahedron orbit**: starting from the tetrahedron
   $T_1=\{(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\}$, applies every group element to
   it and collects the distinct images (via `tet_key`, a `frozenset` of vector
   keys), producing the five tetrahedra $T_1,\dots,T_5$ used in the paper.
5. **Computes the induced permutation** `perm_of(M)` of each group element on
   $\{T_1,\dots,T_5\}$, converts it to cycle notation with `cycle_notation`, computes
   each element's order with `order_of` (by repeated multiplication until the
   identity reappears, since the group is finite), and finally prints every element
   sorted by `(order, cycle notation)` alongside its trace — the raw data behind the
   paper's classification of the 60 elements into 1 identity + 15 order-2 + 20
   order-3 + 24 order-5 (split 12/12 by trace $\varphi$ vs.\ $1-\varphi$).

Run it directly to see the classification:

```
python scratch_a5.py
```

### `scratch_a5_matrices.py`

An extension of the same computation that additionally emits ready-to-paste LaTeX
for the paper's 60-element table (Table for `tab:a5-elements`). It reuses the same
ring arithmetic, generators, group-closure, and tetrahedron-orbit logic as
`scratch_a5.py`, and adds:

- `body_str(an, bn)` / `latex_matrix(M)` — render a $3\times3$ matrix as LaTeX,
  **factoring out the common denominator** (here always 1 or 2) as a leading
  `\dfrac{1}{2}` in front of a `bmatrix` of small integer-coefficient entries,
  rather than writing a separate fraction in every cell. This is what keeps the
  appendix table readable instead of a wall of individual `\dfrac{...}{2}`s.
- A `words` dictionary tracking, for each element, the generator word (e.g.
  `"R5D"`) that produced it during the BFS closure — used to sanity-check specific
  entries (for instance, confirming that the matrix listed under the permutation
  $(1,2)(3,4)$ is $R_5D$, not $R_5$, despite superficially resembling it).
- Conjugacy-class labeling: every order-5 element is tagged `5a` or `5b` depending
  on whether its trace is $\varphi$ (rotation angle $2\pi/5$) or $1-\varphi$
  (rotation angle $4\pi/5$), matching the paper's two order-5 conjugacy classes.
- A final loop that writes `a5_full_table.tex`, a complete
  `longtable` environment with one row per group element, grouped and separated by
  `\hline`/`\multicolumn` headers exactly matching the structure pasted into the
  paper's appendix.

Run it to regenerate the table from scratch:

```
python scratch_a5_matrices.py
```

This writes `a5_full_table.tex` in the working directory (not tracked in the repo —
its contents are copied by hand into `main.tex`'s appendix after generation, so that
the paper doesn't depend on running Python to build).

### Why exact arithmetic matters here

Every check in this repository — group closure, element order, conjugacy class
membership, matrix (in)equality — is done by exact symbolic comparison in
$\mathbb{Z}[\varphi]/(\varphi^2-\varphi-1)$, never by floating-point approximation.
That is what makes statements like "this element has order 5" or "these two matrices
are different" fully rigorous rather than merely numerically suggestive.
