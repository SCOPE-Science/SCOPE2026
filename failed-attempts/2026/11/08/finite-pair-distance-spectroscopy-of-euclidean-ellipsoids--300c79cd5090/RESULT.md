# Finite pair-distance spectroscopy of Euclidean ellipsoids

## Finding
Let \(d\ge2\) be an integer and \(E\subset\mathbb R^d\) any solid nondegenerate Euclidean ellipsoid. The first \(d\) even moments of the Euclidean distance between two independent volume-uniform points of \(E\) determine its unordered positive semiaxis lengths. The number \(d\) is minimal as a uniform recovery cutoff and generically necessary at distinct-axis ellipsoids. If the volume is known, precisely \(d-1\) moments suffice, with the same generic sharpness.

Write \(M_k=\mathbb E\|X-Y\|^{2k}\), \(\lambda_i=a_i^2>0\), and \(v_j=\pi^{j/2}/\Gamma(1+j/2)\). Define the explicit, positive calibration
\[
c_{d,k}=\frac{d\,2^{d+2k}v_{d-1}}{(d+2k)v_d}\, B\left(\frac{d+2k+1}{2},\frac{d+1}{2}\right),\quad k\ge1.
\]
The polynomial consisting of the first \(d+1\) Taylor coefficients of
\[
\left[1+\sum_{k=1}^d\frac{(d/2)_k}{k!}\frac{M_k}{c_{d,k}}t^k\right]^{-2}
\]
is exactly \(\prod_{i=1}^d(1-\lambda_i t)\). Here \((z)_k=z(z+1)\cdots(z+k-1)\) and \(B\) is Euler's beta function.

Every solid ellipsoid also satisfies the sharp interval
\[
\frac{(d+2)(d+3)}{d(d+4)}\le\frac{M_2}{M_1^2}<\frac{3(d+3)}{d+4}.
\]
The lower equality characterizes Euclidean balls. Every intermediate value occurs for nondegenerate ellipsoids, whereas the upper endpoint is approached only through axis degeneration at fixed \(M_1\). For \(d=2\), the area \(A\) is reconstructed directly from only the second and fourth distance moments:
\[
A^2=\pi^2\left(3M_1^2-\frac65 M_2\right).
\]

## Assumptions and scope
Sampling is independent and uniform relative to \(d\)-dimensional volume in the *solid* ellipsoid, not its surface. Distances are ordinary ambient Euclidean distances, and the ellipsoid's dimension \(d\) is known. Positive semiaxes may repeat; uniqueness holds even in that case, while lower-bound sharpness is proved locally at simple spectra. The moments are exact population quantities. Translation and orthogonal orientation are unidentifiable because they preserve all pair distances.

## Proof
**1. Isotropic reduction.** Translation and orthogonal change of coordinates reduce the ellipsoid to \(E=\{(a_1u_1,\ldots,a_du_d):\|u\|_2\le1\}\). For independent volume-uniform \(U,V\) in the unit ball, \(W=U-V\) has a radial law. Consequently \(W=RS\), where \(R\ge0\) is independent of the uniform direction \(S\in S^{d-1}\). Thus
\[
M_k=\mathbb E R^{2k}\;\mathbb E\left(\sum_{i=1}^d\lambda_i S_i^2\right)^k.
\]

**2. Exact radial calibration.** For the unit ball \(B_d\), the covariogram formula gives the density of \(W\) at a vector of norm \(r\le2\) as \(\operatorname{vol}_d(B_d\cap(B_d+re_1))/v_d^2\). The intersection volume is
\[
2v_{d-1}\int_{r/2}^1(1-z^2)^{(d-1)/2}\,dz.
\]
Integrating in polar coordinates and changing order of integration shows
\[
\mathbb E R^{2k}=\frac{d\,2^{d+2k}v_{d-1}}{(d+2k)v_d}B\left(\frac{d+2k+1}{2},\frac{d+1}{2}\right)=c_{d,k}.
\]
In particular \(c_{d,1}=2d/(d+2)\) and \(c_{d,2}=4d(d+3)/((d+2)(d+4))\).

**3. Recover the entire quadratic spectrum.** The vector \((S_1^2,\ldots,S_d^2)\) is Dirichlet with all parameters \(1/2\). Its multinomial moments give, as an identity of formal power series,
\[
\sum_{k\ge0}\frac{(d/2)_k}{k!}\mathbb E\left(\sum_i\lambda_iS_i^2\right)^k t^k
=\prod_{i=1}^d(1-\lambda_i t)^{-1/2}.
\]
Substitution of the calibrated observed moments makes its first \(d\) coefficients known. Raising the series to power \(-2\) extracts all coefficients of the degree-\(d\) polynomial \(\prod_i(1-\lambda_i t)\). Its positive roots after the reciprocal variable change give the \(\lambda_i\) with multiplicities. This is an exact finite reconstruction, not an infinite-moment determinacy claim.

**4. Sharp measurement count.** Put \(p_k=\sum_i\lambda_i^k\). Taking the logarithm of the generating function shows that the first \(r\) distance moments and the first \(r\) power sums mutually determine one another by invertible triangular polynomial transformations. At distinct positive \(\lambda_i\), the Jacobian of \((p_1,\ldots,p_r)\) has rows \((k\lambda_i^{k-1})_i\) and rank \(r\) for \(r<d\). The implicit-function theorem supplies local positive-dimensional fibers of noncongruent ellipsoids for any \(r<d\). Knowing the volume specifies \(e_d=\prod_i\lambda_i=(\operatorname{vol}_d(E)/v_d)^2\), the missing final coefficient. Hence \(d-1\) observed moments determine the polynomial. For \(r\le d-2\), append the known product to the \(r\) power sums; its Jacobian has rank \(r+1\) at a simple spectrum: a dependence would give a polynomial of degree at most \(r+1<d\) vanishing at all \(d\) distinct \(\lambda_i\), with a nonzero constant. Thus the volume-assisted cutoff is generically sharp.

**5. Exact two-moment range.** With \(p_1=\sum_i\lambda_i\), \(p_2=\sum_i\lambda_i^2\), spherical second moments give
\[
M_1=\frac{2p_1}{d+2},\qquad
M_2=\frac{4(d+3)(p_1^2+2p_2)}{(d+2)^2(d+4)}.
\]
Since \(p_1^2/d\le p_2<p_1^2\) for positive \(\lambda_i\), the displayed sharp range follows. Its lower endpoint holds only when all \(\lambda_i\) coincide. For \(0\le s<1\), the family \(\lambda_1=1+(d-1)s\), \(\lambda_2=\cdots=\lambda_d=1-s\) realizes every ratio between the endpoints continuously, with the supremum at \(s\uparrow1\). For \(d=2\), substituting \(p_1=2M_1\) and \(p_2=p_1^2-2\lambda_1\lambda_2\) gives \(\lambda_1\lambda_2=3M_1^2-6M_2/5\), and the area identity follows.

## Verification
`check_ellipsoid.py` performs exact symbolic beta-normalization checks and polynomial reconstruction for nondegenerate spectra in dimensions 2, 3, 4 and 5. It also independently samples 90,000 pairs in each of dimensions 2, 3 and 5, comparing directly observed moments with the polynomial formulas. Exact identities, unlike simulations, establish the algebraic part. The analytical derivation proves the all-dimensional statement, while finite tests are corroborative only.

## Relationship to prior work
García-Pelayo's 2005 article concerns the full distance distribution for a spheroid; Parry and Fischbach (2000) investigated distance distributions and eccentricity expansions for ellipsoids. García-Pelayo (2011) described general moment polynomials for distance laws, a key antecedent for forward calculations. Arias-de-Reyna, Ball and Villa (1998) derived the unit-ball pair-distance covariogram and studied concentration, which provides an independent check on the radial ingredient. Lellouche and Souris (2019 online) treated distance distributions through convolution for standard compact bodies. The claim here is **not** a new full distance density or a new general Dirichlet identity: it is the explicit sharp finite inverse cutoff and feasibility statement for solid ellipsoids under the pair-distance experiment. A separate published inverse theorem reconstructs semiaxes from Haar central-section volumes using a different observable; it does not evaluate or invert the present pair-distance moments.

## Limitations
The result reconstructs unordered semiaxes only; it does not recover translation or orientation, nor prove statistical stability for noisy empirical moments. Distinct-axis hypotheses are needed only for the generic necessity argument, not for reconstruction. Full-text priority comparisons with Parry–Fischbach (2000) and García-Pelayo (2011) were unavailable, so an earlier equivalent inverse formulation cannot be categorically excluded. The focal source's exact publication day is documented for García-Pelayo (2005); the earlier Parry–Fischbach article has month-level (April 2000) bibliographic evidence without a verified public day.

## References
1. R. García-Pelayo, *Distribution of distance in the spheroid*, J. Phys. A 38 (2005), 3475–3482, DOI: 10.1088/0305-4470/38/16/001 (published April 6, 2005).
2. M. Parry and E. Fischbach, *Probability distribution of distance in a uniform ellipsoid: Theory and applications to physics*, J. Math. Phys. 41 (2000), 2417–2433, DOI: 10.1063/1.533249 (April 2000; exact day not verified).
3. R. García-Pelayo, *Moments of the distribution of distance*, J. Math. Phys. 52 (2011), 033505, DOI: 10.1063/1.3559719; see also its 2013 erratum, DOI: 10.1063/1.4820790.
4. J. Arias-de-Reyna, K. Ball and R. Villa, *Concentration of the distance in finite dimensional normed spaces*, Mathematika 45 (1998), 245–252, DOI: 10.1112/S0025579300014182, accessible manuscript https://discovery.ucl.ac.uk/id/eprint/82460/1/download1.pdf.
5. S. Lellouche and M. Souris, *Distribution of Distances between Elements in a Compact Set*, Stats 3 (2020), 1–15 (online December 26, 2019), DOI: 10.3390/stats3010001.
