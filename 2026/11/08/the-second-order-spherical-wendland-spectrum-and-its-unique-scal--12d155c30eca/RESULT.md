# The second-order spherical Wendland spectrum and its unique scale cancellation

## Finding

Fix an integer \(d\ge2\), real \(\alpha>0\), \(\lambda=(d+1)/2+\alpha\), a smoothness parameter \(\mu>\lambda+2\), and a scale \(\varepsilon>0\). The degree-\(m\) spherical Fourier eigenvalue of the generalized Wendland kernel has the **two-term expansion**

\[
\widehat\psi_m=C_{d,\alpha,\mu,\varepsilon}\,\nu^{1-2\lambda}
\left[1+\frac{Q_{\lambda,\mu}(\varepsilon)}{\nu^2}
+o(\nu^{-2})\right],\qquad
\nu=m+\frac{d-2}{2},
\]

where

\[
C_{d,\alpha,\mu,\varepsilon}=
\frac{(2\pi)^{(d-1)/2}2^{\lambda-1/2}\Gamma(\lambda-1/2)\mu}
{\sqrt{2\pi}}\,\varepsilon^{2\alpha+1},
\quad
Q_{\lambda,\mu}(\varepsilon)=
\left(\lambda-\frac12\right)
\left[\frac{\lambda(\lambda-1)}3-(\mu-1)(\mu-2)\varepsilon^2\right].
\]

The relative \(\nu^{-1}\) term vanishes **identically**, for every admissible parameter set. Moreover, there is exactly one positive spatial rescaling for which the entire second-order term vanishes:

\[
\varepsilon_*=
\sqrt{\frac{\lambda(\lambda-1)}{3(\mu-1)(\mu-2)}}.
\]

For \(0<\varepsilon<\varepsilon_*\), the quadratic relative correction is strictly positive; for \(\varepsilon>\varepsilon_*\), it is strictly negative. At the unique calibrated scale the remainder is \(o(\nu^{-2})\). The leading order is known; the **explicit next coefficient, absence of a first-order correction, and unique calibration scale** are the assertions here.

## Assumptions and scope

The radial kernel, using the convention of Hubbert and Jäger, is

\[
\phi_{\mu,\alpha}^{(\varepsilon)}(r)
=\frac1{2^{\alpha-1}\Gamma(\alpha)}
\int_{\varepsilon r}^{1}t(1-t)^\mu\bigl(t^2-(\varepsilon r)^2\bigr)^{\alpha-1}\,dt,
\quad 0\le r\le\varepsilon^{-1},
\]

and zero for \(r>\varepsilon^{-1}\). The spherical kernel is \(K(x,y)=\phi_{\mu,\alpha}^{(\varepsilon)}(|x-y|)\) for \(x,y\in S^{d-1}\). Let \(d\sigma\) denote **area measure**, not probability measure. On the real or complex spherical-harmonic subspace of integer degree \(m\), the rotation-invariant integral operator \(Tf(x)=\int_{S^{d-1}}K(x,y)f(y)\,d\sigma(y)\) acts by the scalar \(\widehat\psi_m\). In dimension \(d=2\), the same definition uses the two-dimensional span of the nonconstant circle modes. No adjustment by surface area is hidden in \(\widehat\psi_m\).

All asymptotics are as the integer \(m\to\infty\) **with parameters fixed**. The assumption \(\mu>\lambda+2\) ensures that the oscillatory endpoint contribution to the Euclidean transform is smaller than its second algebraic term. It is not asserted that the displayed second term survives at the endpoint or under weaker smoothness.

## Proof

**1. Euclidean radial-transform expansion.** Set \(a=\lambda\), \(b=\lambda+\mu/2\), \(c=\lambda+(\mu+1)/2\). The unitary radial Fourier transform, in the convention of the cited primary source, is a positive fixed constant times

\[
{}_1F_2\left(a;b,c;-\frac{z^2}{4\varepsilon^2}\right).
\]

This formula is [1, (3.12)]. The algebraic part of the large-negative-argument asymptotics of \({}_1F_2\), from [3, (16.11.2), (16.11.8)], has leading term proportional to \(z^{-2a}\); its next relative term is obtained by taking the ratio of the residue at \(a+1\) to that at \(a\). That ratio equals

\[
-a(b-1-a)(c-1-a)\frac{4\varepsilon^2}{z^2}
=-\frac{\lambda(\mu-1)(\mu-2)\varepsilon^2}{z^2}.
\]

The oscillatory part is \(O(z^{-\lambda-\mu})\), as follows from the two exponential asymptotic branches in [3] or [1, (3.16)]. Since \(\mu>\lambda+2\), this is \(o(z^{-2\lambda-2})\). Thus the full radial transform satisfies

\[
\widehat\phi(z)=A z^{-2\lambda}
\left[1-\lambda(\mu-1)(\mu-2)\varepsilon^2z^{-2}
+o(z^{-2})\right],
\qquad
A=\frac{2^\lambda\Gamma(\lambda)\mu}{\sqrt{2\pi}}
\varepsilon^{2\alpha+1}.
\tag{1}
\]

The leading constant is also [1, (3.17)]. Notice that the factor \(4\varepsilon^2\) from the hypergeometric argument has been included; omitting it changes the calibration scale.

**2. Transfer to the sphere.** For \(\nu=m+(d-2)/2\), the radial-to-spherical identity of [1, (2.10)] and [2] is

\[
\widehat\psi_m=(2\pi)^{d/2}
\int_0^\infty z\widehat\phi(z)J_\nu(z)^2\,dz.
\tag{2}
\]

For every fixed \(\rho>1/2\), and all sufficiently large \(\nu\), the Bessel-square Mellin integral [4, (10.22.57)] is

\[
M_\nu(\rho):=\int_0^\infty z^{1-2\rho}J_\nu(z)^2\,dz
=\frac{\Gamma(\rho-1/2)\Gamma(\nu+1-\rho)}
{2\sqrt\pi\,\Gamma(\rho)\Gamma(\nu+\rho)}.
\tag{3}
\]

To justify using (1) inside (2) despite the variable Bessel order, split at \(z=\nu/2\). On \(0<z\le\nu/2\), the defining Bessel series yields

\[
|J_\nu(z)|\le
\frac{(z/2)^\nu}{\Gamma(\nu+1)}
\exp\!\left(\frac{z^2}{4(\nu+1)}\right).
\tag{4}
\]

Stirling's formula consequently gives \(|J_\nu(z)|\le C\nu^{-1/2}q^\nu\) throughout this interval, for a fixed \(q<1\) (for example any \(q>e^{17/16}/4\)). The boundedness of \(\widehat\phi\) and the corresponding weighted-integral estimates show that each low-frequency piece of (2), and of the two Mellin integrals in (3), is exponentially smaller than \(\nu^{1-2\lambda-2}\).

For \(z\ge\nu/2\), the remainder in (1) is uniformly \(o(z^{-2})\) relative to \(A z^{-2\lambda}\). Since \(z^{-2}\le4\nu^{-2}\), positivity of \(J_\nu(z)^2\) and (3) show that its integrated contribution is \(o(\nu^{-2}M_\nu(\lambda))\). Therefore

\[
\widehat\psi_m=(2\pi)^{d/2}A
\left[M_\nu(\lambda)
-\lambda(\mu-1)(\mu-2)\varepsilon^2M_\nu(\lambda+1)
+o(\nu^{-2}M_\nu(\lambda))\right].
\tag{5}
\]

**3. Exactly two spectral orders.** From (3), without approximation,

\[
\frac{M_\nu(\lambda+1)}{M_\nu(\lambda)}
=\frac{\lambda-1/2}{\lambda(\nu-\lambda)(\nu+\lambda)}.
\tag{6}
\]

The gamma ratio also has the asymptotic expansion

\[
\frac{\Gamma(\nu+1-\lambda)}{\Gamma(\nu+\lambda)}
=\nu^{1-2\lambda}
\left[1+\frac{\lambda(\lambda-1)(\lambda-1/2)}{3\nu^2}
+O(\nu^{-4})\right].
\tag{7}
\]

Its relative \(\nu^{-1}\) term is zero because the two gamma shifts add to one. Formula (7) follows by inserting the Bernoulli-polynomial expansion of \(\log\Gamma\); equivalently, its quadratic coefficient is \(B_3(\lambda)/3\), where \(B_3(u)=u(u-1)(u-1/2)\).

Substitute (6) and (7) into (5). The leading factor \((2\pi)^{d/2}A\Gamma(\lambda-1/2)/(2\sqrt\pi\Gamma(\lambda))\) equals the stated \(C_{d,\alpha,\mu,\varepsilon}\), by elementary powers-of-two simplification. The quadratic factor is exactly \(Q_{\lambda,\mu}(\varepsilon)\). This proves the expansion and the absence of a linear-order correction.

**4. Calibration and uniqueness.** Since \(d\ge2\), \(\alpha>0\) imply \(\lambda>1\), and \(\mu>\lambda+2\) implies \(\mu>2\), the factors \(\lambda-1/2\), \(\lambda(\lambda-1)\), and \((\mu-1)(\mu-2)\) are strictly positive. Thus \(Q\) is strictly decreasing as a function of \(\varepsilon^2>0\) and has exactly the one positive zero displayed in the finding. The sign and calibrated remainder assertions follow.

## Verification

The standalone `tools/check_wendland.py` reproduces independently: (i) the first two coefficients in the large-argument hypergeometric transform for two parameter sets; (ii) Bessel Mellin integrals from direct numerical integration and their gamma representations; (iii) the quadratic gamma-ratio coefficient; and (iv) direct spherical Fourier integration for the completely explicit case \(d=2\), \(\alpha=1\), \(\mu=6\). In this example \(\lambda=5/2\), and the predicted relative correction is \(5/2-40\varepsilon^2\). At \(\varepsilon=1/2\) this equals \(-15/2\); at the calibrated \(\varepsilon_*=1/4\) it equals zero. The code checks both signs and the improved error trend at the latter value. The script uses Python and `mpmath`; it prints `WENDLAND_SECOND_ORDER_CHECKS_PASS` on success.

These numerical checks are finite and are **not** proofs of the arbitrary-degree asymptotic or the uniqueness assertion; those follow from (1)–(7).

## Relationship to prior work

Hubbert and Jäger [1] give the exact generalized Wendland Euclidean transform, the radial-to-spherical Bessel identity and an explicit leading-order coefficient. Their initial 2021 arXiv manuscript stated the leading-order formula for every dimension (Theorem 5.9); the revised 2023 journal version proves the precise leading asymptotic for odd ambient dimensions and identifies the even-dimensional leading limit as an open question. Neither version states the present *next* spectral coefficient or the unique support-scale cancellation. The first-order result, including its constant, is **not claimed here as new**.

Narcowich, Sun and Ward [2] established the RBF-to-SBF transform connection and Sobolev-space implications. Their general transfer principles supply part of the background, but their inspected discussion does not give this Wendland-specific relative \(\nu^{-2}\) coefficient or its unique zero. The classical Bessel integral [4] and generalized-hypergeometric expansion [3] are explicit ingredients of the proof, not claimed as newly derived identities.

## Limitations

The two-term estimate is pointwise in fixed parameters and applies only for \(\mu>\lambda+2\). It does not yield an all-parameter error bound, results at \(\mu=\lambda\), higher spectral orders, or stability bounds under finite sampling. The calibration concerns asymptotic matching of the spectrum to the leading power law; it does **not** make the full finite-degree kernel spectrum exactly Sobolev or exactly tight. Historically earlier general special-function techniques may offer alternative derivations, and a complete review of all kernel-preconditioning literature has not been performed. No independent mathematical review is claimed.

## References

[1] S. Hubbert and J. Jäger, *Generalised Wendland functions for the sphere*, arXiv:2110.09835 (first publicly posted 19 October 2021), and *Advances in Computational Mathematics* **49** (2023), article 3, DOI:10.1007/s10444-022-10005-z. Relevant formulae: (2.10), (3.12), (3.17), and the first-order spherical-coefficient theorem.

[2] F. J. Narcowich, X. Sun and J. D. Ward, *Approximation power of RBFs and their associated SBFs: A connection*, *Advances in Computational Mathematics* **27** (2007), 107–124, DOI:10.1007/s10444-005-7506-1, especially the representation and Sobolev coefficient bounds.

[3] NIST Digital Library of Mathematical Functions, §16.11, equations 16.11.2 and 16.11.8, generalized hypergeometric large-variable asymptotics; https://dlmf.nist.gov/16.11.

[4] NIST Digital Library of Mathematical Functions, §10.22, equation 10.22.57, Bessel-product Mellin integral; https://dlmf.nist.gov/10.22.E57.
