# Walsh blind spots in cubical sampling of individual spherical-harmonic degrees

## Finding
Let \(d\ge 6\) be an integer, \(X_d=\{d^{-1/2}(\varepsilon_1,\ldots,\varepsilon_d):\varepsilon_i\in\{-1,1\}\}\subset S^{d-1}\), and \(\mathcal H_\ell(\mathbb R^d)\) be the complex vector space of homogeneous harmonic polynomials of degree \(\ell\). For each integer \(0\le\ell\le d+2\), restrict its functions to \(X_d\), obtaining \(E_{d,\ell}:\mathcal H_\ell\to\mathbb C^{X_d}\). Write \(W_j\) for the \(\binom dj\)-dimensional span of Walsh characters \(\chi_I(\varepsilon)=\prod_{i\in I}\varepsilon_i\) indexed by subsets \(I\subseteq\{1,\ldots,d\}\) of size \(j\).

**Complete degree-wise image theorem.** Define
\[
J_{d,\ell}=\{j:0\le j\le\min(d,\ell),\ j\equiv\ell\pmod 2\}\setminus\bigl(\{0\}\text{ if }\ell=2\bigr)\setminus\bigl(\{d\}\text{ if }\ell=d+2\bigr).
\]
The image is exactly the orthogonal direct sum
\[
\operatorname{im}E_{d,\ell}=\bigoplus_{j\in J_{d,\ell}}W_j.
\]
In particular,
\[
\operatorname{rank}E_{d,\ell}=\sum_{\substack{0\le j\le\min(d,\ell)\\j\equiv\ell\ (\mathrm{mod}\ 2)}}\binom dj-\mathbf1_{\{\ell=2\}}-\mathbf1_{\{\ell=d+2\}}.
\]
For degrees \(\ell=d-1,d,d+1\), restriction realizes the entire parity subspace of \(\mathbb C^{X_d}\), of dimension \(2^{d-1}\). At the next degree, \(\ell=d+2\), the rank is exactly \(2^{d-1}-1\): the full-parity Walsh character disappears while every other permitted character remains. The other exceptional deletion is the constant character at degree \(2\).

## Assumptions and scope
All polynomials are over \(\mathbb C\), harmonic for the standard Euclidean Laplacian \(\Delta=\sum_{i=1}^d\partial_{x_i}^2\), and homogeneous in the ambient variables. The cube vertices lie on the unit sphere. Orthogonality in \(\mathbb C^{X_d}\) means uniform counting measure over its \(2^d\) points. The assertion concerns a **single harmonic degree** at a time and covers \(d\ge6\), \(0\le\ell\le d+2\); it does not claim the same two-exception formula for arbitrarily high degrees or for general cubature nodes.

## Proof
**1. Parity restrictions.** The coordinate sign-change group \(\{\pm1\}^d\) preserves both \(\mathcal H_\ell\) and \(X_d\), so \(\operatorname{im}E_{d,\ell}\) is invariant under the regular sign-change action on the vertex functions. Each Walsh character occurs with multiplicity one; consequently the image is a direct sum of individual character lines. If a homogeneous degree-\(\ell\) polynomial has nonzero component of parity \(\chi_I\), each variable in \(I\) must occur to odd exponent; thus \(|I|\le\ell\) and \(|I|\equiv\ell\pmod2\). These are the proposed permitted levels before exceptions.

**2. Every interior Walsh character occurs.** Fix \(I\) with \(1\le j=|I|\le d-1\), \(j\le\ell\) and \(j\equiv\ell\pmod2\). Choose \(a\in I\), \(b\notin I\), and set \(m=(\ell-j)/2\). Then
\[
H_I(x)=\left(\prod_{i\in I\setminus\{a\}}x_i\right)\operatorname{Re}(x_a+i x_b)^{2m+1}
\]
is a homogeneous harmonic polynomial of degree \(\ell\): the last factor is a planar harmonic polynomial, and each other displayed variable occurs only linearly and in a disjoint coordinate. On every vertex of \(X_d\), its value equals \(c_{d,\ell,j}\chi_I(\varepsilon)\), where
\[
c_{d,\ell,j}=d^{-\ell/2}2^{m+1/2}\cos\bigl((2m+1)\pi/4\bigr)\ne0.
\]
The cosine is nonzero because \(2m+1\) is odd. Thus the entire Walsh line of \(I\) belongs to the restriction image.

**3. The constant character.** At \(\ell=0\), the constant polynomial works. At \(\ell=2\), the mean over the cube of any homogeneous quadratic \(P\) equals \(d^{-1}\) times the sum of the squared-coordinate coefficients of \(P\). Harmonicity makes this trace zero. Since degree two also has only the constant and degree-two Walsh levels, the constant level is genuinely missing.

For every positive multiple \(\ell=4m\), the harmonic polynomial \(\operatorname{Re}(x_1+i x_2)^{4m}\) takes the same nonzero value at all cube vertices. For every \(\ell=4m+2\ge6\), first set \(R^2=x_1^2+x_2^2+x_3^2\) and
\[
Q_6(x_1,x_2,x_3)=R^6P_6(x_1/R),\quad P_6(t)=\frac{231t^6-315t^4+105t^2-5}{16}.
\]
This is a homogeneous harmonic polynomial of degree six in its three variables. On any cube vertex its value is \((3/d)^3P_6(1/\sqrt3)=6/d^3\ne0\), because \(P_6(1/\sqrt3)=2/9\). For \(m=1\), take \(Q_6\). For \(m\ge2\), multiply it by \(\operatorname{Re}(x_4+i x_5)^{4m-4}\). The factors depend on disjoint coordinates, so the product is harmonic. Each factor has a nonzero constant value on the cube, giving the required constant Walsh component in every even degree at least four. The hypothesis \(d\ge6\) guarantees the available coordinates.

**4. The top Walsh character.** Let \(I=\{1,\ldots,d\}\). At degree \(\ell=d\), the harmonic monomial \(x_1\cdots x_d\) realizes \(\chi_I\). For \(0\le\ell\le d+2\), the only other possible degree of the same parity admitting this character is \(\ell=d+2\). Projection of an arbitrary degree-\(d+2\) harmonic polynomial onto this sign character preserves harmonicity. Every polynomial of the required full odd parity and total degree \(d+2\) has the form
\[
P(x)=x_1\cdots x_d\sum_{i=1}^d a_i x_i^2.
\]
Direct differentiation gives \(\Delta P=6(x_1\cdots x_d)\sum_i a_i\), so harmonicity forces \(\sum_i a_i=0\). At every cube vertex all \(x_i^2=1/d\), hence \(P\) vanishes identically. This proves the missing top-character line at \(\ell=d+2\) and completes the classification.

**5. Rank and saturation.** Since the Walsh lines are mutually orthogonal and each line has dimension one, the rank is the sum of their binomial multiplicities. The parity half of the Boolean cube has dimension \(2^{d-1}\). For \(\ell=d-1,d,d+1\) the permitted levels exhaust one parity half without either exception; at \(d+2\), exactly the top line is lost.

## Verification
The standalone file `check_hypercube_harmonic.py` performs exact-rational calculations, using the zonal Gegenbauer kernel \(C_\ell^{(d-2)/2}(\varepsilon\cdot\eta/d)\). By the spherical-harmonic addition theorem this is a positive scalar multiple of the degree-\(\ell\) evaluation Gram kernel, so the nonzero Walsh eigenvalues and the image of the evaluation map have identical character support. The checker evaluates every Walsh eigenvalue in dimensions \(d=6,7,8,9,10\) and every degree \(0\le\ell\le d+2\), totaling 505 eigenvalue tests. It confirms the exact predicted zero sets, positivity of all nonzero eigenvalues, and the rank formula; it also checks the critical Legendre value \(P_6(1/\sqrt3)=2/9\). These finite checks corroborate, but do not replace, the unrestricted constructive proof.

## Relationship to prior work
Classical theory of spherical codes, designs, and spherical harmonics supplies the harmonic decomposition and addition theorem; the binary sign cube is a familiar spherical \(3\)-design. Delsarte, Goethals and Seidel established the spherical design framework. Lloyd studied Hamming association schemes and their spherical analogues, including Gegenbauer/Krawtchouk connections. Roy and Suda analyze complex spherical designs and associated harmonic kernels, while Bezubik and Strasburger review canonical harmonic decompositions. The present statement instead classifies the **exact Walsh characters in the restriction image of each real spherical-harmonic degree** at the Euclidean sign cube, with the non-monotone \(d+2\) blind spot and an explicit spanning construction. This is not a claim that the addition theorem, Boolean Fourier basis, or general design framework is new. A possible implicit older equivalent in Hamming or spherical association-scheme literature remains a limitation.

## Limitations
The stated closed rank classification is limited to \(d\ge6\) and degrees through \(d+2\). It gives rank, not singular-value magnitudes or stable inversion bounds. It is a mathematical result supported by a direct proof and finite exact checks, not an independently certified theorem; the oldest relevant foundational papers were not all accessible in full for novelty comparison. It does not assert historical priority beyond the checked literature.

## References
1. A. Roy and S. Suda, *Complex spherical designs and codes*, arXiv:1104.4692v1, posted 2011-04-25, especially Sections 1–3 on harmonic kernels and addition theorems. https://arxiv.org/html/1104.4692v1
2. P. Delsarte, J. M. Goethals and J. J. Seidel, *Spherical codes and designs*, Geometriae Dedicata 6 (1977), 363–388, DOI:10.1007/BF03187604.
3. S. P. Lloyd, *Hamming Association Schemes and Codes on Spheres*, SIAM Journal on Mathematical Analysis 11 (1980), 488–505, DOI:10.1137/0511047.
4. A. Bezubik and A. Strasburger, *Canonical decomposition of the harmonic polynomials and Fourier transforms of SO(d)-finite measures*, publicly posted lecture slides, https://quantum.physics.sk/conf/tatry07/talks/bezubik.pdf (harmonic decomposition in slides 2–3).
