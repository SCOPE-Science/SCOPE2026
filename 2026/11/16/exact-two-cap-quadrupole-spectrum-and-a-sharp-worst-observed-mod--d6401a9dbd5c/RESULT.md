# Exact two-cap quadrupole spectrum and a sharp worst-observed-mode transition

## Finding
Let \(S^2=\{(x,y,z)\in\mathbb R^3:x^2+y^2+z^2=1\}\), and let \(\mathcal H_2\) be the five-dimensional complex space of spherical harmonics of *exactly* degree two. For every
\[
 2^{-1/2}\le c<1,
 \qquad \Omega_c=\{(x,y,z)\in S^2:x\ge c\}\cup\{(x,y,z)\in S^2:z\ge c\},
\]
let \(K_c:\mathcal H_2\to\mathcal H_2\) be the positive self-adjoint concentration operator defined by
\[
 \langle K_cf,g\rangle_{S^2}=\int_{\Omega_c}f\overline g\,d\mu,
 \qquad d\mu=d\sigma/(4\pi).
\]
The caps are disjoint except for a measure-zero contact at the left endpoint. The *entire* spectrum is the following four polynomial branches (one branch is double):
\[
\begin{aligned}
 A(c)&=\frac{1-c}{32}(57c^4+57c^3-13c^2-13c+32),\\
 B(c)&=\frac{1-c}{32}(27c^4+27c^3-23c^2-23c+32),\\
 C(c)&=\frac{(1-c)^2}{2}(3c^3+6c^2+4c+2),\\
 D(c)&=\frac{(1-c)^2}{16}(9c^3+18c^2+17c+16).
\end{aligned}
\]
The associated eigenspaces are respectively
\[
\begin{array}{c|c|c}
\text{eigenvalue}&\text{harmonic eigenspace}&\text{dimension}\\
A&\operatorname{span}_{\mathbb C}\{x^2-z^2\}&1\\
B&\operatorname{span}_{\mathbb C}\{x^2+z^2-2y^2\}&1\\
C&\operatorname{span}_{\mathbb C}\{xz\}&1\\
D&\operatorname{span}_{\mathbb C}\{xy,yz\}&2.
\end{array}
\]
Here and below the coordinate polynomials are restricted to \(S^2\). All eigenvalues are strictly positive. For the entire aperture range, \(A(c)\) is strictly greatest, and its eigenspace is the unique optimizing line for maximal energy concentration. The *sharp lower frame bound* (least observable quadrupole energy) changes according to
\[
\lambda_{\min}(K_c)=
\begin{cases}
 B(c),&2^{-1/2}\le c<\sqrt5/3,\\
 B(c)=D(c),&c=\sqrt5/3,\\
 D(c),&\sqrt5/3<c<1.
\end{cases}
\]
At the transition \(c=\sqrt5/3\), the least-eigenvalue eigenspace is three-dimensional, the direct sum of the \(B\)- and \(D\)-eigenspaces. Below it the least observable eigenspace is one-dimensional; above it the least observable eigenspace is two-dimensional. A second crossing, \(B(c)=C(c)\), occurs *exactly* at \(c=\sqrt{11/15}\); it changes the middle spectral order but not either sharp endpoint bound.

The complete strict spectral ordering between crossings is
\[
\begin{array}{c|l}
2^{-1/2}\le c<\sqrt5/3&A>C>D>B\\
\sqrt5/3<c<\sqrt{11/15}&A>C>B>D\\
\sqrt{11/15}<c<1&A>B>C>D.
\end{array}
\]
At the two endpoints of these intervals use the indicated eigenvalue equalities; there are no other coincidences. Consequently, the exact spectral condition number of the regional observation Gram operator is
\[
 \kappa_{\mathrm{Gram}}(c)=\frac{A(c)}{\min\{B(c),D(c)\}},
 \qquad \kappa_{\mathrm{Gram}}(c)\sim\frac1{1-c}\quad(c\uparrow1).
\]
These are equalities, not bounds or numerical conjectures.

## Assumptions and scope
The measure \(\mu\) is normalized to mass one on the entire sphere, and concentration is the ratio of observed to global squared \(L^2\)-energy. Only the pure degree-two harmonic eigenspace is used; neither the constant nor degree-one terms are included. The two cap centers are exactly perpendicular, their angular radii are equal, and \(c\) is in the stated non-overlapping range. All statements hold for complex coefficients; the real polynomial eigenspaces extend by complex linearity. The restriction operator \(R_c:\mathcal H_2\to L^2(\Omega_c,d\mu)\) satisfies \(R_c^*R_c=K_c\), so the eigenvalues are its squared singular values.

## Proof
Set
\[
 q_A=x^2-z^2,\quad q_B=x^2+z^2-2y^2,\quad q_C=xz,
 \quad q_{D,1}=xy,\quad q_{D,2}=yz.
\]
Each polynomial is homogeneous harmonic of degree two in \(\mathbb R^3\), and their restrictions span \(\mathcal H_2\). Their full-sphere squared norms, with the prescribed normalized surface measure, are respectively
\[
 \frac4{15},\qquad\frac45,\qquad\frac1{15},\qquad\frac1{15},\qquad\frac1{15}.
\]
They are pairwise orthogonal globally. They are also pairwise orthogonal after restriction to \(\Omega_c\). To see the latter, consider integrals separately over the north-\(z\) cap and the east-\(x\) cap. Each cap is invariant under sign reversal of either transverse coordinate; all off-diagonal products have an odd transverse factor on each cap except \(q_Aq_B\), whose two cap integrals cancel because exchanging \(x\) and \(z\) fixes \(q_B\) but negates \(q_A\). This proves the five displayed eigenspaces are invariant and diagonalizes \(K_c\) without presupposing its eigenvalues.

For an independent exact calculation of their eigenvalues, put \(z=t\), \(x=\sqrt{1-t^2}\cos\phi\), and \(y=\sqrt{1-t^2}\sin\phi\) on the north cap. For nonnegative integers \(r,s,d\), its normalized monomial integral is
\[
 \int_{z\ge c}x^{2r}y^{2s}z^d\,d\mu
 =\frac{(2r)!(2s)!}{2\,4^{r+s}r!s!(r+s)!}
 \int_c^1 t^d(1-t^2)^{r+s}\,dt.
\]
A monomial odd in either transverse coordinate integrates to zero. The corresponding integral on the east cap is obtained by exchanging \(x\) and \(z\). Since the caps have disjoint interiors, their integrals add. Apply this identity to the five squares \(|q_A|^2,|q_B|^2,|q_C|^2,|q_{D,1}|^2,|q_{D,2}|^2\), and divide by the five global squared norms above. Expanding the resulting finite integrals gives exactly the four displayed polynomials \(A,B,C,D\), including the repetition of \(D\). No approximation enters this step.

The complete ordering follows from six explicit factorizations:
\[
\begin{aligned}
 A-B&=\frac{5c(1-c)(1+c)(3c^2+1)}{16},\\
 A-C&=\frac{15c(1-c)(1+c)(7c^2-3)}{32},\\
 A-D&=\frac{15c(1-c)(1+c)(5c^2-1)}{32},\\
 B-C&=\frac{5c(1-c)(1+c)(15c^2-11)}{32},\\
 B-D&=\frac{5c(1-c)(1+c)(9c^2-5)}{32},\\
 C-D&=\frac{15c(1-c)^2(1+c)^2}{16}.
\end{aligned}
\]
All common factors not involving the indicated quadratic expressions are strictly positive on \([2^{-1/2},1)\). Moreover, \(7c^2-3>0\) and \(5c^2-1>0\) throughout the domain. Therefore \(A\) is strictly largest, \(C>D\) always, and the only crossings are precisely \(B=D\) at \(c=\sqrt5/3\) and \(B=C\) at \(c=\sqrt{11/15}\). This proves all multiplicity, extremizer, and complete-order claims. Strict positivity of each eigenvalue also follows independently because a nonzero spherical harmonic cannot vanish on either open cap.

Finally, direct addition verifies the trace identity
\[
 A+B+C+2D=5(1-c),
\]
consistent with the constant degree-two reproducing-kernel diagonal and total observed area \(\mu(\Omega_c)=1-c\). For \(\varepsilon=1-c\downarrow0\), the explicit polynomials give \(A=\tfrac{15}{4}\varepsilon+O(\varepsilon^2)\) and \(D=\tfrac{15}{4}\varepsilon^2+O(\varepsilon^3)\); the minimum is \(D\) near \(c=1\). Their quotient establishes the stated sharp asymptotic condition number.

## Verification
Run `python verify.py` in the same directory using Python with SymPy and NumPy. The script symbolically reconstructs every entry of the five-by-five cap concentration and whole-sphere Gram matrices from monomial integration, confirms all off-diagonal zeros, all four eigenvalue polynomials, all six pairwise difference factorizations, and the trace identity. It separately computes the full Gram spectrum using two-dimensional spherical-cap quadrature at seven radii, including both transition values, and compares it with the exact formulas. Successful execution prints `ORTHOGONAL_DUAL_CAP_QUADRUPOLE_PASS exact_gram=25 branch_differences=6 quadrature_radii=7 transitions=5/9,11/15`. The symbolic finite identities establish the elementary integral calculations; quadrature is a corroborating check only. The analytic factorization argument, not finite sampling, proves the all-aperture ordering.

## Relationship to prior work
The concentration-operator framework for arbitrary spherical regions is classical, particularly Simons, Dahlen and Wieczorek (2006), and the exact harmonic Gram-matrix construction and arbitrary-region computation are explicitly developed by Bates, Khalid and Kennedy (arXiv:1608.05479, initially posted in 2016). Aslam and Khalid (arXiv:2010.07266, initially posted 2020-10-14) develop spherical Slepian transforms and explain the regional concentration problem; Michel, Plattner and Seibert (arXiv:2103.14650) treat single-cap commuting operators and tensorial variants. Rogers, Beggan and Whaler (2019) apply Slepian techniques to geophysical regions including two *antipodal* polar caps. These prior works supply general methods and motivation, not an explicit classification of the pure degree-two spectrum for two *perpendicular, non-antipodal* caps. The present contribution is the evaluated exact spectrum, both exact crossing thresholds, and the strict sharp extremizer and inverse-stability classifications. No claim is made to have introduced the Slepian framework or the general region Gram method.

## Limitations
The conclusion is not asserted for other cap-center angles, unequal apertures, overlapping caps, antipodal configurations, mixed-degree bandlimits, or vector/tensor-valued harmonics. The spectral condition number is that of the exact regional *Gram operator*; the condition number of the observation map itself is its square root. Priority is subject to possible specialist calculations outside the inspected literature; only the specified spectrum and transitions, not general concentration methods, are proposed as new.

## References
1. F. J. Simons, F. A. Dahlen, M. A. Wieczorek, *Spatiospectral concentration on a sphere*, SIAM Review **48** (2006), 504–536, DOI:10.1137/S0036144504445765.
2. A. P. Bates, Z. Khalid, R. A. Kennedy, *Efficient Computation of Slepian Functions for Arbitrary Regions on the Sphere*, IEEE Transactions on Signal Processing **65** (2017), 4379–4393; arXiv:1608.05479 (first version 2016-08-19).
3. A. Aslam, Z. Khalid, *Spatial-Slepian Transform on the Sphere*, arXiv:2010.07266 (first version 2020-10-14).
4. V. Michel, A. Plattner, K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650 (first version 2021-03-26).
5. H. F. Rogers, C. D. Beggan, K. A. Whaler, *Investigation of regional variation in core flow models using spherical Slepian functions*, Earth, Planets and Space **71** (2019), 19, DOI:10.1186/s40623-019-0997-7.
