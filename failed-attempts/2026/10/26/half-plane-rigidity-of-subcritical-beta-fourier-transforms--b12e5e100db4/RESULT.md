# Half-plane rigidity of subcritical beta Fourier transforms

## Finding

For every real \(0<s<2\) and \(0<a<s\), define the entire function
\[
F_{s,a}(z)={}_1F_1(a;s;z)=\frac{\Gamma(s)}{\Gamma(a)\Gamma(s-a)}\int_0^1 e^{zu}u^{a-1}(1-u)^{s-a-1}\,du.
\]
Every zero of \(F_{s,a}\) has strictly positive real part if \(a<s/2\), and strictly negative real part if \(a>s/2\). If \(a=s/2\), all zeros are simple and purely imaginary, occurring in conjugate pairs \(z=\pm 2i j_{(s-1)/2,n}\), \(n\ge1\). Thus the sign of the endpoint-shape asymmetry classifies the **entire complex zero set**, not just zeros on the Fourier axis.

## Assumptions and scope

All parameters are real with \(0<s<2\), \(0<a<s\). The Fourier transform of the beta probability measure is \(t\mapsto F_{s,a}(it)\) for real \(t\); \(z\) denotes the complex Laplace-frequency variable. The restriction \(s<2\) is essential for the relationship-to-prior-work claim: a known published half-plane theorem already covers \(s\ge2\). We make no originality claim for that range. Neither the beta density nor the classical Bessel-zero description at equality is claimed to be new.

## Proof

**1. Imaginary-axis rigidity.** Set \(\delta=a-s/2\) and \(g(t)=e^{-it/2}F_{s,a}(it)\). From Kummer's differential equation, for \(t>0\),
\[
(t^s g'(t))'+\bigl(\tfrac14t^s-i\delta t^{s-1}\bigr)g(t)=0.
\]
Multiplication by \(\overline{g}\), subtraction of the conjugate equation and integration from \(0\) give
\[
t^s\operatorname{Im}(g'(t)\overline{g(t)})=\delta\int_0^t u^{s-1}|g(u)|^2\,du.
\]
The integral is strictly positive since \(g(0)=1\). The boundary term at zero vanishes since \(s>0\) and \(g\) is analytic. If \(\delta\ne0\), a zero at any positive real \(t\) would make the left side zero, a contradiction. Complex conjugation handles negative \(t\), and \(F(0)=1\). Therefore no zero lies on the imaginary \(z\)-axis away from the symmetric case.

**2. Symmetric base and direction of departure.** For \(a=s/2\), put \(\nu=(s-1)/2>-1/2\). The classical Bessel reduction is
\[
g_0(t)=\Gamma(\nu+1)(4/t)^\nu J_\nu(t/2),
\]
with the removable value at zero. All zeros of \(g_0\) are real and simple and lie at \(\pm T_n\), \(T_n=2j_{\nu,n}\). Analytic perturbation in \(\delta\) gives, for the zero of \(F_{s,s/2+\delta}(z)\) originating at \(iT_n\),
\[
\left.\frac{dz_n}{d\delta}\right|_{\delta=0}
=-\frac{\int_0^{T_n}t^{s-1}g_0(t)^2\,dt}{T_n^s g_0'(T_n)^2}<0.
\]
This follows by differentiating the differential equation with respect to \(\delta\), multiplying the resulting inhomogeneous equation by \(g_0\), subtracting the base equation times the derivative, and integrating the boundary Wronskian. The conjugate zero has the same real derivative. Hence every *fixed* symmetric zero moves strictly left for sufficiently small positive \(\delta\), and strictly right for negative \(\delta\).

**3. High-frequency localization with parameter uniformity.** Fix \(0<d<s/2\). The Euler-integral endpoint expansions, uniform when \(|\delta|\le d\) and \(|\operatorname{Re}z|=O(\log|\operatorname{Im}z|)\), give in the upper half-plane the two dominant contributions
\[
F_{s,s/2+\delta}(z)=\frac{\Gamma(s)}{\Gamma(s/2-\delta)}(-z)^{-s/2-\delta}(1+O_{s,d}(|z|^{-1}))
+\frac{\Gamma(s)}{\Gamma(s/2+\delta)}e^z z^{-s/2+\delta}(1+O_{s,d}(|z|^{-1})).
\]
The branches are principal near the positive imaginary axis. Standard two-endpoint Rouché localization, together with one-term dominance outside the logarithmic vertical corridor, shows that *every sufficiently large zero* is on one of the upper/lower conjugate strings, with one simple zero per consecutive period. This use of the endpoint expansion does not infer an exhaustive zero census from finite computation. For the upper string, choosing the index so that its symmetric member is \(iT_n\), the real-part equation obtained by taking the logarithm of the two-term cancellation is
\[
\operatorname{Re}z_n(\delta)=-2\delta\log T_n
+\log\Gamma(s/2+\delta)-\log\Gamma(s/2-\delta)
+O_{s,d}(|\delta|\log T_n/T_n).
\]
To justify the *factor* \(|\delta|\) in the real error uniformly at the symmetric endpoint, use analyticity of the localized simple zero in \(\delta\), the uniform differentiated endpoint remainder (Cauchy estimates in a slightly larger parameter disk), and Kummer reflection \(F_{s,s/2+\delta}(z)=e^zF_{s,s/2-\delta}(-z)\). At \(\delta=0\) its real part is identically zero. The gamma-quotient term is \(O_{s,d}(|\delta|)\), so there exists \(N(s,d)\) such that, **simultaneously for every** \(0<\delta\le d\) and every high zero \(n\ge N(s,d)\), the real part is strictly negative. Reflection gives strict positivity for \(-d\le\delta<0\).

For completeness, this localization applies to the whole high-zero set: outside the logarithmic imaginary corridors, the algebraic or exponential endpoint term strictly dominates; within them the two terms have alternating, simple cancellation, and Rouché's theorem on one-period rectangles gives one zero each. The error bound and its derivative are uniform on compact \(a\)-intervals contained in \((0,s)\). These statements are for each fixed \(s\) and compact parameter interval; there is no claim of uniformity as \(a\to0\), \(a\to s\), or \(s\to0,2\).

**4. No finite wrong-half-plane exceptions.** Fix any \(d<s/2\). By Step 3, a single high-frequency cutoff works for all \(\delta\in[0,d]\). Only finitely many zero branches remain below this cutoff. Step 2 places all of them in the correct open half-plane for some common \(\varepsilon>0\) and every \(0<\delta<\varepsilon\). As \(\delta\) varies through \([\varepsilon,d]\), zeros of an entire analytic family are locally continuous as multisets, including through collisions. A finite zero cannot cross the imaginary axis by Step 1, and a wrong-half-plane zero cannot enter from infinity by the uniform high-frequency result in Step 3. Hence the number of wrong-half-plane zeros remains zero. Since \(d\) was arbitrary, every zero for \(0<\delta<s/2\) lies strictly left, and reflection gives the other direction. This completes the proof.

## Verification

The accompanying standalone program `check_halfplane.py` evaluates \(60\) numerically located complex Kummer zeros across ten subcritical parameter choices, with both asymmetry orientations and root indices \(1,2,3,5,10,20\). It verifies the predicted strict signs and small residuals using 50-digit arithmetic. A second checker `check_beta_fourier.py` verifies the exact Fourier-axis Wronskian and positive infinitesimal zero drift independently at four different total shapes. These are checks of finite instances, not substitutes for Steps 1–4.

## Relationship to prior work

Wynn (1973), Theorem 1, proves half-plane localization only on the one-parameter lines \(s=2a+1\) and \(s=2a-1\), where admissible; it does not state the complete open two-parameter subcritical strip. Boussaada, Mazanti and Niculescu (arXiv:2106.03378v2, Corollary 1, pp. 9–10) prove the half-plane theorem for \(s\ge2\) by a different Green–Hille argument and expressly discuss Wynn's additional low-parameter cases. The present result fills the remaining positive-beta parameter region \(0<s<2\) by zero-axis Wronskian rigidity combined with a **uniform** high-frequency and parameter-homotopy argument. DLMF §13.9 contains classical asymptotic zero information, but a large-zero asymptotic alone does not rule out finitely many low-frequency zeros in the opposite half-plane.

## Limitations

The conclusion is for \(0<a<s<2\), not complex parameters or sign-changing beta weights. The high-frequency cutoff in the argument depends on compact parameter ranges and is not numerically optimized. Earlier special-function treatments outside the inspected statements could contain an equivalent positive-parameter theorem; the priority comparison therefore has residual historical risk. Finite computational tests cannot establish any all-parameter assertion or publication priority.

## References

- P. Wynn, "On the zeros of certain confluent hypergeometric functions," *Proceedings of the American Mathematical Society* **40** (1973), 173–182, doi:10.1090/S0002-9939-1973-0318529-7.
- I. Boussaada, G. Mazanti, S.-I. Niculescu, "Some Remarks on the Location of Non-Asymptotic Zeros of Whittaker and Kummer Hypergeometric Functions," arXiv:2106.03378v2 (21 June 2021), Corollary 1 and proof of Proposition 4.
- NIST Digital Library of Mathematical Functions, §13.9 (Kummer zero asymptotics), https://dlmf.nist.gov/13.9.
