# Resonant persistence and sharp mode selection for two-frequency circular Poisson smoothing

## Finding

For every pair of integers \(1\le m<n\), the exact real \(L^2\)-to-\(L^4\) norm of the circle Poisson semigroup on the full two-frequency real space is given below. The sole fourth-moment resonance is \(n=3m\): it forces a nonzero higher-frequency component in **every** maximizer at **every** positive radius. For all other pairs, sufficiently strong smoothing makes the lower frequency the unique norming eigenspace.

Write \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) with normalized Haar measure, and
\[
E_{m,n}=\operatorname{span}_{\mathbb R}\{\cos(m\theta),\sin(m\theta),\cos(n\theta),\sin(n\theta)\}.
\]
Let \(P_\rho e^{ik\theta}=\rho^{|k|}e^{ik\theta}\) for \(0<\rho\le1\). Set \(\mathcal N_{m,n}(\rho)=\|P_\rho|_{E_{m,n}}\|_{L^2\to L^4}\).

**Nonresonant pairs \(n\ne3m\).** With \(u=\rho^{2(n-m)}\),
\[
\boxed{\mathcal N_{m,n}(\rho)^4=\rho^{4m}\begin{cases}
\frac32,&0<u\le\frac12,\\[2pt]
\frac{9u^2}{2(4u-1-u^2)},&\frac12<u\le1.
\end{cases}}
\]
In the first range the norming functions are exactly the nonzero lower-frequency functions. In the second range all norming functions have lower- and upper-frequency input energy fractions \(1-x_*\) and \(x_*\), respectively, where
\[
 x_* =\frac{2u-1}{4u-1-u^2}.
\]
Both phase angles are arbitrary; this specifies all equality cases up to nonzero real scaling.

**Resonant pairs \(n=3m\).** Put \(u=\rho^{2m}\), and let \(z_u\) be the unique positive root of
\[
3u^2(2-u^2)z^3+3uz^2+(3-6u^2)z-u=0.
\]
Then
\[
\boxed{\mathcal N_{m,3m}(\rho)^4=\rho^{4m}\frac{\frac32(1+u^4z_u^4)+6u^2z_u^2+2uz_u}{(1+z_u^2)^2}.}
\]
Every maximizer, and no other function, is a nonzero scalar multiple of
\[
\cos(m\theta+\alpha)+z_u\cos(3m\theta+3\alpha),\qquad \alpha\in\mathbb R.
\]
In particular \(z_u>0\) for every \(\rho>0\), and \(z_u=u/3+O(u^3)\) as \(u\downarrow0\).

The sharp contractivity radius for each pair is the unique \(\rho_*\in(0,1)\) with \(\mathcal N_{m,n}(\rho_*)=1\). In the nonresonant case set \(r_0=(2/3)^{1/(4m)}\). If \(r_0^{2(n-m)}\le1/2\), then \(\rho_*=r_0\); otherwise it is the unique root of the displayed mixed-branch norm equation. In particular the pure lower-frequency contractivity threshold becomes **independent of the upper frequency** whenever \(n\ge5m\).

In the resonant case \(\rho_*=u_*^{1/(2m)}\), where \(u_*\) is the unique real root in \((719/1000,18/25)\) of
\[
1323u^{14}-567u^{12}-2160u^{10}+1125u^8+1080u^6-972u^4+278u^2-36=0.
\]
Numerically \(u_*=0.71919586822867332955\ldots\), so \(\rho_*=0.84805416585774362290\ldots\) when \(m=1\).

## Assumptions and scope

All functions and coefficients are real-valued; each full real frequency eigenspace (both sine and cosine) is included. The Haar measure is a probability measure. The semigroup is the classical Poisson semigroup (generator \(-|D|\)), not the circle heat semigroup. There is no constant Fourier mode. Integers \(m,n\) are positive and distinct; \(\rho\in(0,1]\). At \(\rho=0\) the restricted operator is zero and all nonzero inputs trivially attain its zero norm; it is excluded from equality classification. The primary classification concerns semigroup operator norms and sharp contractivity, not the unrestricted Fourier synthesis norm.

## Proof

1. **Complete Fourier collision classification.** Write every nonzero input as
\[
f(\theta)=\sqrt2\big(a\cos(m\theta+\alpha)+b\cos(n\theta+\beta)\big),\quad a,b\ge0,
\]
so that \(\|f\|_2^2=a^2+b^2\). Orthogonality of characters gives
\[
\|P_\rho f\|_4^4=\frac32(A^4+B^4)+6A^2B^2+
\begin{cases}2A^3B\cos(3\alpha-\beta),&n=3m,\\0,&n\ne3m,\end{cases}
\]
where \(A=\rho^m a\) and \(B=\rho^n b\). Indeed, a zero sum of four signed frequencies using both positive integer magnitudes has either two occurrences of each magnitude with opposite signs, or three of the smaller against one of the larger; the latter occurs exactly when \(n=3m\). Thus the displayed identity has no missing aliases, including \(n=2m\).

2. **Nonresonant optimization.** Put \(x=b^2/(a^2+b^2)\). Divide the fourth moment by \((a^2+b^2)^2\rho^{4m}\). The result is the quadratic
\[
H_u(x)=\frac32+3(2u-1)x+\frac32(u^2-4u+1)x^2.
\]
For \(0<u\le1/2\), the inequality \(H_u(x)\le H_u(0)=3/2\) is strict for \(x>0\) (if the quadratic coefficient is positive, the maximum on the interval is at an endpoint, and \(H_u(1)=3u^2/2<3/2\); if negative, the right derivative at zero is nonpositive). For \(1/2<u\le1\), strict concavity puts its unique maximum at \(x_*\in(0,1)\). Substitution yields \(9u^2/(2(4u-1-u^2))\). Phases do not enter the fourth moment.

3. **Resonant optimization.** The phase term is maximized exactly by \(\beta\equiv3\alpha\pmod{2\pi}\) when \(a,b>0\). Writing \(z=b/a>0\), the remaining quotient is \(G_u(z)=[\frac32(1+u^4z^4)+6u^2z^2+2uz]/(1+z^2)^2\). Its derivative has the opposite sign of
\[
R_u(z)=3u^2(2-u^2)z^3+3uz^2+(3-6u^2)z-u.
\]
Read from highest to lowest power, the nonzero coefficients have exactly one sign change for every \(0<u\le1\). By Descartes' rule and \(R_u(0)<0<R_u(+\infty)\), there is exactly one positive zero. Hence \(G_u\) rises then falls, its maximum is attained at \(z_u>0\), and neither pure mode is maximizing. The implicit-function theorem at \((u,z)=(0,0)\) gives \(z_u=u/3+O(u^3)\).

4. **Sharp thresholds.** For \(0<\rho_1<\rho_2\le1\), factor \(P_{\rho_1}=P_{\rho_1/\rho_2}P_{\rho_2}\). The Poisson kernel at radius strictly between zero and one is strictly positive, so strict Jensen convexity of \(|t|^4\) shows \(\|P_{\rho_1}f\|_4<\|P_{\rho_2}f\|_4\) for every nonzero \(f\in E_{m,n}\). Compactness of the input unit sphere makes the optimal norm strictly increasing. It tends to zero with \(\rho\downarrow0\), and exceeds one at \(\rho=1\), giving one sharp threshold. In the nonresonant case its pure branch reaches one at \(r_0\), proving the branch criterion and high-frequency stabilization.

5. **Algebraic resonant threshold.** The threshold condition is \(u^2G_u(z)=1\), jointly with \(R_u(z)=0\). Eliminating \(z\) gives a nonzero constant times the product of the displayed degree-14 polynomial and \(9u^8-72u^6+162u^4-56u^2+9\). Exact Sturm calculations show that the degree-14 polynomial has one zero in \((719/1000,18/25)\). To identify the physical threshold without spurious resultant roots, apply an exact Sturm count to \((1+z^2)^2-u^2[\frac32(1+u^4z^4)+6u^2z^2+2uz]\): at \(u=719/1000\) it has no positive real zero and is positive at zero, whereas at \(u=18/25\) its value at \(z=12/25\) is negative. Continuity and the strict increase of the semigroup norm therefore place the physical threshold inside the interval, so it coincides with the unique root of the degree-14 factor there. The accompanying exact certificate is reproducible in `checker.py`.

## Verification

Run `python3 -m pip install -r requirements.txt` followed by `python3 checker.py` from the directory containing these files. The checker uses exact rational Fourier zero-sum enumeration for 828 parameter/coefficient tests, verifies the analytic stationary polynomial and resultant factorization symbolically, certifies the rational interval with exact Sturm root counts and a rational test point, and verifies the one-sign-change structure for 99 rational radii. All tests passed. The universal claims about all integer frequencies and all radii follow from the preceding exact Fourier classification, quadratic optimization, Descartes argument and strict semigroup contraction; finite checks alone would not establish them.

## Relationship to prior work

The Poisson semigroup's general circle hypercontractivity is classical (Weissler, 1980); it gives unrestricted estimates rather than these sharp restricted two-band radii. Schmidt (2013), Section 2, gives the autocorrelation identity for fourth norms but studies long unimodular polynomials and the **smallest** fourth-moment excess, not the semigroup norm on two full real eigenspaces. Ivanisvili et al. (2020), Introduction and Section 3, study \(a+bz\) under ultraspherical measures, not the pair of nonzero frequencies \(m,n\).

An earlier sharp result for four consecutive complex Fourier characters (published record in References) already supplies the \(\rho=1\) resonant fourth-moment maximum (after a unimodular frequency shift); it does **not** supply the spectral-weighted norm, its unique optimizing ratio at each radius, or the algebraic contractivity threshold. Earlier real two-tone results classify the **minimum** fourth moment at resonance, not the present semigroup's sharp **maximum**. The previously known first-plus-second spherical-band norm includes the circle specialization \((m,n)=(1,2)\); that case is not claimed new by itself. The contribution is the simultaneous all-pair sharp semigroup classification and its 1:3 persistence versus nonresonant finite-time pure-mode selection.

## Limitations

Only real-valued trigonometric inputs and fourth-moment output are covered. The formula does not address complex independently chosen Fourier coefficients, more than two frequency bands, the heat semigroup, or arbitrary probability measures. The unweighted fourth-moment resonant maximum and elementary autocorrelation identities are pre-existing, not independent novelties. The Weissler 1980 full article was not accessible in this examination; its abstract and secondary discussion were consulted, so an exact older special-case theorem cannot be ruled out categorically. No claim of independent audit or priority certification is made.

## References

1. F. B. Weissler, *Logarithmic Sobolev inequalities and hypercontractive estimates on the circle*, J. Functional Analysis 37 (1980), 218–234, DOI 10.1016/0022-1236(80)90042-7.
2. K.-U. Schmidt, *On a problem due to Littlewood concerning polynomials with unimodular coefficients*, arXiv:1302.2766v1, first posted 2013-02-12; https://arxiv.org/abs/1302.2766.
3. E. Milman, *Spectral Estimates, Contractions and Hypercontractivity*, arXiv:1508.00606v1, first posted 2015-08-03; https://arxiv.org/abs/1508.00606.
4. P. Ivanisvili, A. Lindenberger, P. F. X. Müller, and M. Schmuckenschläger, *Hyper contractivity on the unit circle for ultraspherical measures: linear case*, arXiv:2004.05567v1, first posted 2020-04-12; https://arxiv.org/abs/2004.05567.
5. *A universal four-mode fourth-moment constant and the sharp seven-point sampling threshold*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-universal-four-mode-fourth-moment-constant-and-the-sharp-seven--92de3bb230cd.
