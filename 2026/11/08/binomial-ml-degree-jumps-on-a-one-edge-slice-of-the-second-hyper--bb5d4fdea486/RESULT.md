# Binomial ML-degree jumps on a one-edge slice of the second hypersimplex

## Finding
For each integer \(d\ge7\), let \(V_d(t)\) be the scaled toric variety associated with the exponent vectors \(e_i+e_j\), \(1\le i<j\le d\), with coefficients \(c_{ij}=1\) except \(c_{12}=t\in\mathbb C^*\). Its maximum-likelihood degree is
\[
\operatorname{MLdeg}V_d(t)=2^{d-1}-d-\begin{cases}
\binom{d-2}{k},&t=2k/(k-1)\text{ for some integer }2\le k\le d-2,\\
0,&\text{otherwise}.
\end{cases}
\]
The exceptional values are pairwise distinct. At the exceptional value indexed by \(k\), exactly \(\binom{d-2}{k}\) principal submatrices lose rank; these are indexed by subsets of size \(k+2\) containing both distinguished coordinates. For \(k\le d-3\), the full scaling matrix still has rank \(d\).

## Assumptions and scope
Work over \(\mathbb C\), with \(d\ge7\) and \(t\ne0\). The projective toric variety is the closure of
\[
[x_1:\cdots:x_d]\longmapsto[c_{ij}x_ix_j]_{1\le i<j\le d}
\]
from the dense projective torus. The generic-data maximum-likelihood degree is the number of critical points of the likelihood function on the appropriate very affine locus, counted without multiplicity for generic data. Use the symmetric matrix \(C_d(t)\) with zero diagonal and off-diagonal entries \(c_{ij}\). All other scalings stay exactly 1.

## Proof
**1. The principal-rank phase diagram.** Let \(S\subseteq\{1,\ldots,d\}\) be nonempty, and write \(s=|S|\). If \(S\) misses either of 1,2, its principal matrix is \(J_s-I_s\), whose determinant is \((-1)^{s-1}(s-1)\) for \(s\ge2\). A one-element principal matrix has rank zero, irrespective of \(t\). If \(S=\{1,2\}\), its determinant is \(-t^2\). For \(S\supseteq\{1,2\}\) and \(s=k+2\) with \(k\ge1\), split its space into the antisymmetric coordinate direction on the distinguished pair (eigenvalue \(-t\)), the \(k-1\)-dimensional sum-zero subspace of the remaining coordinates (eigenvalue \(-1\)), and the two-dimensional space of vectors constant on each part. On the last space the matrix is
\[
\begin{pmatrix}t&k\\2&k-1\end{pmatrix}.
\]
Thus its determinant is \((-t)(-1)^{k-1}[t(k-1)-2k]\). For \(k=1\) this never vanishes when \(t\ne0\). For \(k\ge2\) it vanishes exactly at \(t_k=2k/(k-1)\), with corank exactly one, since the other eigenvalues are nonzero and the displayed two-by-two block has rank one. The \(t_k\) are strictly decreasing in \(k\), so no two ranks drop simultaneously. This proves the stated multiplicity \(\binom{d-2}{k}\) of affected principal subsets.

**2. Euler characteristic of a projective quadric of given rank.** For a nonempty subset \(S\), let \(Q_S\subset\mathbb P^{s-1}\) be the projective quadric defined by the restriction of \(f_t=\sum_{i<j}c_{ij}x_ix_j\) to coordinates in \(S\). If its symmetric matrix has rank \(r\ge2\), then \(Q_S\) is a cone with vertex \(\mathbb P^{s-r-1}\) (empty when \(r=s\)) over a nonsingular quadric of dimension \(r-2\). The complement of the vertex is an affine \((s-r)\)-bundle over the smooth quadric. Therefore
\[
\chi(Q_S)=s-r+\chi(Q_{\mathrm{smooth}}^{r-2})=s-1+\mathbf1_{\{r\text{ even}\}}.
\]
This follows from the standard cell decomposition of a nonsingular complex quadric, whose Euler characteristic is \(r-1\) for odd \(r\), and \(r\) for even \(r\). For \(s=1\), the quadratic equation is zero and \(\chi(Q_S)=1\); it is constant in \(t\). Hence an isolated rank change from \(s\) to \(s-1\), where \(s\ge4\), alters \(\chi(Q_S)\) by \((-1)^{s+1}\).

**3. Torus inclusion-exclusion and the exact ML-degree jump.** Put \(T=\{[x_1:\cdots:x_d]\in\mathbb P^{d-1}:x_1\cdots x_d\ne0\}\) and \(Q_t=\{f_t=0\}\). The standard likelihood Euler-characteristic theorem, applied to the second-hypersimplex torus, gives
\[
\operatorname{MLdeg}V_d(t)=(-1)^d\chi(Q_t\cap T).
\]
Indeed, \(T\simeq(\mathbb C^*)^{d-1}\) has Euler characteristic zero and the ML degree equals \((-1)^{d-1}\chi(T\setminus Q_t)\). Inclusion-exclusion on coordinate hyperplanes yields
\[
\chi(Q_t\cap T)=\sum_{\varnothing\ne S\subseteq[d]}(-1)^{d-|S|}\chi(Q_S).
\]
At \(t=t_k\), there are \(N=\binom{d-2}{k}\) changed subsets, each of size \(s=k+2\). Relative to generic \(t\), every such subset changes the ML degree by \((-1)^d(-1)^{d-s}(-1)^{s+1}=-1\). All other subsets contribute identically. Hence the total ML-degree drop is exactly \(N\).

**4. Generic baseline.** For all \(t\ne0\) outside the finite exceptional set, every principal submatrix of order at least two is nonsingular. In particular the principal \(A\)-determinant of the second hypersimplex is nonzero. Therefore the ML degree equals the projective degree of the toric model, namely the normalized volume of \(\Delta(2,d)\), which is the Eulerian number \(2^{d-1}-d\). This proves the formula. The determinant calculation also shows that for \(k\le d-3\), the full principal matrix (with \(d-2\) unmarked coordinates) is nonsingular at \(t=t_k\).

## Verification
The attached exact-arithmetic `CHECK.py` enumerates every principal coordinate subset, calculates its matrix rank using rational Gaussian elimination, constructs the projective-quadric Euler characteristic and sums the alternating torus inclusion-exclusion formula. It checks several generic rational scalings and all exceptional scalings for every \(4\le d\le9\), including that precisely the predicted subsets lose rank. The output ends in `ALL_CHECKS_OK`. The finite checks do not replace the proof for arbitrary \(d\).

For illustration, \(d=7\) has generic ML degree \(57\), but at \(t=4,3,8/3,5/2\), the values are \(47,47,52,56\), respectively; the first three of these occur with full-rank scaling matrix. These illustrate three different binomial degeneracy multiplicities (with the first two numerically equal by binomial symmetry).

## Relationship to prior work
Oldekop (2026, arXiv:2606.16482v1) connects maximum-likelihood degree of second-hypersimplex scalings to Euler characteristics of torus quadrics, gives general results for rank-three and rank-four matrices, and explicitly studies orders at most six. Clarke–Hoşten–Kushnerchuk–Oldekop (2024, arXiv:2312.10010v2) determines the principal \(A\)-determinant and computes low-order ML-degree stratifications. The present statement evaluates the entire one-edge scaling line for all orders at least seven. It is not an arbitrary-scaling classification or a proof of the minimum-ML-degree conjecture. The exact transition parameters and binomial jumps require the principal-rank calculation and all-rank Euler inclusion-exclusion above; they are not quoted from either article.

## Limitations
The parameter family is one-dimensional; no formula is asserted for multiple perturbed edges, arbitrary complex scaling matrices, or the singularity schemes of the discriminant. The asserted priority is subject to independent literature verification. Exact calculations cover only finite values of \(d\), and the unrestricted theorem depends on the written argument.

## References
- J. Oldekop, *Euler Stratifications of Second Hypersimplices via Delta-matroids*, arXiv:2606.16482v1 (first public 2026-06-15), Sections 1–5.
- O. Clarke, S. Hoşten, N. Kushnerchuk, J. Oldekop, *Matroid Stratification of ML Degrees of Independence Models*, arXiv:2312.10010v2 (2024), Section 3.
- C. Améndola et al., *The Maximum Likelihood Degree of Toric Varieties*, arXiv:1703.02251 (2017; journal version 2019), generic-scaling criterion.
