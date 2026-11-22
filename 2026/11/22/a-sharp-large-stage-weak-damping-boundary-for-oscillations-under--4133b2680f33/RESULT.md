# A sharp large-stage weak-damping boundary for oscillations under SSP-optimal third-order Runge–Kutta

## Finding
For every integer \(s\ge2\), use the uniquely SSP-optimal order-three \(s\)-stage implicit Runge–Kutta method with diagonal coefficient \(\gamma_s=(1-\sqrt{(s-1)/(s+1)})/2\), strictly lower coefficient \(\delta_s=1/\sqrt{s^2-1}\), and weights \(b_j=1/s\). Let \(R_s(z)\) be its stability function. Define
\[
F(\omega)=\frac{\omega^2}{2}+\cos\omega-1,
\qquad \eta_*(\omega)=\frac{F(\omega)}2.
\]
For every compact \(K\subset\mathbb R^2\), the **sharp weak-damping expansion** is uniform for \((\omega,\eta)\in K\):
\[
\boxed{\left|R_s\left(i\omega-\frac{\eta}{s^2}\right)\right|^2
=1+\frac{F(\omega)-2\eta}{s^2}+O_K(s^{-4}).}
\]
Consequently, for each fixed \(\omega\ne0\), \(F(\omega)>0\); undamped oscillations are amplified by a factor strictly greater than one at sufficiently many stages. Among damping strengths of the form \(\eta/s^2\), \(\eta_*(\omega)\) is the sharp leading boundary: fixed \(\eta<\eta_*\) gives expansion, fixed \(\eta>\eta_*\) gives contraction, for all sufficiently large \(s\). More precisely, for each fixed real \(\omega\), the unique real-axis crossing \(\lambda_s(\omega)\) of \(\lvert R_s(\lambda+i\omega)\rvert=1\) in a sufficiently small neighborhood of zero satisfies
\[
\boxed{\lambda_s(\omega)=-\frac{F(\omega)}{2s^2}+O_\omega(s^{-4}).}
\]
At frequency zero this local root is exactly zero. Finally, for every fixed \(T>0\), setting \(N_s=\lfloor Ts^2\rfloor\) gives the **long-horizon modal energy law**
\[
\boxed{\lim_{s\to\infty}\left|R_s\left(i\omega-\frac{\eta}{s^2}\right)\right|^{2N_s}
=\exp\!\bigl(T(F(\omega)-2\eta)\bigr).}
\]
Thus the weak-damping boundary is operationally sharp on the natural quadratic-in-stage accumulation timescale. Near zero frequency, \(F(\omega)=\omega^4/24+O(\omega^6)\), so \(\eta_*(\omega)=\omega^4/48+O(\omega^6)\).

## Assumptions and scope
All computations are in exact arithmetic. The scalar linear test equation is \(y'=\lambda y\), with the nondimensional step parameter \(z=h\lambda\); the imaginary part \(\omega\) and weak-damping parameter \(\eta\) are fixed as the integer stage count \(s\) increases. The parameters \(\omega,\eta\) may be any real numbers, with the practical damping case \(\eta\ge0\). The formula is uniform only for \((\omega,\eta)\) in a fixed compact set, not for a frequency growing with \(s\). Convergence of the long-horizon modulus refers to repeated steps for a fixed modal scalar equation, not the convergence of its oscillatory complex phase.

## Proof
**1. Exact stage transfer.** Write \(c_s=\sqrt{1-s^{-2}}\). With \(v=(I-zA)^{-1}\mathbf1\), the lower-triangular stage recurrence yields
\[
q_s(z)=\frac{1+(\delta_s-\gamma_s)z}{1-\gamma_s z},\qquad
R_s(z)=1-c_s+c_sq_s(z)^s.
\]
Indeed, the partial stage sums \(S_j=\sum_{k=1}^jv_k\) satisfy \(S_j=q_sS_{j-1}+(1-\gamma_sz)^{-1}\), whence \(S_s=(q_s^s-1)/(\delta_sz)\); substitution in \(R_s=1+zS_s/s\) proves the identity. Continuity covers \(z=0\). The same transfer identity has been established in earlier real-axis analysis; it is used here as a premise, not presented as new.

**2. Uniform analytic expansion.** Set \(\varepsilon=1/s\), and choose the positive branch \(r(\varepsilon)=\sqrt{1-\varepsilon^2}\) around zero. Algebra gives
\[
\gamma_s=\frac{\varepsilon}{1+\varepsilon+r(\varepsilon)},\quad
\delta_s-\gamma_s=\frac{\varepsilon}{1-\varepsilon+r(\varepsilon)}.
\]
The numerator parameter equals the negative of the denominator parameter at \(-\varepsilon\), so \(q_{-\varepsilon}(z)=q_\varepsilon(z)^{-1}\). The branch \(\log q_\varepsilon(z)\) that vanishes at \(\varepsilon=0\) is therefore odd in \(\varepsilon\). Taylor expansion on any fixed compact set of complex \(z\) yields
\[
\log q_\varepsilon(z)=\varepsilon z+\varepsilon^3P(z)+O_K(\varepsilon^5),\qquad
P(z)=\frac z2-\frac{z^2}4+\frac{z^3}{12}.
\]
Using \(c_s=1-\varepsilon^2/2+O(\varepsilon^4)\) and raising the transfer factor to power \(s=1/\varepsilon\), uniformly on such compacts,
\[
R_s(z)=e^z+\varepsilon^2\left[e^z\left(P(z)-\frac12\right)+\frac12\right]+O_K(\varepsilon^4).
\]
The error follows from analytic Taylor expansion around zero; the odd-parity identity excludes a third-order remainder in the one-step expansion.

**3. Oscillatory boundary layer.** Substitute \(z=i\omega-\eta\varepsilon^2\) and expand the squared modulus. The coefficient is
\[
2\operatorname{Re}\left(P(i\omega)-\frac12-\eta+\frac12e^{-i\omega}\right)
=\frac{\omega^2}{2}+\cos\omega-1-2\eta.
\]
This proves the displayed uniform expansion. Strict positivity for nonzero frequency follows from
\[
F(\omega)=2\left[\left(\frac\omega2\right)^2-\sin^2\left(\frac\omega2\right)\right]>0
\quad(\omega\ne0),
\]
since \(\lvert\sin t\rvert<\lvert t\rvert\) for \(t\ne0\). The sign assertions follow by a fixed gap from the threshold. For a fixed \(\omega\), \(\partial_\lambda\lvert R_s(\lambda+i\omega)\rvert^2\to2\) locally uniformly as \(s\to\infty\). The intermediate-value theorem and strict monotonicity give a unique crossing near zero. Expanding around the crossing and using the derivative gives \(\lambda_s=-F/(2s^2)+O_\omega(s^{-4})\).

**4. Accumulated energy.** With \(N_s=\lfloor Ts^2\rfloor\), take logarithms: \(N_s\log\lvert R_s\rvert^2 =N_s[(F-2\eta)/s^2+O(s^{-4})]\to T(F-2\eta)\). Exponentiation proves the long-horizon law. Taylor expansion of cosine gives the claimed low-frequency coefficients.

## Verification
The standalone `verify.py` recomputes each stability factor independently by triangular forward substitution and by the closed stage-transfer expression, then compares scaled amplification errors on multiple frequencies, damping strengths and stage counts. Its executed output was `VERIFY_OK 97`. All infinite-stage, local uniqueness, strict positivity and compact-uniform statements are proved above; finite calculations only test implementation and coefficients.

## Relationship to prior work
The order-three SSP-optimal tableau, including its uniqueness among implicit methods, is from Weng, Yu and Zhu (2026), Theorem 5.2, based on the earlier Ferracina–Spijker coefficient family. The published mathematical result *Exact real-axis stability frontier of SSP-optimal third-order implicit Runge–Kutta methods* has already derived the exact stage-transfer function and classified negative-real scalar decay, including its high-stage endpoint; those results are credited rather than reclaimed. Fekete and Horváth (2019) plot the four-stage stability region and embedded variants, but give no all-stage weak-damping boundary asymptotic. Gottlieb and colleagues (2026) prove a nonnegative-coefficient algebraic-stability order barrier, which does not quantify this family's near-imaginary energy drift. The new statement instead describes a complex-axis \(s^{-2}\) boundary layer, a nonpolynomial explicit wave-frequency profile and its sharp long-horizon accumulation law.

## Limitations
The theorem is an asymptotic large-stage statement for frequencies bounded independently of stage count, not an all-finite-stage characterization of the imaginary axis or the whole complex stability region. It concerns exact arithmetic and normal scalar Fourier modes; nonnormal and nonlinear evolution, solver error and spatial discretization stability require separate analysis. Earlier specialist analyses not captured by the inspected primary sources may affect historical priority. No independent mathematical audit has been performed.

## References
1. Z. Weng, H. Yu and Q. Zhu, *Phase-type representations for Strong Stability Preserving Runge–Kutta methods*, arXiv:2610.37425v1, publicly posted 2026-10-27, Theorem 5.2. https://arxiv.org/html/2610.37425v1
2. L. Ferracina and M. N. Spijker, *Strong Stability of Singly-Diagonally-Implicit Runge-Kutta Methods*, Leiden report 2007-11, 2007, §3.3. https://math.leidenuniv.nl/reports/files/2007-11.pdf
3. *Exact real-axis stability frontier of SSP-optimal third-order implicit Runge–Kutta methods*, published 2026-11-08, RESULT.md. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-real-axis-stability-frontier-of-ssp-optimal-third-order-im--60906ae1b586
4. I. Fekete and Á. Horváth, *Some Embedded Pairs for Optimal Implicit Strong Stability Preserving Runge–Kutta Methods*, 2019, §2.2 and Figure 2. https://imrefekete.web.elte.hu/files/2019_FH_ECMI.pdf
5. S. Gottlieb, Z. Grant, L. Horesh, L. Lóczi, A. Shinnar and B. Trager, *A stability order barrier and SSP bound for Runge–Kutta methods with non-negative coefficients: AI-assisted proofs*, arXiv:2611.07981v1, publicly posted 2026-11-05, §5. https://arxiv.org/html/2611.07981v1
