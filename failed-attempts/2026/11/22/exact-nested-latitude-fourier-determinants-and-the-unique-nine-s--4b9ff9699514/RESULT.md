# Exact nested-latitude Fourier determinants and the unique nine-sample spherical D-optimum

## Finding
For every integer \(L\ge2\), the square spherical-harmonic collocation matrix on the \(L^2\)-point **nested odd-ring grid** has an exact product determinant independent of all individual ring-longitude offsets. In particular, at \(L=3\), among **all free nonpolar latitudes** of the one-pole, three-point-ring, five-point-ring sampling family, the **unique** determinant-maximizing latitude cosines are
\[
u_* = \frac{11+\sqrt{2305}}{78},\qquad v_* = \frac{15-\sqrt{2305}}{130}.
\]
The freedom to rotate either regular polygon remains: uniqueness concerns the two ordered latitude parameters. The two rings may lie in either order; the theorem compares both orders. The optimal determinant is approximately \(1.0599900996492535\) times the determinant for the conventional equiangular placement \(\bigl(\cos(\pi/5),\cos(3\pi/5)\bigr)\). This is a determinant statement, not a claim about interpolation condition numbers or noise amplification.

More generally let \(x_0=-1\) and let \(x_1,\ldots,x_{L-1}\in(-1,1)\) be pairwise distinct, and put \(a_{\ell,m}\) as defined below. Then the full determinant satisfies the exact all-bandwidth law
\[
|\det E_L|=K_L\left(\prod_{k=1}^{L-1}(1-x_k^2)^{k(k+1)/2}\right)
 \left(\prod_{0\le i<j\le L-1}|x_j-x_i|^{2i+1}\right),
\]
where the positive constant \(K_L\) is explicit and depends only on \(L\). Each strict-ordering chamber for the latitudes has exactly one determinant maximizer.

## Assumptions and scope
Use the unit sphere \(S^2\), colatitude \(\theta\in[0,\pi]\), longitude \(\phi\in[0,2\pi)\), and the standard complex spherical harmonics \(Y_\ell^m\) normalized to be orthonormal in surface measure \(d\Omega\), not probability measure. Fix an integer bandwidth \(L\ge2\) and the \(L^2\)-dimensional space \(\mathcal H_L=\operatorname{span}\{Y_\ell^m:0\le\ell<L,-\ell\le m\le\ell\}\). On index \(k=0\), take one sample at the south pole (\(\cos\theta=-1\)). On ring index \(k\in\{1,\ldots,L-1\}\), take exactly \(2k+1\) equally spaced longitudes \(\phi_{k,j}=\beta_k+2\pi j/(2k+1)\), for all \(0\le j\le2k\), at arbitrary colatitude \(\theta_k=\arccos x_k\in(0,\pi)\). The offsets \(\beta_k\in\mathbb R\) are arbitrary. Let \(E_L\) denote the square matrix whose rows evaluate any ordered orthonormal harmonic basis at these points.

For integers \(0\le m\le\ell\), define the positive leading-coefficient magnitude
\[
a_{\ell,m}=\sqrt{\frac{2\ell+1}{4\pi}}\,
\frac{(2\ell)!}{2^\ell\ell!\sqrt{(\ell-m)!(\ell+m)!}},
\]
and define
\[
K_L=\left(\prod_{k=0}^{L-1}(2k+1)^{(2k+1)/2}\right)
\left(\prod_{\ell=0}^{L-1}a_{\ell,0}\right)
\left(\prod_{m=1}^{L-1}\prod_{\ell=m}^{L-1}a_{\ell,m}^{2}\right).
\]
The determinant modulus is invariant under any reordering of rows or columns and the standard choice of spherical harmonic phase. Distinct latitudes are essential for invertibility, not imposed as an arbitrary ordering convention.

## Proof
**1. Fourier-order separation.** A normalized discrete Fourier transform of the \(2k+1\) values on ring \(k\) has determinant modulus one and converts the ring samples into \(2k+1\) azimuthal Fourier channels, each carrying an overall row normalization factor \(\sqrt{2k+1}\). The channel for azimuthal order \(m\), \(|m|\le k\), contains its desired order-\(m\) profile and aliases from orders congruent to \(m\pmod{2k+1}\). Process harmonic orders from largest absolute value downwards. Since the higher-order profiles have already been solved using rings of larger index, elementary eliminations subtract their aliased contributions without changing the determinant. What remains is a block-triangular evaluation matrix, with one order-\(m\) block of size \(L-|m|\) acting on the rings \(k\ge|m|\). The pole contributes only to the order-zero block. This operation is exact for arbitrary offsets \(\beta_k\); these add unit-modulus factors only.

**2. Weighted Vandermonde blocks.** With the Condon--Shortley convention, the order-\(m\) harmonic equals a phase \(e^{im\phi}\), a factor \((1-x^2)^{|m|/2}\), and the \(|m|\)-th derivative of a Legendre polynomial of degree \(\ell\), normalized by \(\sqrt{(2\ell+1)/(4\pi)\,(\ell-|m|)!/(\ell+|m|)!}\). After stripping row factors, these derivative polynomials have degrees \(0,1,\ldots,L-1-|m|\) and leading coefficient magnitudes \(a_{\ell,|m|}\). Their determinant is thus a leading-coefficient product times a Vandermonde product over the ring latitudes \(x_{|m|},\ldots,x_{L-1}\). The order-zero block includes the pole \(x_0=-1\). Multiplication over all \(m\in\{-(L-1),\ldots,L-1\}\) gives exactly the stated \(K_L\), with the factors \((2k+1)^{(2k+1)/2}\). A given \((1-x_k^2)\) occurs with total exponent \(\sum_{m=1}^k m=k(k+1)/2\). A given pair \(i<j\) occurs in order zero and both orders \(\pm m\) for \(1\le m\le i\), hence the spacing exponent \(2i+1\). This proves the determinant identity, including its independence of offsets.

**3. Strict chamber concavity.** In any chamber with a fixed strict order of the \(x_k\), take the logarithm of the factorized determinant. It is a positive linear combination of \(\log(1-x_k)\), \(\log(1+x_k)\), and \(\log|x_i-x_j|\), each concave on that chamber. The positive \(\log(1-x_k^2)\) terms have strictly negative second derivative in every free variable. Thus the full log determinant is strictly concave. It tends to minus infinity at any collision or at either endpoint, including the fixed pole. Every chamber consequently has exactly one interior maximizer.

**4. Exact nine-sample optimization.** At \(L=3\), put \(u=x_1\) (the three-point ring) and \(v=x_2\) (the five-point ring). A direct substitution yields
\[
K_3=\frac{2278125}{32768\pi^{9/2}},\qquad
|\det E_3|=K_3 F(u,v),
\]
where
\[
F(u,v)=(1-u)(1+u)^2(1-v)^3(1+v)^4|u-v|^3.
\]
The interior critical equations, after multiplying by nonzero denominators within either chamber, are
\[
-6u^2+3uv+u-v+3=0,\qquad
7uv-u-10v^2+v+3=0.
\]
Eliminating \(u\) gives \(-6(v^2-1)(65v^2-15v-8)=0\). The endpoint roots \(v=\pm1\) are excluded. The only two interior candidates are
\[
(u_+,v_-) = \left(\frac{11+\sqrt{2305}}{78},\frac{15-\sqrt{2305}}{130}\right),\qquad
(u_-,v_+) = \left(\frac{11-\sqrt{2305}}{78},\frac{15+\sqrt{2305}}{130}\right).
\]
They lie in the respective chambers \(u>v\) and \(u<v\). The positive exact difference of the two chamber-maximal objective values is
\[
F(u_+,v_-)-F(u_-,v_+)=\frac{5992816136935869152}{25555087118721346875}>0.
\]
Strict chamber concavity and boundary decay therefore prove global uniqueness of the first pair. This completes the all-degree determinant theorem and the sharp degree-two D-optimal design.

## Verification
The standalone standard-library script `verify.py` computes complex collocation determinants by independent Gaussian elimination and reconstructs the predicted product for several bandwidths, random latitudes in differing orders, and independently rotated rings. It also verifies both radical critical points and their exact objective-value difference in the quadratic field \(\mathbb Q(\sqrt{2305})\), using rational arithmetic. Run `python3 verify.py`. The analytic determinant and strict-concavity arguments, not these finite evaluations, prove the universal statements. The conventional equiangular comparison uses \(u=\cos(\pi/5)\) and \(v=\cos(3\pi/5)\).

## Relationship to prior work
Khalid (2026) proves exact reconstruction and an \(O(L^3)\) transform on precisely this nested \(L^2\)-node family, and optimizes an error-amplification constant for ring placement, not the full collocation determinant. Khalid, Kennedy, and McEwen (2014) optimize sequential interpolation condition numbers for related layouts; Nafees and colleagues (2017) consider improved conditioning under order-dependent placements. Giacaglia and Lundquist (1972) use historical one/three/five spherical-geophysics samples and did not derive this exact unrestricted latitude determinant optimum in the inspected treatment. The Fourier-block identity and classical Vandermonde formula are prior techniques; the claim is their explicit all-ring determinant evaluation and the globally compared radical optimum within the specified family.

## Limitations
The problem maximizes the determinant of a square collocation matrix **only within this structured family**, not among all \(L^2\)-point sets on the sphere. Determinant maximization does not imply best condition number, smallest pointwise interpolation error, or numerical noise tolerance. The general-degree formula ensures a unique extremizer per ordering chamber, not a closed global latitude classification at arbitrary \(L\). The first public date refers to the motivating source, not to an independent publication of the present finding. Earlier equivalent formulations in optimal-design or Vandermonde literature remain a bibliographic risk. Independent mathematical audit has not been performed.

## References
- Z. Khalid, *An \(O(L^3)\) Spherical Harmonic Transform on \(L^2\) Samples*, arXiv:2611.16441, submitted 2026-11-12. https://arxiv.org/abs/2611.16441
- Z. Khalid, R. A. Kennedy, and J. D. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms*, arXiv:1403.4661, 2014. https://arxiv.org/abs/1403.4661
- W. Nafees and colleagues, *Optimal-Dimensionality Sampling on the Sphere: Improvements and Variations*, arXiv:1709.02497, 2017. https://arxiv.org/abs/1709.02497
- G. Giacaglia and C. Lundquist, *Sampling Functions for Geophysics*, NASA technical report 19730008792, 1972. https://ntrs.nasa.gov/citations/19730008792
