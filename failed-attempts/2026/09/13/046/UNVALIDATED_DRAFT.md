# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Arithmeticity decision for the first compact hyperbolic Coxeter 4-cube

## The polytope
Let **C0** be the first compact hyperbolic Coxeter 4-cube in the Jacquemet–Tschantz
classification ("All hyperbolic Coxeter n-cubes", JCTA 158 (2018), Fig. 1), i.e. the graph
**Σ₁^{2,2,3}** (solid labels k=l=2, m=3), identically the Ma–Zheng polytope **P_{34,1}**
("Compact hyperbolic Coxeter four-dimensional polytopes with eight facets", J. Algebraic
Combin. 59 (2024), Fig. 34, Table 17). It is combinatorially a 4-cube (8 facets; the four
disjoint facet pairs form a perfect matching, so the adjacency graph is the complete
4-partite graph K_{2,2,2,2}). Every intersecting dihedral angle is π/2 or π/3, so all
dihedral angles are of the form π/m.

## Exact Gram matrix
Order the facets (T,U,LM,CM,RM,LB,CB,RB). With a=(1+√13)/4 and c=√((5+√13)/6):

- G_ii = 1;
- G_ij = −1/2 on the six pairs (T,LM),(LM,CM),(CM,RM),(CM,CB),(LB,CB),(RM,RB);
- G_ij = −a on the three pairs (T,RM),(LM,LB),(CB,RB);
- G_ij = −c on the pair (U,CM);
- G_ij = 0 on the remaining 18 (orthogonal, m=2) pairs.

The dotted lengths are exactly those of JT Table 4, entry ((k,l),m)=((2,2),3)
(cosh e=(1+√13)/4, cosh d=√((5+√13)/6)) and MZ Table 17, row P_{34,1}.
Exact characteristic polynomial (sympy):
  char(G0) = λ³(λ−2)³(24λ²−48λ−23−13√13)/24,
so rank(G0)=5 with exactly one negative eigenvalue: signature (4,1) — a genuine
compact-hyperbolic Gram matrix (Vinberg, Thm 2.1). All 16 vertex 4×4 principal minors
(the 4-sets of facets avoiding the four disjoint pairs) are positive definite
(Sylvester, checked exactly), confirming compactness (Vinberg, Thm 3.1–3.2).

## Vinberg field
Facet U is pendant (its only non-orthogonal neighbour is CM), hence every closed walk
in the diagram traverses the edge (U,CM) an even number of times. Every cyclic product
of 2G0 is therefore a monomial in a and c²=(5+√13)/6 with rational coefficients, i.e.
lies in Q(√13). Since 4a²=(7+√13)/2 ∉ Q, the field is exactly
  k0 = Q(√13), [k0:Q] = 2 (totally real).

## Decision: NOT arithmetic
The 2-cycle of 2G0 on the dotted pair (U,CM) is 4c²=(10+2√13)/3. Its monic minimal
polynomial over Q is t²−(20/3)t+16/3 (i.e. 3t²−20t+16), and its field norm is
N(4c²)=(100−52)/9=16/3 ∉ ℤ. An algebraic integer has integral minimal polynomial and
integral norm; hence 4c² is **not** an algebraic integer. Vinberg's arithmeticity
criterion requires every cyclic product of 2G0 to be an algebraic integer. This
condition is violated, so the reflection group of C0 is **not arithmetic** over k0.
For contrast, the other dotted pairs are unobstructed: 4a²=(7+√13)/2 has monic
minpoly t²−7t+9 (integral), and 2a=(1+√13)/2 has monic minpoly t²−t−3 (integral).

## Quasi-arithmetic status
The unique nontrivial embedding σ:√13↦−√13 sends the Gram matrix to Gs, with exact
  char(Gs) = λ³(λ−2)³(24λ²−48λ−23+13√13)/24.
The quadratic factor has discriminant (4512²−1248²·13)=110592>0 (hence real, via
integers only), root-product (13√13−23)/24>0 (since 13²·13−23²=1668>0) and root-sum 2>0:
two distinct strictly positive roots. Thus Gs is positive semi-definite (rank 5, no
negative eigenvalue); the same holds with c↦−c since det(Gs−λI) depends only on c²
(row U has a single off-diagonal entry). A Schur-complement (pivot at the pendant
vertex) transfers this to the K-rational Vinberg form. Hence the nontrivial Galois
conjugate is admissible: the group is **properly quasi-arithmetic** in the standard
Gromov–Piatetski-Shapiro / Belolipetsky–Thomson sense (field totally real, all
nontrivial conjugates compact, but traces non-integral).
Caveat: JT Remark 9 labels Σ₁^{2,2,3} "non-arithmetic and not quasi-arithmetic",
apparently using a finer invariant or stricter terminology; that remark gives no
computation. It does not affect the certified non-arithmeticity proved here (which
needs only the single non-integral cyclic product above).

## Reproducibility
`output/verify_c0_vinberg.py` re-derives (A)–(D) exactly with sympy (rank, charpolys,
vertex ellipticity, minpolys, norm, PSD certificate). No floating point enters any
certificate. PARI/GP was unavailable on this host; sympy exact arithmetic is the
substitute (see Limitations in research_report.json).
