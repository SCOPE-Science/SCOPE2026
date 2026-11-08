# Sharp skeletal minima and a single-crossing cutoff for products of disk-containing triangles

## Finding
For every integer \(m\ge2\), let \(T_1,\ldots,T_m\subset\mathbb R^2\) be nondegenerate triangles, each containing the unit Euclidean disk centered at the origin. In the orthogonal Cartesian product \(P=T_1\times\cdots\times T_m\subset\mathbb R^{2m}\), let \(\Phi_j(P)\) denote the sum of the Euclidean \(j\)-volumes of all \(j\)-dimensional faces (including \(\Phi_0\) as the vertex count and \(\Phi_{2m}\) as volume). Define
\[
H(t)=3\sqrt3+6\sqrt3\,t+3t^2,\qquad C_{m,k}=[t^k]H(t)^m.
\]
Then simultaneously for every integer \(0\le k\le2m\),
\[
\boxed{\Phi_{2m-k}(P)\ge C_{m,k}.}
\]
Every bound is attained by the Cartesian product of \(m\) equilateral triangles of inradius one centered at the origin. For \(k<2m\), equality holds only for these factors, up to rotations and permutations; for \(k=2m\), every product has \(3^m\) vertices and equality.

Set \(\delta=\sqrt{1-1/\sqrt3}\), \(u=1+\delta\), \(v=1-\delta\), and \(N=2m\). If \(e_k\) denotes the \(k\)-th elementary symmetric function of the list containing \(m\) copies of \(u\) and \(m\) copies of \(v\), define
\[
R_m(k)=\frac{C_{m,k}}{4^m\binom{2m}{k}}=
\left(\frac{3\sqrt3}{4}\right)^m\frac{e_k}{\binom{2m}{k}}.
\]
Then \(R_m(0)=R_m(1)>R_m(2)>\cdots>R_m(2m)=(3/4)^m\): every comparison after the first is strict. The first value exceeds one, and the last is below one. Consequently the integer
\[
K_m=\max\{k\in\{0,\ldots,2m\}: C_{m,k}\ge4^m\binom{2m}{k}\}
\]
is a single sharp cutoff: the cube-skeleton inequality \(\Phi_{2m-k}(P)\ge2^{2m}\binom{2m}{k}\) holds for **all** such products exactly for \(0\le k\le K_m\), while for every \(k>K_m\) the equilateral product violates it. In particular \(K_m\ge2\) for \(m\ge2\), recovering the ridge inequality for this product family (an already known consequence of a stronger planar-polygon product theorem). For \(m=2\), \(K_2=2\); more generally \(K_m\) for \(m=2,3,4,5,6,7,8\) is \(2,4,5,7,8,9,11\), respectively.

## Assumptions and scope
Here \(m\) is an arbitrary integer at least two. The triangles need not be regular, smooth, congruent, centrally symmetric, or aligned with one another. Their ambient coordinate planes are orthogonal: an arbitrary affine shear of the product is not included. The assumption \(B_2^2\subseteq T_i\) is weaker than the full face-distance hypothesis of the motivating ridge conjecture. For that conjecture's *admissible* subclass, additionally require each vertex of each \(T_i\) to have norm at least \(\sqrt2\). Facet lines have distance at least one automatically, and the product then satisfies all codimension-dependent face-distance hypotheses. The equilateral minimizers with inradius one do satisfy these stronger conditions because their vertices lie at radius two.

For \(k=2m\), the minimization is constant and equality is non-rigid. No assertion is made for arbitrary convex products other than triangles or for all admissible polytopes.

## Proof
**1. Planar sharp bounds.** A triangle \(T\) containing the centered unit disk has inradius \(r\ge1\). If its interior angles are \(\alpha_1,\alpha_2,\alpha_3\), the semiperimeter is
\[
s=r\sum_{i=1}^3\cot(\alpha_i/2).
\]
Since \(\cot\) is strictly convex on \((0,\pi/2)\) and \(\sum_i\alpha_i/2=\pi/2\), Jensen's inequality gives \(s\ge3\sqrt3\,r\). Thus the area \(A(T)=rs\ge3\sqrt3\), perimeter \(L(T)=2s\ge6\sqrt3\), and vertex count \(f_0(T)=3\). Simultaneous equality, or equality in either area or perimeter separately, requires an equilateral triangle of inradius one; because it contains the centered unit disk, its incenter is the origin.

**2. Multiplicative face measures.** The faces of an orthogonal Cartesian product are products of factor faces. Fubini's theorem for their intrinsic Euclidean volumes gives the polynomial identity
\[
\sum_{k=0}^{2m}\Phi_{2m-k}(P)t^k
=\prod_{i=1}^m\bigl(A(T_i)+L(T_i)t+3t^2\bigr).
\]
Every coefficient is nonnegative, so the planar lower bounds yield coefficientwise domination by \(H(t)^m\). The equilateral product realizes equality. For \(k<2m\), each individual factor's area or perimeter occurs in at least one strictly positive monomial contributing to the coefficient, hence a non-equilateral factor makes that coefficient strictly larger; at \(k=2m\) only the constant vertex counts contribute.

**3. Strict single crossing.** Put \(a=3\sqrt3\). Direct multiplication shows
\[
H(t)=a(1+ut)(1+vt),\qquad u+v=2,\quad uv=1/\sqrt3,\quad0<v<1<u.
\]
Thus \(C_{m,k}=a^m e_k\). Let \(b_k=e_k/\binom{2m}{k}\), with \(b_0=1\). Because the mean of the \(2m\) positive numbers is one, \(b_1=1\). Newton's inequalities say \(b_k^2\ge b_{k-1}b_{k+1}\), and equality at an internal index is possible only if all numbers are equal. Here \(u\ne v\), so the inequalities are strict. Hence \(b_1>b_2>\cdots>b_{2m}>0\), as the consecutive ratios begin below one and strictly decrease. Multiplication by \((a/4)^m>1\) gives the claimed ratio ordering, while \(R_m(2m)=(a uv/4)^m=(3/4)^m<1\). There is exactly one integer cutoff separating the nonnegative and negative cube-comparison coefficients (an equality at the boundary is allowed).

**4. The ridge cutoff.** For all \(m\ge2\),
\[
R_m(2)=\left(\frac{3\sqrt3}{4}\right)^m\left(1-\frac{1-1/\sqrt3}{2m-1}\right)
\ge \frac{27}{16}\left(1-\frac{1-1/\sqrt3}{3}\right)>1.
\]
Thus \(K_m\ge2\). The coefficient calculation for \(m=2\) gives \(C_{2,2}=108+18\sqrt3>96=4^2\binom42\) but \(C_{2,3}=36\sqrt3<64=4^2\binom43\), so \(K_2=2\). The other listed cutoffs follow by exact polynomial multiplication and comparison; the accompanying program checks these values and the strict ordering for \(m\le30\). The proof for all \(m\) is the analytic argument above, not this finite computation.

**5. Compatibility with the face-distance hypotheses.** Every face of \(P\) has the form \(F_1\times\cdots\times F_m\), and its squared distance from the origin's projection onto the affine hull is the sum of the corresponding squared distances of the factors. Each full triangle contributes zero codimension and distance, a facet contributes codimension one and squared distance at least one, and a vertex contributes codimension two and squared distance at least two. Therefore the stronger vertex hypothesis in the scope section implies the entire product is admissible under the motivating conjecture.

## Verification
The standard-library script `check_skeleta.py` performs exact arithmetic in \(\mathbb Q(\sqrt3)\), compares all coefficients with the cube profile for \(1\le m\le30\), checks the strict elementary-symmetric ratio ordering, and reproduces the listed cutoff values. It reports `EXACT_COEFFICIENT_CHECK_OK` with 1860 comparisons. It does **not** certify the universally quantified proof; the latter follows from product-face decomposition, Jensen's inequality, and the classical Newton inequalities.

## Relationship to prior work
Zwierzyński's *A Sharp Surface-Area Extension of Vaaler's Theorem* proves the surface inequality for general face-distance admissible polytopes, proposes its ridge-skeleton extension as Conjecture 5.2, and asks for the valid codimension range in Question 5.5. Its Section 5 already contains the face-measure product identity and counterexamples to the unrestricted higher-skeleton extension. Those statements are acknowledged. An earlier result (research item `09ff8fbc-913e-4d9f-929a-8571e972b582`) already proves the ridge inequality, with a sharp triangle-factor excess, for *all* admissible planar-polygon-and-interval products. Thus neither the product identity nor the ridge case is claimed as new here. The proposed contribution is the **sharp all-codimension coefficient profile**, **rigidity**, and **single-crossing classification of the allowable codimension range** for products of planar triangles. The lower bounds on area and perimeter of disk-containing triangles and Newton–Maclaurin inequalities are classical inputs, not novel theorems. Earlier integral-geometric work by Burton on convex-body skeleta is related, but the available abstract does not resolve this parameter-specific extremal profile.

## Limitations
No bound for arbitrary admissible polytopes, arbitrary products of polygons, sheared products, or nonsimplicial factors is established. This result does not determine the global \(k_{\max}(n)\) from Question 5.5. The explicit sequence \(K_m\) is exactly characterized by finite coefficient comparisons rather than a simpler closed formula; no asymptotic formula is claimed. Older skeletal-geometry literature could contain an equivalent all-codimension statement; historical priority remains provisional. The ridge inequality itself was already established in a more general product class. No independent audit has been performed.

## References
1. M. Zwierzyński, *A Sharp Surface-Area Extension of Vaaler's Theorem* (2026), arXiv:2609.27798, particularly Section 5, Proposition 5.1, Conjecture 5.2 and Question 5.5. https://arxiv.org/abs/2609.27798
2. G. R. Burton, *The measure of the s-skeleton of a convex body*, Mathematika 26 (1979), 290–301. https://doi.org/10.1112/S0025579300009839
3. G. R. Burton, *Skeleta and sections of convex bodies*, Mathematika 27 (1980), 97–103. https://doi.org/10.1112/S0025579300009980
4. Classical Newton–Maclaurin inequalities for normalized elementary symmetric functions. A modern related reference is T. Tao, *A Maclaurin type inequality* (2023), arXiv:2310.05328.
