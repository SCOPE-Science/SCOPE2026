# A rank-one covariance gap between enriched order and chain polytopes

## Finding
Let \(m,n\ge1\) be integers, put \(d=m+n\), and let \(P_{m,n}=A_m\oplus A_n\) be the ordinal sum of an \(m\)-element antichain (lower level) and an \(n\)-element antichain (upper level). Let \(\mathcal O_{m,n}^{(e)}\) and \(\mathcal C_{m,n}^{(e)}\) be its enriched order and enriched chain polytopes in their canonical \(\mathbb R^m\times\mathbb R^n\) coordinates. For any full-dimensional convex body \(K\), let \(\Sigma_K\) denote the covariance of its normalized uniform interior measure, and define its squared isotropic constant by
\[
L(K)^2=\frac{(\det\Sigma_K)^{1/d}}{\operatorname{vol}_d(K)^{2/d}}.
\]
Write \(I_j\) for the identity matrix and \(J_j=\mathbf1_j\mathbf1_j^{\mathsf T}\) for the all-ones matrix. Define
\[
a_j=\frac{(j+1)(j+2)}{3(d+1)(d+2)},\qquad
b_{m,n}=\frac{m(n+1)}{(d+1)^2(d+2)}.
\]
Then the centroids and complete covariance matrices are
\[
\begin{aligned}
\operatorname{cent}(\mathcal C_{m,n}^{(e)})&=0,&
\Sigma_{\mathcal C_{m,n}^{(e)}}&=
\begin{pmatrix}a_m I_m&0\\0&a_n I_n\end{pmatrix},\\
\operatorname{cent}(\mathcal O_{m,n}^{(e)})&=(0_m,\tfrac{m}{d+1}\mathbf1_n),&
\Sigma_{\mathcal O_{m,n}^{(e)}}&=
\begin{pmatrix}a_m I_m&0\\0&a_n I_n+b_{m,n}J_n\end{pmatrix}.
\end{aligned}
\]
In particular, the order-minus-chain covariance is the positive rank-one matrix
\[
\boxed{\Sigma_{\mathcal O_{m,n}^{(e)}}-\Sigma_{\mathcal C_{m,n}^{(e)}}=b_{m,n}\,(0_m,\mathbf1_n)(0_m,\mathbf1_n)^{\mathsf T}.}
\]
The polytopes have equal Euclidean volume, as required by the published enriched Ehrhart correspondence, and the common volume is
\[
\operatorname{vol}_d(\mathcal O_{m,n}^{(e)})=
\operatorname{vol}_d(\mathcal C_{m,n}^{(e)})
=2^d\frac{m!n!}{d!}.
\]
Their affine-invariant isotropic constants nevertheless satisfy the exact strict inequality
\[
\boxed{\left(\frac{L(\mathcal O_{m,n}^{(e)})}
{L(\mathcal C_{m,n}^{(e)})}\right)^{2d}
=1+\frac{3mn}{(d+1)(n+2)}\in(1,4).}
\]
The constant \(4\) is the sharp universal supremum (not attained): for \(m=t^2,n=t\), the displayed ratio tends to \(4\) as \(t\to\infty\). Reversing the two levels replaces \(n+2\) by \(m+2\); the two numerical isotropic constants are unequal whenever \(m\ne n\), although the two dual-poset enriched order polytopes have the same Ehrhart polynomial. The latter distinction is an exact metric/affine-invariant quantification, not a claim that the dual orientations were previously known to be combinatorially equivalent.

## Assumptions and scope
The poset is complete across levels: every lower element precedes every upper element, with no comparisons within a level. The enriched chain polytope is the convex hull of all signed characteristic vectors of antichains. The enriched order polytope is the convex hull of sign-valued order filters, with negative entries allowed only at minimal elements of their support. In these conventions, writing \(B_j=[-1,1]^j\), the two polytopes are exactly
\[
\mathcal C_{m,n}^{(e)}=\operatorname{conv}(B_m\times\{0_n\},\{0_m\}\times B_n),
\qquad
\mathcal O_{m,n}^{(e)}=\operatorname{conv}(B_m\times\{\mathbf1_n\},\{0_m\}\times B_n).
\]
Each is full-dimensional, and the formulas use the canonical coordinate Lebesgue measure (not normalized lattice volume) and its uniform interior probability distribution. The quantity \(L(K)\) is invariant under invertible affine transformations. Indices \(m,n\) have distinct roles for enriched order polytopes; swapping them is not assumed to be a metric or affine symmetry. All boundaries have measure zero.

## Proof
**1. Defining geometry and volume.** An antichain of \(P_{m,n}\) is entirely contained in one level. An order filter is either a subset of the upper level or contains some lower elements and hence all upper elements. In the second case, only the chosen lower elements can be negative, whereas every upper coordinate is \(1\). Convexification gives precisely the two displayed convex-hull formulas. Equivalently,
\[
\mathcal O_{m,n}^{(e)}=
\{(x,y):y_i\le1,\ |x_j|\le(1+\min_i y_i)/2\quad\forall i,j\}.
\]
The displayed inequalities imply \(y_i\ge-1\) automatically. Indeed, a convex combination with weight \(\lambda\) on the first cube requires \(\|x\|_\infty\le\lambda\) and \(y_i\in[-1+2\lambda,1]\), so such a \(\lambda\in[0,1]\) exists if and only if these constraints hold. For fixed \(y\in B_n\), the \(x\)-section is a cube of side length \(1+\min_i y_i\). Set \(T=(1+\min_i y_i)/2\). Under unweighted uniform \(y\in B_n\), the density of \(T\) is \(n(1-t)^{n-1}\) for \(0<t<1\). Integrating section volumes gives
\[
\operatorname{vol}_d(\mathcal O_{m,n}^{(e)})
=2^d n\int_0^1t^m(1-t)^{n-1}\,dt
=2^d\frac{m!n!}{d!}.
\]
The same volume for \(\mathcal C_{m,n}^{(e)}\) follows either from the enriched Ehrhart equality or directly from the volume formula for the \(\ell_1\)-sum of the two cubes.

**2. Enriched order covariance.** In uniform interior measure on \(\mathcal O_{m,n}^{(e)}\), the variable \(T\) has the Beta distribution with shape parameters \(m+1,n\). Consequently,
\[
\mathbb E T=\frac{m+1}{d+1},\quad
\operatorname{Var}T=\frac{(m+1)n}{(d+1)^2(d+2)},\quad
\mathbb E T^2=\frac{(m+1)(m+2)}{(d+1)(d+2)},\quad
\mathbb E(1-T)^2=\frac{n(n+1)}{(d+1)(d+2)}.
\]
Given \(T=t\), the lower vector \(X\) is uniformly distributed on \([-t,t]^m\), independent of the upper vector conditioned on its minimum. Hence its covariance is \(\mathbb E(T^2)I_m/3=a_m I_m\), with no cross-covariance with \(Y\).

Conditioned on \(T=t\), the minimum upper coordinate equals \(2t-1\), and its index \(H\) is uniform on \(\{1,\ldots,n\}\). The remaining coordinates are independent uniforms on \([2t-1,1]\). Accordingly, for every \(i\),
\[
\mathbb E(Y_i\mid T=t)=\frac{(n+1)t-1}{n}.
\]
The unconditional mean simplifies to \(\mathbb E Y_i=m/(d+1)\). For distinct \(i,j\), the conditional covariance equals \(-(1-t)^2/n^2\), because the indicators of the disjoint events \(H=i\) and \(H=j\) have covariance \(-1/n^2\) and the residual uniform noises are conditionally uncorrelated. For each coordinate the conditional variance is \((n-1)(n+3)(1-t)^2/(3n^2)\). Total covariance and the four Beta moments yield
\[
\operatorname{Cov}(Y_i,Y_j)=\frac{m(n+1)}{(d+1)^2(d+2)}=b_{m,n}\quad(i\ne j),
\]
and
\[
\operatorname{Var}(Y_i)=a_n+b_{m,n}.
\]
When \(n=1\) the off-diagonal assertion is vacuous, and the same diagonal formula follows directly. This proves the order covariance matrix for every allowed parameter.

**3. Enriched chain covariance.** Define block radii \(R=\|X\|_\infty\) and \(S=\|Y\|_\infty\). The free-sum body is \(\{R+S\le1\}\). In uniform interior measure, shell integration gives \((R,S,1-R-S)\) a Dirichlet distribution with parameters \((m,n,1)\). Thus
\[
\mathbb E R^2=\frac{m(m+1)}{(d+1)(d+2)},\quad
\mathbb E S^2=\frac{n(n+1)}{(d+1)(d+2)}.
\]
At a fixed nonzero radius \(R\), symmetry and the uniform cube shell show that one of the \(m\) lower absolute coordinates is \(R\), and the other \(m-1\) absolute coordinates are uniform on \([0,R]\). Therefore \(\mathbb E(X_i^2\mid R)=R^2(m+2)/(3m)\). Coordinate-sign symmetry eliminates every mean and every off-diagonal covariance. Its lower covariance is \(a_mI_m\), and the upper covariance is similarly \(a_nI_n\). This also follows from the general covariance recursion for \(\ell_1\)-sums of centrally symmetric bodies; that underlying recursion is not claimed as new.

**4. Determinant, strictness, sharpness.** The order-minus-chain formula is immediate by subtraction. By the matrix determinant lemma,
\[
\frac{\det\Sigma_{\mathcal O_{m,n}^{(e)}}}
{\det\Sigma_{\mathcal C_{m,n}^{(e)}}}
=\frac{\det(a_n I_n+b_{m,n}J_n)}{a_n^n}
=1+\frac{n b_{m,n}}{a_n}
=1+\frac{3mn}{(d+1)(n+2)}.
\]
Equality of the volumes converts this identity to the claimed ratio of affine-invariant isotropic constants. Positivity of \(m,n\) makes it greater than \(1\); the factorization
\[
\frac{mn}{(d+1)(n+2)}=\frac{m}{d+1}\cdot\frac{n}{n+2}<1
\]
makes it strictly less than \(4\). For \(m=t^2,n=t\) both factors tend to \(1\), proving the supremum is \(4\) and is never attained. Swapping \(m,n\) changes the positive factor from \(1/(n+2)\) to \(1/(m+2)\), so the isotropic constants for the two level orientations differ if and only if \(m\ne n\).

## Verification
Run `python verification/verify.py` from the extracted package after installing the packages in `verification/requirements.txt`. The script reconstructs the explicitly given generating vertices of both polytopes. In dimensions \(2\) through \(5\), including \((m,n)=(1,1),(1,2),(2,1),(1,3),(3,1),(2,2),(2,3),(3,2)\), it uses numerical convex-hull face incidences to form a star triangulation about the known strict interior point \(0\), but computes each simplex's determinant, volume, first moment, and second moment **exactly over rational integers**. This independently verifies every covariance entry and the common volume in those eight parameter pairs, without using the Beta/Dirichlet derivation. Additionally, rational arithmetic checks the determinant lemma identity, strict \((1,4)\) bound, and level-reversal criterion for all \(22{,}500\) pairs \(1\le m,n\le150\) and one explicit near-sharp pair. The hull stage uses floating point only to identify faces; exact integer determinants determine the claimed moment equalities. These finite computations are corroboration, not a proof of the all-parameter theorem.

## Relationship to prior work
Ohsugi and Tsuchiya introduced enriched chain polytopes, including their signed-antichain vertex construction and their \(2^d\) volume relation with ordinary chain polytopes [1]. They later introduced enriched order polytopes and proved their equal Ehrhart polynomials [2]. Okada and Tsuchiya formulated the transfer map and triangulations between these enriched objects [3], and their vertex and inequality statements support the two-level realizations used here. These results are prerequisites, not new claims. A published general analysis of isotropic constants for Hanner polytopes supplies the covariance recursion for the enriched **chain** partner (a free sum of cubes) [4]; this half of the covariance formula is therefore credited. The new claim is the exact **enriched order** covariance, its positive rank-one difference, and the sharp quantitative isotropic-constant comparison. A published two-level signed-chain volume formula concerns the distinct body defined by \(|x_i+y_j|\le1\) together with singleton bounds, rather than either of the two convex hulls here [5]. The standard order/chain covariance identities for ordinary (unsigned) posets do not imply the signed enriched order formula: their volumes differ by a factor of \(2^d\) and their defining vertices are different.

## Limitations
No assertion is made for posets of more than two complete levels, partial comparability graphs, or arbitrary enriched order polytopes. The covariance comparison is between fixed canonical coordinate realizations; its Loewner-matrix order is not preserved under unrelated changes of coordinates. The isotropic constant is affine invariant. The strict inequality does not itself establish a first-known affine inequivalence between the dual level orders (their facet structures already distinguish them when the sizes differ). Historical priority remains subject to additional literature under optimal-design, probabilistic convexity, and enriched-poset terminology. The verification script's finite triangulations do not replace the universal integral proof.

## References
[1] H. Ohsugi and A. Tsuchiya, *Enriched chain polytopes*, arXiv:1812.02097v1, first public 2018-12-05, https://arxiv.org/abs/1812.02097.

[2] H. Ohsugi and A. Tsuchiya, *Enriched order polytopes and enriched Hibi rings*, arXiv:1903.00909v1, first public 2019-03-03, https://arxiv.org/abs/1903.00909; European Journal of Mathematics 7 (2021).

[3] S. Okada and A. Tsuchiya, *Two enriched poset polytopes*, arXiv:2003.12271v1, first public 2020-03-27, https://arxiv.org/abs/2003.12271; Annals of Combinatorics 28 (2024).

[4] *Sharp isotropic-constant range of all Hanner polytopes*, public mathematical research record (2026), identifier `7976b0937cd2`; general \(\ell_1\)-sum covariance recursion, not the enriched order formula.

[5] *Exact volume and strict imbalance law for two-level signed-chain polytopes*, public mathematical research record (2026), identifier `84c1d3d87a65`; defines a different signed-chain halfspace body.
