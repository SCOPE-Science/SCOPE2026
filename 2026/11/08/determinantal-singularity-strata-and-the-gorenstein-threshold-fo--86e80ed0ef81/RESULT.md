# Determinantal singularity strata and the Gorenstein threshold for corank-one toric positroids

## Finding

For every integer \(r\ge3\) and every \((r+1)\)-tuple of positive integers \((a_0,\ldots,a_r)\), consider the rank-\(r\) matroid with consecutive parallel blocks \(A_i\) of cardinalities \(a_i\), whose bases select one label in each of precisely \(r\) blocks. Its complex positroid variety \(X\) is toric, and has dimension \(N-1\), where \(N=\sum_i a_i\).

For each index \(i\), define the closed reduced coordinate-support locus \(S_i\) by retaining only the Pluecker coordinates whose bases omit block \(i\). The loci are pairwise disjoint and satisfy
\[
S_i\cong\prod_{j\ne i}\mathbb P^{a_j-1},\qquad
\operatorname{Sing}(X)_{\mathrm{red}}=\bigsqcup_{i:a_i\ge2} S_i.
\]
At every point of \(S_i\), an affine neighborhood is a smooth \(N-a_i-r\)-dimensional factor times the affine rank-at-most-one determinantal variety of \(a_i\times r\) matrices. More precisely, the isomorphism holds at the level of affine Pluecker coordinate charts, hence for completed local rings. If \(a_i\ge2\), the codimension of \(S_i\) in \(X\) is \(a_i+r-1\), its Hilbert--Samuel multiplicity is
\[
e_i=\binom{a_i+r-2}{a_i-1},
\]
and its local Weil divisor class group is infinite cyclic. Finally,
\[
X\text{ is }\mathbb Q\text{-Gorenstein}
\quad\Longleftrightarrow\quad
X\text{ is Gorenstein}
\quad\Longleftrightarrow\quad
a_i\in\{1,r\}\text{ for all }i.
\]

## Assumptions and scope

Work over \(\mathbb C\). The blocks \(A_0,\ldots,A_r\) are all nonempty and occur in the indicated cyclic order, with no interleaving. Let \(M\) be the parallel extension of the uniform matroid \(U_{r,r+1}\) along these blocks. This matroid is regular: it is obtained by duplicating columns of a totally unimodular representation of \(U_{r,r+1}\). It is a positroid because columns of each block may be duplicated consecutively in a totally nonnegative maximal-minor representation. McNeill's toricity theorem then identifies the positroid variety with the projective closure of its dense diagonal-torus orbit. The subvariety \(X\) has the reduced scheme structure of the positroid variety. For a block index \(i\), \(S_i\) is defined inside \(X\) as the reduced intersection with the coordinate projective subspace spanned by Pluecker coordinates of bases omitting \(A_i\).

## Proof

**1. Monomial parameterization and dimension.** Choose a rank-\(r\) representation of \(U_{r,r+1}\) with all its nonzero ordered maximal minors equal to one; duplicate column \(i\) across \(A_i\). Multiplication of each column labeled \((i,s)\) by an independent parameter \(t_{i,s}\) produces Pluecker coordinates
\[
p_{\widehat i;(s_j)_{j\ne i}}=\prod_{j\ne i}t_{j,s_j},
\]
with coordinates of all nonbases equal to zero. Here the hat means that block \(i\) is omitted. By the cited regular-positroid toricity theorem, the closure of this monomial diagonal orbit is all of \(X\), not merely a proper toric subvariety. All \(N\) diagonal parameters vary effectively modulo their common scalar because the matroid is connected, so \(\dim X=N-1\).

**2. Exact affine charts.** Fix an omitted block \(k\) and choose one baseline label \((j,0)\in A_j\) for every \(j\ne k\). On the Pluecker chart \(p_{\widehat k;(0)_{j\ne k}}\ne0\), every homogeneous coordinate ratio is a monomial in the following functions:
\[
u_{j,s}=\frac{t_{j,s}}{t_{j,0}}\quad(j\ne k,\ 1\le s<a_j),
\qquad
z_{s,i}=\frac{t_{k,s}}{t_{i,0}}\quad(0\le s<a_k,\ i\ne k).
\]
A ratio from a basis omitting \(k\) is a product of the \(u\)-variables. A ratio from a basis omitting \(i\ne k\) is \(z_{s,i}\) times a product of \(u\)-variables, so these functions generate the entire affine chart algebra. The \(u\)-variables are algebraically independent from the \(z\)-subalgebra. The \(z\)-variables are the entries of an outer-product matrix, and the full kernel of their monomial parametrization is the prime ideal of its \(2\times2\) minors. Consequently there is a **scheme-theoretic isomorphism**
\[
\mathcal O_X\bigl(p_{\widehat k;(0)}\ne0\bigr)
\cong
\mathbb C[u_{j,s}:j\ne k,\ s>0]\otimes_{\mathbb C}
\frac{\mathbb C[z_{s,i}:0\le s<a_k,\ i\ne k]}{I_2(Z)}.
\]
There are exactly \(\sum_{j\ne k}(a_j-1)=N-a_k-r\) independent \(u\)-variables. The determinantal factor has dimension \(a_k+r-1\), matching the global dimension. This algebraic description works for every choice of omitted block and baseline labels and these Pluecker charts cover \(X\).

**3. Singular strata and multiplicities.** The rank-at-most-one \(a_k\times r\) determinantal variety is smooth off its zero matrix. If \(a_k=1\), it is affine \(r\)-space everywhere. If \(a_k\ge2\), its singular locus is the origin: all defining minors have vanishing linear parts at the origin, while its positive-rank points have standard smooth affine charts. In the above Pluecker chart, the zero matrix is exactly the locus with support only in bases omitting \(k\), and the remaining coordinates \(u\) parameterize a piece of the Segre product \(\prod_{j\ne k}\mathbb P^{a_j-1}\). The coordinate supports for distinct omitted blocks are disjoint, so these chartwise loci glue to the asserted disjoint union. The origin of the cone over \(\mathbb P^{a_k-1}\times\mathbb P^{r-1}\) has Hilbert--Samuel multiplicity equal to the Segre degree \(\binom{a_k+r-2}{a_k-1}\); adjoining smooth variables preserves multiplicity. The codimension equals the transverse dimension \(a_k+r-1\).

**4. Gorenstein frontier.** For \(a_k\ge2\), the rank-one matrix cone is the normal affine cone over \(\mathbb P^{a_k-1}\times\mathbb P^{r-1}\) in its \(\mathcal O(1,1)\) embedding. Its local divisor class group at the vertex is
\[
\operatorname{Pic}(\mathbb P^{a_k-1}\times\mathbb P^{r-1})/\mathbb Z[\mathcal O(1,1)]
\cong\mathbb Z.
\]
The canonical bundle of the Segre product is \(\mathcal O(-a_k,-r)\), hence its image in this quotient is \(a_k-r\) times a primitive generator, up to sign. Because this class group has no torsion, the canonical class is \(\mathbb Q\)-Cartier if and only if \(a_k=r\); in that case the Cohen--Macaulay determinantal cone is Gorenstein. When \(a_k=1\), the cone is smooth and also Gorenstein. Every local chart is of one of these types, proving the global if-and-only-if criterion.

## Verification

The included `CHECK.py` performs exact integral exponent-vector checks of the chart generators and all rank-one minor identities for sample rank and block-size combinations, plus finite-difference computations of the Segre multiplicity formula. Its successful output ends `ALL_EXACT_CHART_CHECKS_OK`. The checker does not establish generation of the full determinantal kernel in all dimensions, the all-rank local-ring isomorphism, or the local class-group formula; those are supplied by the algebraic proof and standard determinantal-cone geometry.

## Relationship to prior work

McNeill proves the classification of toric positroid varieties by regularity, and the present family is a special toric family within that scope; toricity itself is **not** a novelty claim. The present statement specifies the complete affine local models, singular strata, multiplicities, and canonical-class threshold. Billey–Weaver and Fluegemann give smoothness tests for positroid varieties but do not, in the inspected material, give this family-wide transverse local-ring and Gorenstein classification. Friedman–Hoşten–Rosana study a rank-two matroid-variety singularity criterion, not the rank-at-least-three local models. Two related earlier computations concern the three-block rank-two case and the all-binary equal-block case; both are explicitly subsumed specializations, not claimed new here. The unrestricted higher-rank variable-block formula, including singular Gorenstein examples with \(a_i=r\), is the asserted extension. No exhaustive priority guarantee is claimed.

## Limitations

This theorem concerns only parallel extensions of \(U_{r,r+1}\), not arbitrary regular positroids, nonregular positroids, or non-consecutive block arrangements. The statement classifies the **reduced** singular locus, not its potentially nonreduced Jacobian singular scheme. It works over \(\mathbb C\). Prior-literature inspection may not exhaust older descriptions of toric monomial embeddings or local divisor class groups. Independent mathematical review has not been performed.

## References

1. Avery McNeill, *There are no unexpected toric positroid varieties*, arXiv:2610.35914, first posted 2026-10-07; in particular Theorem 1, Definition 2, and cited Knutson–Lam–Speyer scheme equations. https://arxiv.org/html/2610.35914v2
2. Sara C. Billey and Jordan E. Weaver, *A Pattern Avoidance Characterization for Smoothness of Positroid Varieties*, arXiv:2204.09013 (2022), especially Theorems 1.3–1.6. https://arxiv.org/pdf/2204.09013
3. Joseph Fluegemann, *Smooth Points on Positroid Varieties*, arXiv:2407.21116 (2024), abstract and announced tangent-space criterion. https://arxiv.org/abs/2407.21116
4. Hannah Friedman, Serkan Hoşten, and Andrea Rosana, *Euclidean Distance Optimization Within the Grassmannian*, arXiv:2610.02018 (2026), rank-two matroid-variety singularity discussion (full text not checked). https://arxiv.org/abs/2610.02018
5. W. Fulton, *Introduction to Toric Varieties* (1993), for standard toric and affine-cone divisor-class methods.
