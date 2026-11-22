# Sharp high-conditioning two-step objective gain for Cauchy-seeded curvature feedback

## Finding

The first curvature-feedback step of the gradient method in [1] can erase the benefit of an exact-line-search start. For the two-dimensional positive-definite quadratic defined below, let \(F_j\) denote the objective gap after \(j\) gradient updates and let \(\kappa>1\) be the Hessian condition number. Then, uniformly over every nonstationary starting state with both spectral components present,

\[
0\le \frac{F_2}{F_0}<\kappa.
\]

The growth coefficient is asymptotically sharp in the strongest worst-start sense:

\[
\boxed{\lim_{\kappa\to\infty}\frac1\kappa\sup_{x_0}\frac{F_2}{F_0}=1.}
\]

In particular the two-step objective need not decrease: with \(\kappa=9\) and initial squared-gradient-mode ratio \(r=1/63\),

\[
\frac{F_1}{F_0}=\frac7{71},\qquad
\frac{F_2}{F_1}=\frac{197}{9},\qquad
\boxed{\frac{F_2}{F_0}=\frac{1379}{639}>1.}
\]

This is a sharp leading coefficient as \(\kappa\to\infty\), **not** an assertion that the supremum equals \(\kappa\) for fixed \(\kappa\).

## Assumptions and scope

Work in exact real arithmetic with \(f(x)=\tfrac12 x^{\mathsf T}Hx\), \(H=\operatorname{diag}(1,\kappa)\), and \(\kappa>1\). An arbitrary translation and positive scaling of both curvatures give the equivalent result. Assume \(g_0=Hx_0=(u,v)\) with \(u v\ne0\), and write \(r=v^2/u^2>0\). Initialize the scheme of [1] using a Cauchy, i.e. exact-line-search, seed

\[
\alpha_0=\frac{g_0^{\mathsf T}g_0}{g_0^{\mathsf T}Hg_0}=
\frac{1+r}{1+\kappa r},\qquad
x_1=x_0-\alpha_0g_0.
\]

Then compute the first secant local curvature \(c_1=\|H(x_1-x_0)\|_2/\|x_1-x_0\|_2\) and take the first running-min/running-max feedback step of [1],

\[
\alpha_1=\frac{2}{\min\{c_1\}+\max\{c_1\}}=\frac1{c_1},\qquad
x_2=x_1-\alpha_1 Hx_1.
\]

Only the first two updates are claimed; this theorem does not assert a finite-time bound for all subsequent running-estimator steps. The first feedback step coincides with the previously known geometric-mean spectral/Barzilai--Borwein step [2,3]; its formula is prior work, not a new algorithm.

## Proof

Because \(x_1-x_0=-\alpha_0g_0\), the first measured curvature and second stepsize are exactly

\[
c_1=\sqrt{\frac{1+\kappa^2r}{1+r}},\qquad
\alpha_1=\sqrt{\frac{1+r}{1+\kappa^2r}}=:a.
\]

Consequently \(1/\kappa<a<1\). The first line-search gradients satisfy

\[
g_1=\frac{\kappa-1}{1+\kappa r}(ru,-v),
\]

and direct evaluation of the two objective ratios yields

\[
\frac{F_1}{F_0}=\frac{(\kappa-1)^2r}{(1+\kappa r)(\kappa+r)},\qquad
\frac{F_2}{F_1}=\frac{\kappa r(1-a)^2+(1-\kappa a)^2}{1+\kappa r}.
\]

Hence the complete two-update ratio, valid for every \(\kappa>1\) and \(r>0\), is

\[
\boxed{\mathcal R(\kappa,r)=\frac{F_2}{F_0}=
\frac{(\kappa-1)^2r\big[\kappa r(1-a)^2+(1-\kappa a)^2\big]}
{(1+\kappa r)^2(\kappa+r)},\quad
a^2=\frac{1+r}{1+\kappa^2r}.}
\]

For the upper bound, \(0<a<1\) gives \((1-a)^2<1\), while \(\kappa a>1\) gives \((1-\kappa a)^2<\kappa^2a^2\). Therefore

\[
\mathcal R(\kappa,r)
<\frac{(\kappa-1)^2\big(\kappa r^2+\kappa^2r a^2\big)}{(1+\kappa r)^2(\kappa+r)}
<\frac{\kappa^2(\kappa r^2+1+r)}{(1+\kappa r)^2(\kappa+r)},
\]

where the last inequality uses \(\kappa^2r a^2=\kappa^2r(1+r)/(1+\kappa^2r)<1+r\). The remaining denominator margin is explicitly

\[
(1+\kappa r)^2(\kappa+r)-\kappa(\kappa r^2+1+r)
=r(2\kappa^2-\kappa+1)+r^2(\kappa^3-\kappa^2+2\kappa)+\kappa^2r^3>0.
\]

Each coefficient is positive for \(\kappa\ge1\), so \(\mathcal R(\kappa,r)<\kappa\). Nonnegativity is immediate because each \(F_j\) is nonnegative and \(F_0>0\).

To prove sharpness of the leading factor, select the admissible family \(r=\kappa^{-3/2}\). The exact formulas give

\[
\frac{F_1}{F_0}\sim\kappa^{-1/2},\qquad
\alpha_1\sim\kappa^{-1/4},\qquad
\frac{F_2}{F_1}\sim\kappa^{3/2},\qquad
\mathcal R(\kappa,\kappa^{-3/2})\sim\kappa.
\]

The upper bound and this explicit lower-bound family squeeze the scaled supremum to one. For the rational example, substitute \(\kappa=9\), \(r=1/63\), obtaining \(\alpha_0=8/9\) and \(\alpha_1=2/3\); the displayed rational objective ratios follow exactly. This completes the proof.

## Verification

The standalone Python verifier `artifacts/verify_two_step.py` uses symbolic algebra for the ratio reduction and positivity-margin polynomial, `fractions.Fraction` for the exact gain witness, 5,000 reproducibly seeded numerical tests of the actual two updates, and a high-conditioning sequence checking the limiting coefficient. Run with `python artifacts/verify_two_step.py` in an environment with Python 3 and SymPy. The verified output is in `artifacts/verification.txt`. The proof above is independent of the numerical tests.

## Relationship to prior work

Wang et al. [1] introduce the running local-curvature estimators and asymptotic stepsize objective, but do not state a condition-number-sharp *two-update objective ratio* from a Cauchy seed. Dai, Huang and Liu [2] explicitly include the geometric-mean BB step in their spectral family, crediting Dai, Al-Baali and Yang [3] for that stepsize. This work does not claim priority for the update rule or asymptotic convergence theory. A published exact one-step BB-interval analysis [4] establishes sharp \((\kappa-1)^2\) amplification relative to the **immediately preceding** iterate, including after a Cauchy seed; it does not give the tight two-step *initial-to-final* \(\kappa\) leading coefficient proved here. The endpoint-mode example in [5] addresses stepsize identification rather than two-step objective amplification. A separate two-mode study [6] obtains a different initial-to-final coefficient for a different adaptive rule. These comparisons concern mathematical implications, not title similarity.

## Limitations

The claim is only for two-dimensional SPD quadratics, exactly initialized by a first Cauchy step, followed by the first local-curvature feedback step. It is a high-conditioning sharp leading coefficient, not an exact optimizer for each fixed condition number, and it does not bound the total gain over arbitrary numbers of subsequent steps. The geometric-mean BB update predates [1]. The complete 2015 analysis [3] was not accessible for theorem-level inspection, so historical priority of the particular two-step sharp coefficient remains a qualified risk. No independent validation has been performed.

## References

1. Y. Wang, L. Ballotta, R. Carli, X. Cao, L. Schenato, *Pursuing Optimal Stepsize in Adaptive Gradient-Based Quadratic Optimization*, arXiv:2608.03546v1, first public 2026-08-04. https://arxiv.org/abs/2608.03546
2. Y.-H. Dai, Y. Huang, X.-W. Liu, *A Family of Spectral Gradient Methods for Optimization*, Computational Optimization and Applications 74 (2019), 43--65. Open manuscript https://optimization-online.org/wp-content/uploads/2018/05/6628.pdf
3. Y.-H. Dai, M. Al-Baali, X. Yang, *A Positive Barzilai--Borwein-Like Stepsize and an Extension for Symmetric Linear Systems*, Numerical Analysis and Optimization, NAO-III, pp. 59--75 (2015). https://doi.org/10.1007/978-3-319-17689-5_3
4. *Sharp objective-monotonicity frontier for Barzilai--Borwein interval steps*, publicly available mathematical result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-bb-interval-objective-monotonicity-frontier--7866f4762b53
5. *Spectral-persistence counterexamples and a repair for AdOGD*, publicly available mathematical result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/9/17/SCOPE-adogd-spectral-persistence-counterexamples--5f12814867fa
6. *Sharp two-mode transient amplification for CG_AOS after exact initialization*, publicly available mathematical result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/9/17/SCOPE-cgaos-two-mode-transient-amplification--69464fd3db0c
