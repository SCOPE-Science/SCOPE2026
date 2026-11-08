# A sharp all-spectrum gradient-safety frontier for cyclic steepest descent

## Finding

Let \(m\ge2\) be an arbitrary integer. Consider a cycle of \(m\) gradient steps on a strictly convex quadratic in which the first step is an exact Cauchy step and that same step length is reused for the remaining \(m-1\) steps. **The sharp dimension-independent boundary for nonexpansion of the gradient norm after a complete cycle** is a uniquely determined condition number \(\kappa_m>2\). More precisely,

\[
\mathcal R_m(\kappa)=\max_{t>0}
\frac{(\kappa-1)^{2m}(t+t^{2m})}
{(1+\kappa t)^{2m}(1+t)}
\]

is the exact largest *squared* complete-cycle gradient-norm factor over all nonzero initial gradients for **each** symmetric positive-definite matrix whose largest-to-smallest eigenvalue ratio is \(\kappa\ge1\). For \(\kappa>1\), the maximum can equivalently be taken over \(t\in[0,\infty]\) with the endpoint values interpreted as limits. The factor vanishes identically when \(\kappa=1\).

For each \(m\ge2\), the equation \(\mathcal R_m(\kappa_m)=1\) has exactly one solution with \(\kappa_m>2\). The following sharp conclusions hold:

- When \(\kappa<\kappa_m\), every nonzero gradient strictly contracts after the cycle.
- When \(\kappa=\kappa_m\), all gradients are nonexpansive and a two-eigenvalue initialization attains equality.
- When \(\kappa>\kappa_m\), an initialization supported on the extreme eigenspaces strictly increases the norm.

The boundaries strictly decrease in cycle length and satisfy

\[
\kappa_{m+1}<\kappa_m,\qquad
\lim_{m\to\infty}\kappa_m=2,\qquad
\kappa_m=2+\frac{\log m+\log(4e)+o(1)}{2m}.
\]

## Assumptions and scope

Let \(f(x)=\frac12x^THx-b^Tx\) for a real symmetric positive-definite \(d\times d\) matrix \(H\), \(d\ge2\). Denote the smallest and largest eigenvalues by \(a>0\) and \(b_H\ge a\), respectively, and their ratio by \(\kappa=b_H/a\). Starting at any \(x\) with nonzero gradient \(g=Hx-b\), calculate \(\alpha=(g^Tg)/(g^THg)\). Within the cycle perform \(x_{j+1}=x_j-\alpha(Hx_j-b)\) for \(j=0,\ldots,m-1\), without recalculating \(\alpha\). Thus \(g_m=(I-\alpha H)^mg\). The theorem concerns the Euclidean gradient norm at the *cycle boundary*, not the objective decrease on individual interior steps, nor the Euclidean error to the minimizer. The result is exact arithmetic and applies to every finite dimension.

## Proof

**1. Reduction from all spectra to their endpoints.** Let \(\lambda_i\in[a,b_H]\) be eigenvalues and \(w_i\ge0\) the squared gradient component masses normalized by \(\|g\|^2\), so \(\sum_iw_i=1\). Define \(\mu=\sum_iw_i\lambda_i=1/\alpha\). The squared gradient multiplier is

\[
Q=\sum_iw_i(1-\lambda_i/\mu)^{2m}.
\]

For fixed \(\mu>0\), \(\phi_\mu(\lambda)=(1-\lambda/\mu)^{2m}\) is convex throughout the spectral interval. Its endpoint chord gives, pointwise,

\[
\phi_\mu(\lambda)\le
\frac{b_H-\lambda}{b_H-a}\phi_\mu(a)
+\frac{\lambda-a}{b_H-a}\phi_\mu(b_H).
\]

Averaging shows that \(Q\) is at most the value for endpoint weights \(w_a=(b_H-\mu)/(b_H-a)\) and \(w_b=(\mu-a)/(b_H-a)\), whose mean is still \(\mu\). This endpoint pair exists as a gradient supported on the two extreme eigenspaces of the same \(H\). For \(a=b_H\), one step already yields the exact minimizer.

**2. Exact two-eigenvalue formula.** By positive scaling take \(a=1\), \(b_H=\kappa\), and put \(t=w_b/w_a>0\). Then \(\alpha=(1+t)/(1+\kappa t)\). The multipliers on the upper and lower eigenspaces are respectively \((1-\kappa)/(1+\kappa t)\) and \((\kappa-1)t/(1+\kappa t)\). Squaring after \(m\) repeated steps and averaging gives

\[
Q=F_m(\kappa,t)=
\frac{(\kappa-1)^{2m}(t+t^{2m})}
{(1+\kappa t)^{2m}(1+t)}.
\]

The two endpoint limits are both zero, \(F_m(\kappa,0)=F_m(\kappa,\infty)=0\). Thus this expression maximized over \(t\) is the exact universal factor for *every fixed* \(H\) of condition \(\kappa\).

**3. Existence, uniqueness and sharpness of the threshold.** For each \(t>0\), the factor \((\kappa-1)/(1+\kappa t)\) strictly increases with \(\kappa>1\). Compactification of \(t\in[0,\infty]\) makes \(\mathcal R_m\) continuous in \(\kappa\) and strictly increasing for \(\kappa>1\) (any maximizing positive \(t\) witnesses strictness). When \(\kappa=2\), every endpoint multiplier has absolute value strictly below \(1\) for finite positive \(t\); the endpoint limits are also below \(1\), so \(\mathcal R_m(2)<1\). At fixed \(t>0\) sufficiently small, \(F_m(\kappa,t)\) exceeds \(1\) for sufficiently large \(\kappa\), since its limit is \((t+t^{2m})/[t^{2m}(1+t)]>1\). This proves a unique crossing \(\kappa_m>2\). At the crossing the maximizing \(t\) is finite and positive, giving equality. The same construction gives strict amplification above the crossing.

**4. Strict decrease with cycle length.** At \(\kappa_m\) choose a maximizing endpoint distribution with \(Q=1\). Its two absolute mode multipliers are not equal: if they were equal, both would be \((\kappa_m-1)/(\kappa_m+1)<1\), contradicting \(Q=1\). Strict power-mean inequality therefore gives

\[
\sum_iw_i|1-\alpha\lambda_i|^{2m+2}
>\left(\sum_iw_i|1-\alpha\lambda_i|^{2m}\right)^{(m+1)/m}=1.
\]

Hence \(\mathcal R_{m+1}(\kappa_m)>1\) and, by uniqueness of its crossing, \(\kappa_{m+1}<\kappa_m\).

**5. Large-cycle asymptotics.** Factor

\[
\mathcal R_m(\kappa)=(\kappa-1)^{2m}h_m(\kappa),\quad
h_m(\kappa)=\sup_{t>0}\frac{t+t^{2m}}{(1+\kappa t)^{2m}(1+t)}.
\]

The function \(t/(1+\kappa t)^{2m}\) is maximized at \(t_*=1/[\kappa(2m-1)]\), with maximum

\[
U_m(\kappa)=\frac1{\kappa(2m-1)}
\left(\frac{2m-1}{2m}\right)^{2m}.
\]

Splitting the numerator yields the rigorous sandwich

\[
\frac{U_m(\kappa)}{1+t_*}
\le h_m(\kappa)\le U_m(\kappa)+\kappa^{-2m}.
\]

For every fixed \(\kappa>2\), the lower bound implies \(\mathcal R_m(\kappa)\to\infty\); together with \(\kappa_m>2\) and the preceding strict decrease this proves \(\kappa_m\to2\). Uniformly for \(\kappa\in[2,3]\), the sandwich yields

\[
h_m(\kappa)=\frac{1+o(1)}{2e\kappa m}.
\]

Substituting \(\kappa=\kappa_m\) into \(\mathcal R_m=1\) and taking logarithms gives \(2m\log(\kappa_m-1)=\log(2e\kappa_m m)+o(1)\), which first implies \(\kappa_m-2=O(\log(m)/m)\), and then the stated sharp expansion.

## Verification

The standalone standard-library script `verify.py` checks the exact two-mode recurrence identity over rational inputs, an explicit strict-amplification certificate, and rational endpoint-chord inequalities for test spectra; its floating-point threshold calculations are supplemental only. The complete proof above is algebraic and valid for all \(m\ge2\) and all finite dimensions, independently of finite tests.

As a rational witness, take \(m=2\), \(H=\operatorname{diag}(4,1)\), and initial gradient \(g=(1/4,1)^T\). Then \(\alpha=17/20\) and

\[
\frac{\|g_2\|^2}{\|g\|^2}=
\frac{19521}{10000}>1.
\]

Numerical one-variable optimization (not rigorous certified brackets) gives \(\kappa_2\approx3.442815869\), \(\kappa_3\approx2.893404938\), \(\kappa_4\approx2.657498972\), \(\kappa_8\approx2.334440483\), and \(\kappa_{16}\approx2.178028724\).

## Relationship to prior work

Li and Wang's 2026 analysis of cyclic steepest descent develops two-spectral recurrence formulas and long-run convergence behavior. The two-point expression here is compatible with that setting. The additional conclusions established here concern *all finite-dimensional spectra*, exact worst-case endpoint realization for each fixed matrix, a uniform cycle-boundary safety transition, and the strictly decreasing asymptotic transition \(\kappa_m\to2\). Classical cyclic Barzilai–Borwein literature studies convergence and efficiency of reused step lengths; it does not directly supply this particular uniform gradient-norm threshold in the inspected portions. This statement concerns a different metric and update horizon from repeated exact-line-search steepest descent, one-step Barzilai–Borwein objective descent, and stagewise-safe Richardson iteration.

## Limitations

The claim is restricted to exact Cauchy initialization followed by an unchanged positive step for exactly \(m\ge2\) updates on a fixed SPD quadratic. It does not establish monotonicity at every *internal* step, a global objective safety frontier, a global optimal iteration count, or robustness to rounding or noisy gradients. The numerical thresholds are illustrative and do not replace the implicit exact characterization. A matching unindexed analysis of cyclic-step worst-case gradients could affect historical priority; no independent validation has been performed.

## References

1. Y. Li and Q. Wang, *Cyclic steepest descent is R-superlinearly convergent for almost every initialization on two-spectrum quadratics*, arXiv:2610.15335v1, 2026. https://arxiv.org/abs/2610.15335
2. Y.-H. Dai, W. W. Hager, K. Schittkowski and H. Zhang, *The cyclic Barzilai–Borwein method for unconstrained optimization*, IMA Journal of Numerical Analysis 26 (2006), 604–627. https://doi.org/10.1093/imanum/drl006
3. M. P. Friedlander, M. A. Saunders and M. H. Wright, *A gradient method with retards and generalizations*, SIAM Journal on Optimization (1999). https://pages.cs.wisc.edu/~swright/726/handouts/retard.pdf
