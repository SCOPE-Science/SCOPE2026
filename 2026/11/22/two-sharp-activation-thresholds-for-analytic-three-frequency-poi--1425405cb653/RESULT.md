# Two sharp activation thresholds for analytic three-frequency Poisson fourth moments

## Finding
On the circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) with normalized Haar measure, put
\[
V_{m,n}=\operatorname{span}_{\mathbb C}\{1,e^{imt},e^{int}\},\qquad 1\le m<n,
\]
and let \(P_\rho e^{ikt}=\rho^{|k|}e^{ikt}\) for \(0<\rho\le1\). Define the **fourth power** of its restricted sharp norm by
\[
\mathcal C_{m,n}(\rho)=\max_{0\ne f\in V_{m,n}}\frac{\|P_\rho f\|_4^4}{\|f\|_2^4}.
\]
Write \(a=\rho^{2m}\), \(b=\rho^{2n}\), and \(b_*(a)=3a/[2(1+a)]\).

**Non-arithmetic frequencies \(n\ne2m\).** There are exactly three optimizing regimes:
\[
\boxed{\mathcal C_{m,n}(\rho)=
\begin{cases}
1,&a\le\frac12,\\[3pt]
1+\dfrac{(2a-1)^2}{4a-1-a^2},&a>\frac12,\quad b\le b_*(a),\\[6pt]
\dfrac5{2H^2-5J},&a>\frac12,\quad b>b_*(a),
\end{cases}}
\]
where \(H=1+a^{-1}+b^{-1}\) and \(J=1+a^{-2}+b^{-2}\). The unique optimizing **squared-modulus profile** \((x_0,x_1,x_2)=(|c_0|^2,|c_m|^2,|c_n|^2)/\|f\|_2^2\) is respectively
\[
(1,0,0),\qquad (1-s,s,0),\quad s=\frac{2a-1}{4a-1-a^2},
\]
or, in the third regime,
\[
\boxed{x_j=\frac{2H/w_j-5/w_j^2}{2H^2-5J},\quad (w_0,w_1,w_2)=(1,a,b).}
\]
All coefficient phases are unrestricted. The first threshold is \(\rho_1=2^{-1/(2m)}\); the strictly later second threshold is the unique \(\rho_2\in(\rho_1,1)\) solving
\[
\boxed{\rho_2^{2(n-m)}(1+\rho_2^{2m})=\frac32.}
\]
Thus the higher frequency remains **exactly absent** from every optimizer over the nonempty interval \(\rho_1<\rho\le\rho_2\).

**Arithmetic-resonant frequencies \(n=2m\).** The constant function is the unique optimizing direction for \(a\le1/2\), but **all three coefficients are nonzero** in every optimizer for every \(a>1/2\). Their phases necessarily obey
\[
\arg c_0+\arg c_{2m}\equiv2\arg c_m\pmod{2\pi}.
\]
At the critical onset \(a=1/2+\delta\), \(\delta\downarrow0\), the squared-modulus fractions are uniquely determined (apart from the phase symmetries) and satisfy
\[
\boxed{x_m=4\delta+O(\delta^2),\quad x_{2m}=4\delta^2+O(\delta^3),\quad \mathcal C_{m,2m}=1+8\delta^2+O(\delta^3).}
\]
For comparison, a nonresonant pair of the same lower frequency has \(\mathcal C=1+\frac{16}{3}\delta^2+O(\delta^3)\) directly above the first threshold. The resonance therefore raises the leading fourth-power excess by a factor \(3/2\), and removes the higher-mode-free interval completely.

## Assumptions and scope
All three characters have **complex and independently variable coefficients**, including the constant mode. Their input norm is \(\|c_0+c_me^{imt}+c_ne^{int}\|_2^2=|c_0|^2+|c_m|^2+|c_n|^2\). The output uses the normalized-circle \(L^4\) norm, not \(L^4\) of the coefficient vector. This is the classical Poisson semigroup and applies to every pair of distinct positive integer frequencies. At equality in either nonresonant threshold, the stated modulus profile is still unique. The resonant claim gives exact activation and sharp near-threshold asymptotics, **not** a closed all-radius norm formula or global uniqueness of resonant amplitudes away from the threshold.

## Proof

**1. Fourier square and the only collision.** Normalize \(\sum_j|c_j|^2=1\) and set \(u_0=c_0\), \(u_1=\rho^m c_m\), \(u_2=\rho^n c_n\). By Parseval, \(\|P_\rho f\|_4^4=\|(P_\rho f)^2\|_2^2\). Its six candidate pair-sum frequencies are \(0,m,n,2m,m+n,2n\). They are distinct except that \(n=2m\) identifies the pair sums \(0+n\) and \(m+m\). Consequently, if \(n\ne2m\), with input energies \(x_j=|c_j|^2\) summing to one,
\[
F(x)=\sum_{j=0}^2w_j^2x_j^2+4\sum_{0\le i<j\le2}w_iw_jx_ix_j,
\quad (w_0,w_1,w_2)=(1,a,b).
\]
There is no phase dependence. For resonance the extra term is \(4\operatorname{Re}(u_0u_2\overline{u_1}^{\,2})\), maximized precisely when the three positive amplitudes have aligned quadratic phase.

**2. The constant-only regime.** For \(a\le1/2\), also \(b\le1/2\). The off-diagonal coefficients of \(F\) do not exceed those of \((x_0+x_1+x_2)^2\): \(4a\le2\), \(4b\le2\), and \(4ab\le1<2\). The diagonal coefficients are at most one. Hence \(F\le1\), with equality only at \((1,0,0)\). For resonance, write aligned nonnegative amplitudes \((X,Y,Z)\) with \(X^2+Y^2+Z^2=1\). Its exact moment is
\[
R_a=X^4+a^2Y^4+a^4Z^4+4aX^2Y^2+4a^2X^2Z^2+4a^3Y^2Z^2+4a^2XY^2Z.
\]
At \(a=1/2\) there is an explicit sum-of-squares identity
\[
(X^2+Y^2+Z^2)^2-R_{1/2}
=\left(XZ-\frac12Y^2\right)^2+\frac12Y^4+\frac{15}{16}Z^4+\frac32Y^2Z^2.
\]
It vanishes only when \(Y=Z=0\). Every coefficient in \(R_a\) is nonnegative and nondecreasing in \(a\), so the same unique constant optimizer holds for \(a<1/2\).

**3. Nonresonant pair region.** On the face \(x_2=0\), put \(x_1=s\). Then
\[
F(1-s,s,0)=1+(4a-2)s+(a^2-4a+1)s^2.
\]
For \(a>1/2\), its unique maximum has \(s=(2a-1)/(4a-1-a^2)\) and value \(1+(2a-1)^2/(4a-1-a^2)\). The inward first derivative in the \(x_2\) direction vanishes precisely at \(b=b_*(a)\), is negative below and positive above. At that boundary the full simplex quadratic \(F\) is strictly concave: with \(x_0=1-x_1-x_2\), half its Hessian is
\[
T=\begin{pmatrix}a^2-4a+1&2ab-2a-2b+1\\2ab-2a-2b+1&b^2-4b+1\end{pmatrix}.
\]
The first diagonal entry is negative. Its determinant is a concave quadratic function of \(b\), and at the endpoints of the interval \([b_*(a),a]\) it equals
\[
\det T\big|_{b=b_*}=\frac{-15a^2(a^2-4a+1)}{4(1+a)^2}>0,
\quad \det T\big|_{b=a}=a^2(-3a^2+8a-2)>0.
\]
Thus \(F\) is strictly concave for \(b_*(a)\le b\le a\). At \(b=b_*\), the two-mode maximizer is stationary in the full simplex and hence uniquely optimal. For \(b<b_*\), the polynomial \(F(x;a,b)\) is nondecreasing in \(b\) at each fixed nonnegative \(x\) and strictly increasing whenever \(x_2>0\); comparison to \(b=b_*\) proves the same unique pair maximizer.

**4. All-three regime.** For \(b>b_*\), the pair-face maximum has positive inward derivative and so is not globally optimal. No other face can contain a maximum. If \(x_0=0\) with \(x_1>0\), its inward gradient toward \(x_0\) exceeds the derivative along \(x_1\) by \(2a(2-a)x_1+4b(1-a)x_2>0\); at a remaining vertex the other coordinate gives an improvement. If \(x_1=0\) with \(x_2>0\), its inward gradient toward \(x_1\) exceeds that along \(x_2\) by \(4(a-b)x_0+2b(2a-b)x_2>0\); the vertex \(x_0=1\) is not optimal when \(a>1/2\). The strict concavity from Step 3 therefore forces a unique interior maximizer.

Write \(S=\sum w_jx_j\). Lagrange stationarity gives \(4w_j S-2w_j^2x_j=\lambda\). Solving jointly with \(\sum_jx_j=1\) yields exactly
\[
x_j=\frac{2H/w_j-5/w_j^2}{D},\qquad D=2H^2-5J.
\]
The stationary value is \(\lambda/2=5/D\). This proves the formula and positivity of its denominators and components in the stated physical region. The ratio \(b/b_*(a)=\frac23\rho^{2(n-m)}(1+\rho^{2m})\) strictly increases from below one at \(\rho_1\) to \(4/3\) at \(\rho=1\), proving the unique later threshold.

**5. Resonant immediate activation and asymptotics.** For \(a>1/2\), the best \(\{0,m\}\) pair uses both coefficients and has value larger than one. Among two-mode supports it dominates \(\{0,2m\}\) by the ordering of Poisson multipliers, and \(\{m,2m\}\) because the latter's fourth-power norm is \(a^2\) times the \(\{0,m\}\) pair norm. Adding a small positive second-harmonic amplitude \(Z\) to an aligned nonzero \(\{0,m\}\) optimizer increases its fourth moment linearly by the positive resonance term \(4a^2XY^2Z\), whereas the normalization costs only order \(Z^2\). Hence no optimizer omits a mode. The phase alignment in Step 1 is therefore necessary.

For the near-onset analysis set \(a=1/2+\delta\), \(t=Y^2\), \(Z=z\), and \(X=\sqrt{1-t-z^2}\). Compactness and the strict unique optimizer at \(\delta=0\) force all global optimizing profiles toward \((t,z)=(0,0)\). The analytic expansion near the origin is
\[
R_a=1+4\delta t-\frac34t^2+tz-z^2+O\bigl(\delta(t^2+z^2+|tz|)+(|t|+|z|)^3\bigr).
\]
The Hessian in \((t,z)\) at \(\delta=0\) is strictly negative definite. The implicit-function theorem gives a unique nearby interior critical point satisfying \(t=4\delta+O(\delta^2)\), \(z=2\delta+O(\delta^2)\); all global optimizers lie there for small positive \(\delta\). Substitution gives \(z^2=4\delta^2+O(\delta^3)\) and \(R_a=1+8\delta^2+O(\delta^3)\). The nonresonant leading comparison follows by expanding the second branch in Step 3.

## Verification
From the directory containing `checker.py`, run `python3 -m pip install -r requirements.txt` and then `python3 checker.py`. The stand-alone checker uses exact SymPy identities for the stationary values, the Hessian boundary determinants, the resonant sum of squares and the onset expansion; exact Gaussian-rational Fourier convolution for varied frequency pairs; and randomized simplex stress tests against the sharp formulas. It completed 2,141 assertions. Those finite frequency and numerical tests do not certify the universal theorem on their own: that follows from the analytical collision classification, concavity argument, sum-of-squares identity and implicit-function proof.

## Relationship to prior work
Ivanisvili–Lindenberger–Müller–Schmuckenschläger (2020 preprint), Section 3, treats hypercontractivity for **linear** polynomials \(u+vz\) under ultraspherical measures. Frank–Ivanisvili (2021), Theorem 1.1, establishes global sphere Poisson-semigroup hypercontractivity conditions, not sharp supercritical restricted three-character norms. Weissler's classical circle hypercontractivity theorem gives the context for the first contraction threshold but does not by itself state the exact second activation transition or the resonant spectral-mixing asymptotics.

The available three-character \(\Lambda(4)\) finite-cyclic classification determines the **unweighted** endpoint at equal multipliers and some equality patterns; it does not supply the continuous family of Poisson-weighted norms and exact frequency-dependent transition radii. An available full-space **real, zero-mean two-frequency** Poisson \(L^2\)-to-\(L^4\) theorem has a \(1{:}3\) resonance, whereas the present **analytic, constant-containing three-character** result has a \(1{:}2\) collision and a different phase diagram. The new contribution is the sharp nonresonant all-radius law and the contrasting immediate resonant high-mode activation.

## Limitations
The result is restricted to analytic trinomials of the indicated frequency structure and the fourth output moment. The resonant global norm is **not** expressed by an all-radius closed form, and global uniqueness of resonant amplitude profiles is proved only sufficiently close to the first threshold. Independent examination and historical priority certification have not been performed. Inaccessible full texts (notably parts of historical circle hypercontractivity literature) and unindexed equivalent weighted-trinomial results remain priority risks.

## References
1. P. Ivanisvili, A. Lindenberger, P. F. X. Müller and M. Schmuckenschläger, *Hyper contractivity on the unit circle for ultraspherical measures: linear case*, arXiv:2004.05567v1, first public 2020-04-12, https://arxiv.org/abs/2004.05567.
2. R. L. Frank and P. Ivanisvili, *Hypercontractivity of the semigroup of the fractional laplacian on the n-sphere*, arXiv:2101.06209v1, first public 2021-01-15, https://arxiv.org/abs/2101.06209.
3. F. B. Weissler, *Logarithmic Sobolev inequalities and hypercontractive estimates on the circle*, Journal of Functional Analysis 37 (1980), 218–234, DOI:10.1016/0022-1236(80)90042-7.
4. *Exact \(\Lambda(4)\) constants for every three-character subset of a cyclic group*, publicly available mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-lambda-4-constants-for-every-three-character-subset-of-a-c--5562292e7127.
5. *Resonant persistence and sharp mode selection for two-frequency circular Poisson smoothing*, publicly available mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-resonant-persistence-and-sharp-mode-selection-for-two-frequency--ebfd25bec609.
