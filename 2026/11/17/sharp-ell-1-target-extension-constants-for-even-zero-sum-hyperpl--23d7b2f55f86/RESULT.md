# Sharp \(\ell_1\)-target extension constants for even zero-sum hyperplanes

## Finding
For every even integer \(n\ge2\), the optimal uniform norm-inflation factor for real-linear operators from the zero-sum hyperplane of \(\ell_1^n\) into arbitrary finite-dimensional real \(\ell_1\) targets is exactly
\[
\mathrm{POE}_1(H_n,\ell_1^n)=\frac{2(n-1)}{n}.
\]
An explicit finite-dimensional target and one operator attain this constant for each even \(n\). For positive-diameter configurations, the corresponding extremal finite metric geometry has optimal enclosing-radius-to-diameter ratio \((n-1)/n\).

## Assumptions and scope
All vector spaces and operators are **real**. Fix an even integer \(n=2k\ge2\). Let
\[
E=\ell_1^n,\qquad H_n=\{x\in E:\sum_{i=1}^n x_i=0\}.
\]
The norm of \(H_n\) is inherited from \(E\). Define the number \(C_n\) to be the least \(C\ge1\) for which every integer \(m\ge1\) and bounded linear map \(R:H_n\to\ell_1^m\) admits an extension \(\widetilde R:E\to\ell_1^m\) with \(\|\widetilde R\|\le C\|R\|\). The result determines \(C_n\) only for **even** \(n\), and does not assert a bound for other target Banach spaces or complex scalars.

## Proof
**1. Reduction to an enclosing-ball problem.** Every \(R:H_n\to\ell_1^m\) has a representation
\[
R(x)=\sum_{i=1}^n x_iv_i,\qquad v_i\in\ell_1^m.
\]
The vectors \(v_i\) are unique up to adding a common vector. The unit ball of \(H_n\) is the convex hull of the vectors \(\pm(e_i-e_j)/2\) for \(i\ne j\). Indeed, a zero-sum vector has equal positive and negative mass, and any transportation coupling between its positive and negative coordinates decomposes it as such a convex combination after scaling. Thus
\[
\|R\|=\frac12D,\qquad D=\max_{i,j}\|v_i-v_j\|_1.
\]
Every extension of \(R\) has column vectors \(v_i-c\) for one common \(c\in\ell_1^m\). Since the domain is \(\ell_1^n\), its operator norm is \(\max_i\|v_i-c\|_1\). Therefore
\[
\inf_{\widetilde R|_{H_n}=R}\|\widetilde R\|
=\min_{c\in\ell_1^m}\max_i\|v_i-c\|_1=:r(v_1,\dots,v_n).
\]
The minimum exists in finite dimension. These equalities establish the claimed geometric equivalence with the \(n\)-point Jung ratio.

**2. Universal upper bound.** For \(c=n^{-1}\sum_jv_j\), the triangle inequality gives, for every \(i\),
\[
\|v_i-c\|_1=\left\|\frac1n\sum_{j\ne i}(v_i-v_j)\right\|_1
\le\frac{n-1}nD.
\]
Hence \(r\le(n-1)D/n\), so \(C_n\le2(n-1)/n\). This inequality holds for **all** \(n\ge2\), although sharpness below is shown only when \(n\) is even.

**3. Balanced-subset extremizers.** Let \(k=n/2\) and let \(\mathcal S\) be all \(k\)-element subsets of \(\{1,\dots,n\}\). Take \(m=|\mathcal S|=\binom nk\), and define \(v_i\in\ell_1^m\) coordinatewise by
\[
(v_i)_S=\begin{cases}1&i\in S,\\-1&i\notin S.\end{cases}
\]
For distinct \(i,j\), exactly \(2\binom{n-2}{k-1}\) subsets contain precisely one of them, and each such coordinate contributes \(2\) to the distance. Thus
\[
D=4\binom{n-2}{k-1}=
\frac{n}{n-1}\binom nk=\frac{nm}{n-1}.
\]
For any proposed center \(c=(c_S)\), each coordinate \(S\) contains exactly \(k\) positive and \(k\) negative entries across \(v_1,\dots,v_n\). Thus, by the scalar triangle inequality,
\[
\sum_{i=1}^n |(v_i)_S-c_S|
=k(|1-c_S|+|-1-c_S|)\ge2k=n.
\]
Summing over coordinates gives \(\max_i\|v_i-c\|_1\ge m\). The center \(c=0\) satisfies \(\|v_i\|_1=m\) for every \(i\), so \(r=m\). Consequently
\[
\frac{2r}{D}=\frac{2m}{nm/(n-1)}=\frac{2(n-1)}n,
\]
matching the upper bound. Defining \(R(x)=\sum_i x_iv_i\) on \(H_n\) makes this a concrete operator attaining the claimed constant. \(\square\)

## Verification
The accompanying standalone `balanced_checker.py` uses only the Python standard library. It enumerates each balanced-subset configuration for \(n=2,4,6,8,10,12\) with exact integers and checks the radius lower-bound certificate, all pair distances, and the ratio \(2(n-1)/n\) as exact rational numbers. These finite checks are corroborative; Steps 1–3 prove the statement for every even positive \(n\).

## Relationship to prior work
Pariente-Martín and Tradacete (2026, arXiv:2611.00451v1), especially Theorems 1.3 and 4.1 and its introductory definition of POE-\(p\), connect operator extension properties to order continuity of induced homomorphisms of free Banach lattices. Their inspected text establishes qualitative equivalences but not the explicit sharp even-dimensional \(\ell_1\)-target constant above. The foundational work of Oikhberg, Taylor, Tradacete and Troitsky (arXiv:2210.00614) develops POE-\(p\) generally; only its publicly available abstract and citations were inspected here, so its full-text priority risk remains. The elementary mean-center upper bound is classical in finite metric geometry; sharpness for this *particular operator-extension invariant* requires the balanced-subset realization.

## Limitations
The result is confined to even dimensions, real scalars and finite \(\ell_1\) targets. It does not compute the odd-dimensional sharp value, and it does not assert novelty of the general mean-center bound, the POE definition, or the qualitative free-Banach-lattice criterion. Unindexed equivalent finite-dimensional Jung or extension formulations remain a bibliographic risk. No independent mathematical audit has been performed.

## References
1. R. E. Pariente-Martín and P. Tradacete, *Order continuity of induced homomorphisms between free Banach lattices*, arXiv:2611.00451v1 (first public 2026-10-30), https://arxiv.org/html/2611.00451v1.
2. T. Oikhberg, M. A. Taylor, P. Tradacete and V. G. Troitsky, *Free Banach lattices*, arXiv:2210.00614 (first public 2022-10-02), https://arxiv.org/abs/2210.00614.
