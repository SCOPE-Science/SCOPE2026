# Sharp Fejér bandwidth staircase for circular heat-kernel approximation

## Finding

Let \(H_t(\theta)=\sum_{k\in\mathbb Z}e^{-tk^2}e^{ik\theta}\), for \(t>0\), be the mean-one heat kernel on the circle, and let
\[
F_{N,\phi}(\theta)=\sum_{|k|<N}\left(1-\frac{|k|}{N}\right)e^{ik(\theta-\phi)},\qquad N\in\mathbb N,
\]
be a translated mean-one Fejér kernel. Use normalized Haar measure \(d\theta/(2\pi)\) in every \(L^2\) norm. Define \(E_N(t)=\|H_t-F_{N,0}\|_2^2\).

For every \(N\ge1\) there is exactly one \(t_N>0\) determined by
\[
\sum_{k=1}^N k e^{-t_Nk^2}=\frac{2N(N+1)-1}{12}.
\]
These thresholds satisfy \(t_1=\log4>t_2>\cdots>0\) and \(t_N\downarrow0\). For every \(t\in(t_N,t_{N-1})\), with \(t_0=\infty\), the **unique** minimizing Fejér order is \(N\); for \(t=t_N\), precisely orders \(N\) and \(N+1\) tie. Every minimizing kernel of order at least two has its unique optimal center \(\phi=0\pmod{2\pi}\); the order-one kernel is constant and its center is immaterial.

Let \(u_*\in(2,3)\) be the unique positive solution of
\[
1-e^{-u_*}=u_*/3,\qquad c_*=\sqrt{u_*}.
\]
Then the entire staircase and the optimum error have sharp small-time laws
\[
t_N=\frac{u_*}{N(N+1)}+O(N^{-4}),\quad N_{\mathrm{opt}}(t)\sqrt t\longrightarrow c_*,
\]
\[
\min_{N\ge1,\phi}\|H_t-F_{N,\phi}\|_2^2\sim\frac{J_*}{\sqrt t},\qquad
J_*=\sqrt{\frac\pi2}-2\sqrt\pi\,\operatorname{erf}(c_*)+\frac{4c_*}{3}>0.
\]
Numerically, \(u_*\approx2.821439372122079\), \(c_*\approx1.679714074514493\), and \(J_*\approx0.010154696409760\).

In contrast, choosing an integer \(N_{\mathrm{moment}}(t)\) nearest to \((1-e^{-t})^{-1}\), which matches the first Fourier multiplier to rounding accuracy, incurs
\[
\|H_t-F_{N_{\mathrm{moment}}(t),0}\|_2^2\sim\frac{2}{3t};
\]
thus its error ratio to the optimal Fejér squared error diverges as \(\frac{2}{3J_*}t^{-1/2}\).

## Assumptions and scope

The circle is \(\mathbb R/(2\pi\mathbb Z)\); the heat semigroup generator is \(\partial_\theta^2\), so Fourier multiplier \(k\) is exactly \(e^{-tk^2}\). Fejér order \(N=1\) denotes the constant kernel; order \(N\) has modes \(|k|<N\), not \(|k|\le N\). Only integer orders and translated, nonnegative normalized Fejér kernels are admissible; general nonnegative trigonometric polynomials, scalar rescalings, and other filters are not covered. Every statement holds for all real \(t>0\) and integer \(N\ge1\).

## Proof

**1. Centering.** Parseval gives
\[
\|H_t-F_{N,\phi}\|_2^2=\|H_t\|_2^2+\|F_{N,0}\|_2^2-2-4\sum_{k=1}^{N-1}e^{-tk^2}\Big(1-\frac{k}{N}\Big)\cos(k\phi).
\]
For \(N\ge2\), the \(k=1\) coefficient is positive and all other coefficients are nonnegative. The cross-inner product is maximized exactly when \(\cos\phi=1\); for \(N=1\), the kernel is identically one. Consequently order optimization reduces to \(E_N(t)\).

**2. Exact adjacent difference and global ordering.** Let \(S_N(t)=\sum_{k=1}^N k e^{-tk^2}\). The finite spectral identity and elementary sum of squares yield
\[
E_N(t)=2\sum_{k=1}^\infty e^{-2tk^2}-4\sum_{k=1}^{N-1}e^{-tk^2}\Big(1-\frac{k}{N}\Big)+\frac{(N-1)(2N-1)}{3N}.
\]
The infinite series is absolutely convergent. Subtraction cancels its tail exactly:
\[
\Delta_N(t):=E_{N+1}(t)-E_N(t)=\frac23-\frac{1}{3N(N+1)}-\frac{4S_N(t)}{N(N+1)}.\tag{1}
\]
For each \(t>0\), \(2S_N/[N(N+1)]\) is the average of the strictly decreasing numbers \(e^{-tk^2}\), \(1\le k\le N\), with positive weights proportional to \(k\). Adding the next, smaller entry strictly lowers the average. Therefore \(S_N/[N(N+1)]\) strictly decreases with \(N\). Equation (1) shows that \(\Delta_N(t)\) is strictly increasing in \(N\), so \(E_N(t)\) is a strictly convex sequence and cannot have nonadjacent or three-way minimizer ties. Furthermore \(\Delta_N(t)\to 2/3>0\) as \(N\to\infty\), because \(S_N(t)\) is bounded.

At \(t=0\) the expression (1), interpreted by its finite sum, is strictly negative; as \(t\to\infty\) it is positive. As a function of \(t>0\), it is strictly increasing, hence has one zero \(t_N\). At \(t_N\) strict increase in \(N\) forces \(\Delta_{N+1}(t_N)>0\), hence \(t_{N+1}<t_N\); similarly \(t_N\to0\), since at every fixed positive time \(\Delta_N\to2/3\). The sign change of consecutive differences proves the complete staircase, including all ties. Setting \(N=1\) gives \(t_1=\log4\).

**3. Threshold asymptotics.** Define \(u_N=N^2t_N\). From the defining equation,
\[
\frac1N\sum_{k=1}^N \frac{k}{N}\,e^{-u_N(k/N)^2}=\frac16+\frac{1}{6N}-\frac{1}{12N^2}.
\]
For any fixed \(u\ge0\), the left side converges to \(I_1(u)=\int_0^1 x e^{-ux^2}\,dx=(1-e^{-u})/(2u)\), with its continuous value \(I_1(0)=1/2\). This strictly decreases from \(1/2\) to zero; the right side tends to \(1/6\). Monotonicity in \(u_N\) and comparison with two fixed bracketing values show \(u_N\to u_*\), where \(I_1(u_*)=1/6\). Its equation has one positive root, which lies in \((2,3)\).

For the finer expansion use Euler–Maclaurin uniformly for \(u\) in a compact neighborhood of \(u_*\):
\[
S_N(u/N^2)=N^2 I_1(u)+\frac N2e^{-u}+O(1).
\]
Monotonicity and the nonzero derivative \(I_1'(u_*)=-I_3(u_*)\) first yield \(u_N=u_*+O(N^{-1})\), where \(I_3(u)=\int_0^1x^3e^{-ux^2}dx\). Write \(u_N=u_*+v/N+O(N^{-2})\) and compare coefficients of \(N\) in the threshold equation:
\[
-vI_3(u_*)+\tfrac12e^{-u_*}=\tfrac16.
\]
Using \(e^{-u_*}=1-u_*/3\) gives \(I_3(u_*)=(u_*-2)/(6u_*)\), whence \(v=-u_*\). The nonzero derivative and uniform expansion control the residual by \(O(N^{-2})\), so \(t_N=u_*/N^2-u_*/N^3+O(N^{-4})=u_*/[N(N+1)]+O(N^{-4})\). Bracketing an optimal order between consecutive thresholds immediately yields \(N_{\mathrm{opt}}(t)\sqrt t\to c_*\) (both adjacent orders obey this limit at tie times).

**4. Sharp error constant.** For any orders with \(N\sqrt t\to c>0\), apply Riemann-sum convergence to the exact expression in Step 2, obtaining
\[
\sqrt t\,E_N(t)\to J(c)=\sqrt{\frac\pi2}-4\int_0^c e^{-x^2}(1-x/c)\,dx+\frac{2c}{3}.
\]
Direct differentiation gives \(J'(c)=2/3-2(1-e^{-c^2})/c^2\). The ratio \((1-e^{-c^2})/c^2\) strictly decreases from one to zero. Hence \(J\) has a unique minimizer \(c_*=\sqrt{u_*}\). Its value simplifies, using \(1-e^{-u_*}=u_*/3\), to the displayed \(J_*\). It is strictly positive because \(J(c)\) is the integral of the square of the difference between \(e^{-x^2}\) and the triangular profile \((1-x/c)_+\) over \(\mathbb R\); those continuous functions differ on sets of positive measure. The threshold result places every optimal sequence in this scaling, proving the claimed minimum error law.

**5. Moment-matching comparison.** Since \(N_{\mathrm{moment}}\sim t^{-1}\), the exact expression in Step 2 gives \(2\sum_{k\ge1}e^{-2tk^2}=O(t^{-1/2})\) and the magnitude of the cross term at most \(4\sum_{k\ge1}e^{-tk^2}=O(t^{-1/2})\). The elementary quadratic Fejér sum equals \((2/3)N_{\mathrm{moment}}+O(1)\). Therefore the stated \(2/(3t)\) law and divergent ratio follow without additional regularity assumptions.

## Verification

Run `python3 checker.py` in a standard Python 3 environment. It uses the standard library only and checks the adjacent-difference identity, monotonicity, root ordering, second-order threshold scale, direct angular quadrature, small-time error scaling, and moment-match penalty. `CHECKER_OUTPUT.txt` records the observed deterministic output. These finite diagnostics do not substitute for the analytic arguments above.

## Relationship to prior work

Fu–Hou–Wu (first posted 2022) prove convergence properties of fractional Fejér kernels and the associated fractional heat equation; in the ordinary circle case their formulas give the two multiplier families. They do not determine the best integer Fejér order for a heat kernel in squared \(L^2\), a global staircase or a sharp calibration limit. Abdullayev–Savchuk (first posted 2021) study generalized positive Fejér means in a Takenaka–Malmquist basis, rather than least-squares fitting a heat kernel. Colbrook–Townsend (first posted 2021), Section 3.2, use Fejér's triangular Fourier filter and discuss convergence and bandwidth heuristics for spectral measures; they do not solve this fixed Gaussian-target integer-order optimization. The transcendental root \(u_*\) is independently tabulated as OEIS A194567, so the numerical constant alone is not claimed new. Existing related heat-to-Poisson fitting results optimize a continuous Poisson radius, not Fejér order, and do not imply the staircase.

## Limitations

The result concerns squared normalized \(L^2\) distance for exact centered heat kernels and the one-parameter Fejér family. It does not claim optimality among arbitrary positive trigonometric polynomials, among other spectral tapers, in \(L^1\), or for data-dependent noisy density estimation. The source comparison establishes best-knowledge historical originality, not exhaustive priority or independent verification. Exact integer switch times are implicit unique roots, not elementary closed forms for general order.

## References

1. Z. Fu, X. Hou, Q. Wu, *Convergence of fractional Fourier series on the torus and applications*, arXiv:2210.14720 (initial public posting 2022-10-26), https://arxiv.org/abs/2210.14720.
2. F. G. Abdullayev and V. V. Savchuk, *Fejér-type positive operator based on Takenaka–Malmquist system on unit circle*, arXiv:2106.08675 (initial posting 2021-06-16), https://arxiv.org/abs/2106.08675.
3. M. J. Colbrook and A. Townsend, *Rigorous data-driven computation of spectral properties of Koopman operators for dynamical systems*, arXiv:2111.14889 (initial posting 2021-11-29), https://arxiv.org/abs/2111.14889; see Section 3.2 on the hat Fourier filter.
4. OEIS A194567, positive solution to \(u=3(1-e^{-u})\), https://oeis.org/A194567 (constant identification only, not an approximation theorem).
