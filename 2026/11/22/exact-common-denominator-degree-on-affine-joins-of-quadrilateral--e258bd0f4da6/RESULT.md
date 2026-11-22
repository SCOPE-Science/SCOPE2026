# Exact common-denominator degree on affine joins of quadrilaterals

## Finding
For every integer \(k\ge 2\) and every family of nondegenerate convex quadrilaterals \(Q_1,\ldots,Q_k\), embed the factors in affinely independent layers and let \(J=Q_1*\cdots*Q_k\) be their affine join. Among all nonnegative rational generalized barycentric-coordinate systems on \(J\), the least possible total degree of a common polynomial denominator is **exactly \(k\)**:
\[
\deg_{\mathrm{GBC}}(J)=k.
\]
This is independent of quadrilateral shapes and remains true when all factors are parallelograms. In the latter case, the Cartesian product of the same \(k\) factors has polynomial barycentric coordinates (denominator degree zero), while their join requires degree \(k\): the join-versus-product gap is unbounded.

## Assumptions and scope
All polytopes are real, full dimensional in their affine hulls and convex; the quadrilaterals have four distinct extreme vertices. An affine join means the convex hull of \(Q_i\) in pairwise disjoint affine layers with affinely independent layer labels. In block coordinates it is
\[
J=\{(z_1,\ldots,z_k,t_1,\ldots,t_k):t_i\ge0,\ \sum_i t_i=1,\ z_i\in t_iQ_i\},
\]
where only \(k-1\) layer coordinates are independent; hence \(\dim J=3k-1\). The expression \(t_iQ_i\) uses a fixed affine-coordinate origin for each polygon block and at \(t_i=0\) means \(z_i=0\).

A nonnegative rational generalized barycentric system is a family \(\alpha_v=p_v/q\), indexed by vertices \(v\) of \(J\), with real polynomials \(p_v,q\), a nonzero common \(q\), nonnegative \(\alpha_v\) in the relative interior, normalization \(\sum_v\alpha_v=1\), and affine precision \(\sum_v\alpha_v v=x\). Boundary values are taken by continuous extension. The denominator degree is the total polynomial degree on \(\operatorname{aff}J\), after any common factors have been canceled. Multiplication of all numerator and denominator polynomials by a common polynomial cannot decrease the optimum.

## Proof
**Step 1 (facet incidence and excess).** A facet of an affine join is the join of one factor facet with all remaining full factors. Each quadrilateral has four edges, so \(J\) has \(4k\) facets. At a vertex \(v\) belonging to factor \(Q_i\), precisely two facets from \(Q_i\) contain \(v\), while all four facets arising from any other factor contain \(v\). Thus \(v\) belongs to \(4k-2\) facets. Since \(\dim J=3k-1\), its vertex excess is
\[
\operatorname{ex}(v)=(4k-2)-(3k-1)=k-1.
\]
The vertex set of \(J\) affinely spans its ambient affine space.

**Step 2 (spanning-excess obstruction).** The vanishing-order theorem for rational generalized barycentric denominators, Baumbach--Winter [1, Lemma 2.8], states that at any face \(f\) a common denominator \(q\) vanishes to order at least its facet excess. In particular, for every vertex of \(J\),
\[
\operatorname{ord}_v(q)\ge k-1.
\]
Here order is the minimum total degree of a nonzero term in the Taylor expansion around \(v\). If \(\deg q<k-1\), this forces \(q=0\), impossible. Suppose \(\deg q=k-1=r\ge1\). Let \(H\) be the top homogeneous component of \(q\). All lower Taylor terms at every vertex vanish, so \(q(v+u)=H(u)\) for every vertex \(v\) and every vector \(u\). For two vertices \(v,w\), therefore, \(H(u)=H(u+v-w)\) for all \(u\). A polynomial invariant under translation by a nonzero vector is invariant under every real multiple of that vector. Since the vertex differences span the ambient translation space, \(H\) is translation-invariant in all directions, hence constant. But \(H\) is a nonzero homogeneous polynomial of positive degree \(r\), a contradiction. Consequently \(\deg q\ge k\). This yields the more general *spanning-excess principle*: if an affinely spanning set of vertices of a full-dimensional polytope all have excess at least an integer \(r\ge1\), every rational GBC denominator has degree at least \(r+1\).

**Step 3 (sharp construction).** Each convex quadrilateral has nonnegative rational Wachspress coordinates \(\beta_{i,a}=p_{i,a}/q_i\) with quadratic-or-lower numerators and affine-or-constant common denominator [1, Sections 2.3--2.4]. Choose these representations with \(q_i>0\) in the interior. Homogenize to degree two and one, respectively:
\[
P_{i,a}(z_i,t_i)=t_i^2 p_{i,a}(z_i/t_i),\qquad
H_i(z_i,t_i)=t_iq_i(z_i/t_i).
\]
Both are polynomials, including when \(q_i\) is constant (in which case \(H_i\) is proportional to \(t_i\)). Define the common denominator and numerators
\[
Q=\prod_{i=1}^k H_i,\qquad
N_{i,a}=P_{i,a}\prod_{j\ne i}H_j.
\]
Their total degrees are at most \(k\) and \(k+1\). Wherever all \(t_i>0\), the resulting coordinates satisfy
\[
\frac{N_{i,a}}Q=t_i\,\beta_{i,a}(z_i/t_i).
\]
They are nonnegative, sum to \(\sum_i t_i=1\), and reproduce each block \(z_i\) and the layer labels. On a boundary layer \(t_i=0\), the bound \(0\le t_i\beta_{i,a}\le t_i\) gives a continuous extension, so the construction is valid on all of \(J\). Thus \(\deg_{\mathrm{GBC}}(J)\le k\), matching Step 2.

**Step 4 (unbounded join-product separation).** For parallelograms, each factor admits polynomial bilinear coordinates via affine transport of the unit square. Tensor products produce polynomial generalized barycentric coordinates for the Cartesian product, hence degree zero. Step 2 forces degree \(k\) for the join, for every \(k\ge2\). This contrast uses only the same factor polygons with different natural polytope operations.

## Verification
The universal inequalities are proved in Steps 1--3, not inferred from finite testing. For the unit square the homogenized four numerators are \((t-z_x)(t-z_y)\), \(z_x(t-z_y)\), \(z_xz_y\), \((t-z_x)z_y\) and the homogenized denominator is \(t\). For the trapezoid with vertices \((0,0),(2,0),(1,1),(0,1)\), they are \((2t-z_x-z_y)(t-z_y)\), \(z_x(t-z_y)\), \(z_xz_y\), \(z_y(2t-z_x-z_y)\), with homogenized denominator \(2t-z_y\). In both cases direct expansion verifies
\[
\sum_a P_{i,a}=t_iH_i,\qquad
\sum_a v_{i,a}P_{i,a}=z_iH_i.
\]
The standalone `VERIFY_JOIN_QUADRILATERALS.py` uses exact rational arithmetic to verify normalization, affine precision, positivity and the incidence count in 336 model cases for \(2\le k\le8\), including mixed square/trapezoid factors. This finite check supplements the all-dimensional proof.

## Relationship to prior work
Baumbach--Winter [1] establishes the local vertex-excess vanishing-order theorem and a general Wachspress upper bound, but these give only \(k-1\le\deg_{\mathrm{GBC}}(J)\le k\) for the present joins. The present spanning-vertex argument closes this gap for arbitrary rational GBC denominators, not just Wachspress adjoints. Baumbach--Freyer--Weigert--Winter [2] studies adjoint degree and degree drop, including products and pyramids; the adjoint degree is not in general the minimum possible denominator degree, so an adjoint computation alone does not establish the lower bound here. Kohn--Ranestad [3] develops projective adjoints and Wachspress maps, but does not establish the present minimum-denominator join classification. The published planar denominator theorem [4] concerns individual polygons, not joins; the Cartesian-product degree comparison differs both combinatorially and dimensionally from affine joins.

## Limitations
No claim is made for joins containing polygons with five or more sides, for sign-indefinite affine barycentric coordinates, or for arbitrary rational representations lacking a common polynomial denominator. The proof uses the precise published vertex-excess theorem [1]; verification of that external lemma is through inspection of its stated hypotheses and proof. The exact classifications are not a claim of independence or a substitute for external priority review.

## References
[1] T. Baumbach and M. Winter, *Rational barycentric coordinates and low degree adjoints*, arXiv:2611.02110v1, first posted 2026-11-01. https://arxiv.org/html/2611.02110v1 (Sections 2.3--2.5, especially Lemma 2.8).

[2] T. Baumbach, A. Freyer, J. Weigert and M. Winter, *The canonical form, scissors congruence and adjoint degrees of polytopes*, arXiv:2508.04275v1, 2025-08-06. https://arxiv.org/html/2508.04275v1 (Section 3 and Appendix C).

[3] K. Kohn and K. Ranestad, *Projective Geometry of Wachspress Coordinates*, Foundations of Computational Mathematics 20 (2020), 1135--1173; first preprint arXiv:1904.02123, 2019-04-03. https://link.springer.com/article/10.1007/s10208-019-09441-z (Introduction and Section 2).

[4] *Wachspress denominators have minimum degree on every convex polygon*, published published-finding corpus research record dated 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-wachspress-denominators-have-minimum-degree-on-every-convex-poly--7b4aad67706d (published abstract used for statement comparison).
