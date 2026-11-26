# Sharp ultraviolet positivity threshold for a quadrupole-modulated spherical Poisson kernel

## Finding
Let \(\mathbb S^2\) be the unit sphere, let \(P_n\) be the Legendre polynomial normalized by \(P_n(1)=1\), and fix \(0<r<1\). Define
\[
\mathcal P_r(u)=\frac{1-r^2}{(1-2ru+r^2)^{3/2}},\qquad
K_{r,b}(x,y)=\mathcal P_r(x\cdot y)\bigl(1+bP_2(x\cdot y)\bigr),\qquad b\in\mathbb R.
\]
**Theorem.** This continuous isotropic kernel is positive semidefinite for every finite set of points of \(\mathbb S^2\) if and only if
\[
\boxed{b\ge b_*(r):=-\frac{8r^2}{3+2r^2+3r^4}.}
\]
For **every** admissible \(b\), including \(b=b_*(r)\), it is strictly positive definite on every finite set of *pairwise distinct* sites. The sharp negative-coefficient obstruction is attained only in the infinite-harmonic-degree limit: at \(b=b_*(r)\) **every** finite-degree Legendre coefficient is strictly positive, while any \(b<b_*(r)\) makes all sufficiently high-degree coefficients negative. Consequently, for every fixed finite cutoff \(N\), there exists an inadmissible \(b\) for which **all** multipliers through degree \(N\) remain strictly positive.

The critical amplitude decreases strictly from \(0\) to \(-1\) as \(r\) increases from zero to one. At the boundary, the degree-\(n\) eigenvalue of the associated integral operator on probability-normalized spherical measure has the sharp asymptotic
\[
\boxed{\lambda_n(r,b_*(r))=\frac{3(1-r^4)}{3+2r^2+3r^4}\frac{r^n}{n}\bigl(1+O_r(n^{-1})\bigr).}
\]
In particular, critical positive definiteness creates a new factor of inverse harmonic degree compared with the unperturbed Poisson multiplier \(r^n\).

## Assumptions and scope
Here \(0<r<1\), \(b\in\mathbb R\), and all points belong to the unit **two-sphere**, with normalized area measure \(\sigma(\mathbb S^2)=1\). Positive semidefiniteness means \(\sum_{i,j=1}^N c_i\overline{c_j}K_{r,b}(x_i,x_j)\ge0\) for every positive integer \(N\), every choice of sites, and complex coefficients. Strict positive definiteness concerns nonzero coefficient vectors on pairwise distinct sites. Neither the singular limit \(r=1\), the endpoint \(r=0\), nor other sphere dimensions is included in the theorem.

## Proof
**1. Exact Legendre multipliers.** The classical spherical Poisson expansion, absolutely and uniformly convergent for \(r<1\), is
\[
\mathcal P_r(u)=\sum_{n=0}^{\infty}(2n+1)r^nP_n(u).
\]
The Legendre three-term recurrence \(uP_n(u)=\frac{n+1}{2n+1}P_{n+1}(u)+\frac n{2n+1}P_{n-1}(u)\), applied twice to \(P_2(u)=(3u^2-1)/2\), gives the following exact coefficients for every integer \(n\ge0\):
\[
R_n(t)=\frac{3n(n-1)}{2(2n-1)(2n+1)t}
+\frac{n(n+1)}{(2n-1)(2n+3)}
+\frac{3(n+1)(n+2)t}{2(2n+1)(2n+3)},\qquad t=r^2,
\]
where the first fraction is interpreted as zero at \(n=0,1\) and the middle fraction as zero at \(n=0\). (These are also the values obtained by literal substitution.) Thus
\[
K_{r,b}(x,y)=\sum_{n=0}^{\infty}(2n+1)\lambda_n(r,b)P_n(x\cdot y),
\qquad \lambda_n(r,b)=r^n\bigl(1+bR_n(r^2)\bigr).
\]
The product expansion involves only degrees \(n-2,n,n+2\), so there are no omitted cross-degree terms. Every \(R_n(t)>0\) when \(0<t<1\).

**2. The sharp monotone spectral ratio.** Direct common-denominator algebra, valid for all integers \(n\ge0\), gives
\[
R_{n+1}(t)-R_n(t)=
\frac{3(1-t)\bigl(2n^2(1+t)+n(3t+5)-2t\bigr)}{t(2n-1)(2n+1)(2n+3)(2n+5)}.
\]
For \(n\ge1\), all factors in numerator and denominator are positive. At \(n=0\), both the bracket and the factor \(2n-1\) are negative. Hence \(R_n(t)\) is **strictly increasing** in \(n\ge0\). Its limit is
\[
R_\infty(t)=\frac{3+2t+3t^2}{8t}>0.
\]
For completeness, a second exact identity quantifies strict nonattainment:
\[
R_\infty(t)-R_n(t)=
\frac{3(1-t)\bigl(8n^2(1+t)+n(6t+10)-5t-3\bigr)}{8t(2n-1)(2n+1)(2n+3)}>0.
\]
The sign follows in the same way, with the bracket positive for all \(n\ge1\) and negative for \(n=0\). Furthermore,
\[
R_\infty(t)-R_n(t)=\frac{3(1-t^2)}{8t}\frac1n+O_t(n^{-2}).
\]

**3. Complete covariance cone and finite-site strictness.** Schoenberg's characterization on \(\mathbb S^2\) states that a continuous isotropic kernel is positive semidefinite on every finite configuration exactly when all its Legendre coefficients are nonnegative. The displayed coefficient formula therefore reduces the condition to \(1+bR_n(t)\ge0\) for every \(n\ge0\). For \(b\ge0\) it is automatic. For \(b<0\) the sharp condition is \(b\ge-1/\sup_nR_n(t)=-1/R_\infty(t)\), proving the theorem. If the inequality fails, monotone convergence makes every sufficiently high-degree coefficient negative. Given any finite cutoff \(N\), choose \(b\) strictly between \(-1/R_N(t)\) and \(-1/R_\infty(t)\); then degrees at most \(N\) all have positive multipliers, while the eventually negative higher coefficients make the kernel inadmissible. At equality, however, \(1-R_n/R_\infty>0\) for **every finite** \(n\). Consequently all spherical harmonic projection coefficients are positive.

For clarity, this latter fact alone proves strict finite-site positivity. If a finite signed point measure \(\mu=\sum_i c_i\delta_{x_i}\) has zero Gram energy, positivity of every coefficient implies \(\int Y_{n,m}\,d\mu=0\) for every spherical harmonic \(Y_{n,m}\) and every degree \(n\). Finite sums of spherical harmonics are uniformly dense in continuous functions on the sphere (Stone–Weierstrass, or restrictions of polynomials), so \(\mu=0\). Pairwise distinct support then forces every \(c_i=0\). This applies to all admissible parameters, including the boundary.

**4. Scale and critical spectral law.** Writing \(t=r^2\), direct differentiation gives
\[
\frac{d}{dt}\left(-\frac{8t}{3+2t+3t^2}\right)=
-\frac{24(1-t^2)}{(3+2t+3t^2)^2}<0\quad(0<t<1).
\]
The endpoint limits are immediate. Finally the exact identity \(\lambda_n(r,b_*)=r^n(R_\infty-R_n)/R_\infty\) and the last asymptotic in Step 2 yield the stated high-degree coefficient and its strictly positive leading constant.

## Verification
Run `python3 check.py` with Python, SymPy and mpmath installed. The checker verifies the exact rational difference and gap identities symbolically, reconstructs the Legendre product decomposition in degrees zero through nineteen, compares the exact convolution with Legendre triple integrals at rational radii and many degrees, compares high-precision direct Poisson integrals with the formula, and checks rational monotonicity/nonattainment through degree 399 at four radii. Its execution produced `PASS: 3318 verified exact or numerical assertions`. The infinite claims depend on the proof's closed rational identities and the established Schoenberg theorem, **not** on truncation or numerical quadrature. No assertion of independent mathematical audit is made.

## Relationship to prior work
Jäger, *Strictly positive definite kernels on the 2-sphere: beyond radial symmetry* (arXiv:2005.02798, first public version 2020-05-06), and Buhmann–Jäger, *Strict Positive Definiteness of Convolutional and Axially Symmetric Kernels on d-Dimensional Spheres* (2022), give general spherical harmonic coefficient and strictness frameworks. Their relevant results do not calculate the complete signed degree-two Poisson covariance cone or the strict unattained spectral endpoint. Sun–Gao–Sun, *Spherical quasi-interpolation using scaled zonal kernels* (arXiv:2408.14803, first public 2024-08-27; inspected later open-access version), gives the classical unmodulated spherical Poisson expansion and studies spherical approximation, not the signed quadratic modulation.

Nearby published exact positive-type studies treat geodesic exponentials multiplied by a linear angular factor, differences of two geodesic exponential scales, and a **nonstationary circle** Poisson modulation. Those are distinct functional families and do not imply the present exact Legendre-coefficient comparison. General Schoenberg positivity is the essential background, not claimed as new; the new statement here is the sharp all-radius parameter threshold, its infinite-degree control, strictness at the unattained endpoint, and the critical spectral decay law. The source comparison is bounded, not a proof that no equivalent treatment exists.

## Limitations
The claim is restricted to the classical three-dimensional ball Poisson kernel on the unit boundary two-sphere and its *single signed quadrupolar factor*. It supplies no general characterization of arbitrary polynomial modulations, other dimensions, or nonisotropic multipliers. High-degree spectral positivity is proved analytically, but its possible earlier discovery in specialized or unindexed literature has not been excluded. The result has not undergone independent mathematical validation.

## References
1. J. Jäger, *Strictly positive definite kernels on the 2-sphere: beyond radial symmetry*, arXiv:2005.02798 (first public 2020-05-06), https://arxiv.org/abs/2005.02798.
2. M. Buhmann and J. Jäger, *Strict Positive Definiteness of Convolutional and Axially Symmetric Kernels on d-Dimensional Spheres*, Journal of Fourier Analysis and Applications 28 (2022), article 40, https://doi.org/10.1007/s00041-022-09913-x.
3. Z. Sun, W. Gao and X. Sun, *Spherical quasi-interpolation using scaled zonal kernels*, arXiv:2408.14803 (first public 2024-08-27), https://arxiv.org/abs/2408.14803.
4. I. J. Schoenberg, *Positive definite functions on spheres*, Duke Mathematical Journal 9 (1942), 96–108.
5. R. K. Beatson, W. zu Castell and Y. Xu, *A Pólya criterion for (strict) positive definiteness on the sphere*, arXiv:1110.2437 (2011), https://arxiv.org/abs/1110.2437.
