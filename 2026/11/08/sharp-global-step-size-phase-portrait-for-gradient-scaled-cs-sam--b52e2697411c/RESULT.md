# Sharp global step-size phase portrait for gradient-scaled CS-SAM on a convex quadratic

## Finding
Consider the curvature-scaled sharpness-aware minimization (CS-SAM) update defined below. Its exact global behavior on the scalar quadratic with a strictly gradient-dependent curvature scale has a sharp threshold
\[
\gamma_{\mathrm c}=\frac{2}{1+\rho}.
\]
For every \(\rho\geq0\) and every positive curvature-scale slope, all trajectories converge to the minimizer when \(0<\gamma\leq\gamma_{\mathrm c}\). At equality, nonterminating trajectories have the exact dimensionless amplitude law
\[
\ell|x_k|\sim\frac{1+\rho}{2(1+3\rho+\rho^2)}\frac1k.
\]
For \(\gamma>\gamma_{\mathrm c}\), there is a unique nonzero symmetric two-cycle; every trajectory either reaches the minimizer in finitely many steps or converges to this two-cycle, with eventual sign alternation in the latter case. The cycle has amplitude \(p/\ell\), where \(p>0\) is the unique solution of
\[
\gamma\frac{1+p+\rho}{(1+p)^2+\rho p}=2,
\]
and hence
\[
p=\frac{\gamma-4-2\rho+\sqrt{(4+2\rho-\gamma)^2+8(\gamma(1+\rho)-2)}}{4}.
\]
The zero-hitting starting values in the supercritical regime form an at-most-countable set. Thus, unlike the constant-curvature-scale update, positive gradient-dependent scaling converts every supercritical nonterminating trajectory into bounded but nonoptimal oscillation rather than divergence. These conclusions remain valid for perturbations \(\rho\geq\log2\), outside the motivating paper's sufficient convergence condition, whenever the stated scalar step criterion holds.

## Assumptions and scope
Work in exact real arithmetic. Let \(a>0\), \(\ell>0\), \(\rho\geq0\), \(\gamma>0\), and
\[
f(x)=\frac a2 x^2,\qquad M(x)=a+\ell|f'(x)|=a(1+\ell|x|).
\]
The pair \((L_0,L_1)=(a,\ell)\) is a valid, possibly nonminimal, generalized smoothness bound because \(|f''(x)|=a\leq a+\ell|f'(x)|\) for all real \(x\). Define the *two-scale* CS-SAM iteration, for every \(k\geq0\), by
\[
y_k=x_k+\frac{\rho f'(x_k)}{M(x_k)},\qquad x_{k+1}=x_k-\frac{\gamma f'(y_k)}{M(y_k)}.
\]
The initial value \(x_0\) is any real number. No stochasticity, preconditioning or numerical roundoff is included. The case \(\rho=0\) is included as the normalized-gradient boundary; the genuinely sharpness-aware regime is \(\rho>0\). The positive slope \(\ell\) is essential to the global boundedness conclusion above the threshold.

## Proof
**Exact reduction.** Put \(t=\ell|x|\). Since \(1+\rho/(1+t)>0\), the perturbation has the same sign as \(x\), and direct substitution yields
\[
x^+=x\{1-\gamma F_\rho(t)\},\quad
F_\rho(t)=\frac{1+t+\rho}{1+(2+\rho)t+t^2},\quad
t^+=T(t)=t|1-\gamma F_\rho(t)|.
\]
The rational denominator is strictly positive for \(t\geq0\). Its exact derivatives give
\[
F_\rho'(t)=-\frac{t^2+(2+2\rho)t+(1+3\rho+\rho^2)}{[1+(2+\rho)t+t^2]^2}<0,
\]
\[
\frac{d}{dt}[tF_\rho(t)]=\frac{(1+t)^2+\rho}{[1+(2+\rho)t+t^2]^2}>0.
\]
In particular, \(F_\rho(0)=1+\rho\), while \(F_\rho(t)\downarrow0\) as \(t\to\infty\).

**Subcritical and critical regimes.** If \(0<\gamma\leq2/(1+\rho)\), then \(0<\gamma F_\rho(t)<2\) for every \(t>0\). Hence \(0\leq T(t)<t\). The decreasing amplitudes have a limit; any positive limit would satisfy \(|1-\gamma F_\rho(t)|=1\), impossible for positive gain strictly below two. Thus every trajectory reaches zero or tends to zero. At equality, with \(K_\rho=1+3\rho+\rho^2\) and \(c=2K_\rho/(1+\rho)\), Taylor expansion gives
\[
\gamma F_\rho(t)=2-ct+O(t^2),\qquad T(t)=t-ct^2+O(t^3)
\]
for sufficiently small positive \(t\). For any trajectory never reaching zero, \(t_k\to0\), and thus
\[
\frac{1}{t_{k+1}}-\frac{1}{t_k}=c+O(t_k)\longrightarrow c.
\]
Cesàro summation yields \(1/(k t_k)\to c\), which proves the stated sharp \(k^{-1}\) law. For \(\gamma=1/(1+\rho)\) below the threshold, the linear multiplier cancels and \(T(t)=[K_\rho/(1+\rho)]t^2+O(t^3)\), providing local quadratic convergence of nonterminating trajectories.

**Supercritical existence and uniqueness.** If \(\gamma>2/(1+\rho)\), strict decrease of \(F_\rho\) produces exactly one \(p>0\) with \(\gamma F_\rho(p)=2\). Its defining quadratic has negative constant coefficient \(2-\gamma(1+\rho)<0\), so precisely one root is positive, given above. The signed map sends \(p/\ell\) to \(-p/\ell\) and back. Any nonzero fixed amplitude requires \(|1-\gamma F_\rho(t)|=1\); positive gain forces \(\gamma F_\rho(t)=2\), hence \(t=p\).

**Global attraction, not merely local stability.** Write \(G(t)=tF_\rho(t)\), which is strictly increasing and satisfies \(\gamma G(p)=2p\). For \(0<t<p\), the multiplier is less than \(-1\) and
\[
t<T(t)=\gamma G(t)-t<2p-t.
\]
For \(p<t<2p\), monotonicity of \(G\) implies \(\gamma F_\rho(t)>2p/t>1\), while \(\gamma F_\rho(t)<2\), giving
\[
2p-t<T(t)=\gamma G(t)-t<t.
\]
Consequently, for all \(0<t<2p\) with \(t\ne p\),
\[
0<T(t)<2p,\qquad |T(t)-p|<|t-p|.
\]
For \(t\geq2p\), \(0\leq T(t)<t\). If such an orbit does not hit zero, it must eventually enter \((0,2p)\): otherwise its decreasing amplitudes converge to a positive fixed point in \([2p,\infty)\), contradicting uniqueness of \(p\). Inside \((0,2p)\) the strict decrease of \(|t_k-p|\), compactness and continuity force that distance to tend to zero. Indeed, a positive limiting distance would admit a subsequential limit \(t_*\ne p\) in a compact subinterval of \((0,2p)\), violating strict decrease at \(t_*\). Therefore \(t_k\to p\). As \(\gamma F_\rho(p)=2\), the multiplier tends to \(-1\), so signs alternate for all sufficiently large indices. The signed orbit approaches the symmetric two-cycle.

**Finite termination.** Exact termination occurs precisely if an iterate satisfies \(\gamma F_\rho(t)=1\) (or has already reached zero). Each iterate of the signed rational map is, on each of finitely many sign branches, rational with finite-degree numerator; its nonconstant analytic branches have finite zero sets, and the original map cannot be identically zero on a nontrivial interval. The union of finite-step zero-preimage sets is therefore countable. No zero-hitting initialization converges to the nonzero two-cycle.

## Verification
The standalone `CHECK.py` uses exact rational arithmetic to compare the full two-stage update against the reduced recurrence for 35 parameter combinations and 71 input points each. It verifies the signed rational orbit \(\pm1\) at \(\rho=1\), \(\gamma=10/3\), \(\ell=1\), and also runs derivative-sign, Lyapunov-inequality, and borderline-rate diagnostics. Run:

```text
python3 CHECK.py
```

The verifier reports 11,865 supplementary checks passed. These finite checks are *not* a proof of the quantified global statements; their proof is the algebraic argument above.

## Relationship to prior work
Oikonomou and Loizou (2026) introduce CS-SAM and establish sufficient convergence conditions, including \(\rho<\log2\), for broad classes of generalized-smooth objectives. Their quadratic example with the *constant* scale has a linear CS-SAM recurrence; their nonzero two-cycle example concerns conventional fixed-radius SAM, not the gradient-dependent two-scale update here. The present result concerns the exact global phase portrait when the permissible positive gradient-dependent component of the scale is retained. Bartlett, Long and Bousquet (2023) prove cycles for conventional fixed-radius SAM; their iteration has a different perturbation rule and does not imply this scaled rational recurrence or its critical decay. Vankov and collaborators (2025) analyze gradient-dependent steps and convergence complexity but not the two-stage CS-SAM phase portrait. Rossi, Campelo and Oliveira (2026) analyze a dynamic-radius CAP-SAM rule, not the double-normalized fixed-\(\rho\) CS-SAM update.

## Limitations
The theorem is exact only for a scalar, centered strongly convex quadratic with the specified, possibly loose, gradient-dependent curvature scale and positive slope. In particular, the nonzero-cycle phenomenon does not persist as a bounded orbit for the constant-scale \(\ell=0\) algorithm: there the recurrence is linear and supercritical steps give geometric divergence. Nothing is claimed about global behavior of the general nonconvex optimization class, multivariate quadratics, minibatch noise, numerical roundoff or an optimal practical stepsize. The historical-priority search cannot rule out unindexed equivalent rational-map calculations. Independent mathematical review has not been performed.

## References
1. D. Oikonomou and N. Loizou, *Curvature-Scaled Sharpness-Aware Minimization: Convergence Beyond Smoothness*, arXiv:2610.29192v1, submitted 2026-10-21, https://arxiv.org/abs/2610.29192.
2. P. L. Bartlett, P. M. Long and O. Bousquet, *The Dynamics of Sharpness-Aware Minimization: Bouncing Across Ravines and Drifting Towards Wide Minima*, JMLR 24(316), 2023, https://jmlr.org/papers/v24/23-043.html.
3. D. Vankov and collaborators, *Optimizing \(L_{0},L_{1}\)-Smooth Functions by Gradient Methods*, arXiv:2410.10800v3, https://arxiv.org/abs/2410.10800.
4. A. Rossi, F. Campelo and G. L. Oliveira, *One Size Does Not Fit All: Curvature-Aware Adaptive Perturbation for SAM*, arXiv:2610.20415v1, submitted 2026-10-14, https://arxiv.org/abs/2610.20415.
