# Sharp one-particle survival floor and inconsistent zero-step limit for binomial-adjusted tau-leaping

## Finding

For one-molecule linear death with the propensity set to zero at every nonpositive integer state, the binomial-adjusted \(\theta\)-trapezoidal tau-leap has the exact one-step survival probability

\[
s_\theta(t)=e^{-t}+e^{-(1-1/(2\theta))t}-e^{-\theta t},\qquad t=\lambda h,\quad \tfrac12\le\theta<1.
\]

Its \(n\)-step probability of still having one molecule is \(s_\theta(\lambda h)^n\). For each finite physical time \(T>0\), the refined-step limit with \(h=T/n\) is

\[
\lim_{n\to\infty}s_\theta(\lambda T/n)^n
=\exp\!\left(-\lambda T\left(2-\theta-\frac1{2\theta}\right)\right)
\ne e^{-\lambda T}.
\]

At the natural midpoint setting \(\theta=1/2\) the exact survival law simplifies to \(s_{1/2}(t)=1-e^{-t/2}+e^{-t}\), with a **unique global minimum** of \(3/4\) at \(t=2\log 2\), increasing back toward \(1\) as \(t\to\infty\). In contrast, the unadjusted \(\theta\)-trapezoidal tau-leap has exact one-molecule survival probability \(e^{-t}\) for every finite step, so the binomial adjustment destroys exact survival on this test problem.

## Assumptions and scope

Consider one reaction \(S\to\varnothing\) at rate \(\lambda>0\) with integer state \(x\) and propensity \(a(x)=\lambda\max\{x,0\}\). Start at \(x=1\) and apply Definition 3 of Scott--McCallum--Foster [1] with a constant \(\theta\in[1/2,1)\), step length \(h>0\), independent fresh random draws each step, predictor count \(N\sim\mathrm{Poisson}(\theta \lambda h)\), and output \(x-Q\). When the tentative predictor state \(1-N\) is nonpositive, its propensity is zero; no additional rejection, truncation, or critical-event special treatment is imposed. The same clipped propensity is used in the unadjusted Definition 2 comparison. The event called survival is exactly \(\{x=1\}\), not the event \(\{x>0\}\) from any other starting state.

Both schemes are allowed to generate negative counts after an accepted Poisson reaction burst; the clipped propensity makes nonpositive states absorbing. The conclusions concern the numerical survival probability from the one-particle initial state, not general moment convergence, physical nonnegativity of every path, or arbitrary reaction networks. The source [1] is concerned with local error and large-count assumptions; this boundary case is outside its favorable count conditions.

## Proof

Set \(t=\lambda h\), \(\alpha_1=1/(2\theta)\), and \(\alpha_2=1/(2\theta)-1+\theta\). Notice \(\alpha_1-\alpha_2=1-\theta>0\) and \(\alpha_2>0\). We compute the probability that the corrected total reaction count \(Q\) is zero, conditional on the predictor count \(N\).

If \(N=0\), the predicted state remains \(1\); the nondegenerate branch adds \(P\sim\mathrm{Poisson}((1-\theta)t)\), so \(\Pr(Q=0\mid N=0)=e^{-(1-\theta)t}\). Its unconditional contribution is \(e^{-\theta t}e^{-(1-\theta)t}=e^{-t}\).

If \(N\ge1\), the predicted state is nonpositive and the reaction propensity there is zero. The binomial branch therefore draws \(Q\sim\mathrm{Binomial}(N,p_0)\), where

\[
p_0=\frac{1-1/(2\theta)}{\theta}=\frac{2\theta-1}{2\theta^2}.
\]

For \(\theta\in[1/2,1)\) this lies in \([0,1]\). The unconditional contribution for \(N\ge1\) is obtained from the Poisson probability-generating function:

\[
\begin{aligned}
\sum_{k\ge1}e^{-\theta t}\frac{(\theta t)^k}{k!}(1-p_0)^k
&=e^{-\theta t}\left(e^{\theta t(1-p_0)}-1\right)\\
&=e^{-\theta p_0t}-e^{-\theta t}.
\end{aligned}
\]

Since \(\theta p_0=1-1/(2\theta)\), the two contributions sum to the claimed \(s_\theta(t)\).

Every generated count \(Q\) is nonnegative, so the chain starting at \(1\) cannot return to \(1\) after an exit; at all nonpositive states the propensity vanishes and the chain stays put. The Markov property therefore gives \(\Pr(X_n=1)=s_\theta(\lambda h)^n\).

Expanding at zero yields \(s_\theta(t)=1-c_\theta t+O(t^2)\) with \(c_\theta=2-\theta-1/(2\theta)\). By AM--GM, \(\theta+1/(2\theta)\ge\sqrt2\), with equality at \(\theta=1/\sqrt2\); its maximum on \([1/2,1]\) is \(3/2\). Hence \(1/2\le c_\theta\le2-\sqrt2<1\), proving the distinct refined-time limit for every permitted \(\theta\).

At \(\theta=1/2\), write \(u=e^{-t/2}\in(0,1)\). Then \(s_{1/2}(t)=1-u+u^2=(u-1/2)^2+3/4\). The unique minimum occurs at \(u=1/2\), i.e. \(t=2\log2\), and the endpoint limits as \(t\downarrow0\) and \(t\to\infty\) both equal \(1\). In the original (unadjusted) Definition 2, if \(N\ge1\), the endpoint reaction count is at least \(N\), hence the state cannot remain \(1\). If \(N=0\), it remains \(1\) precisely when the second independent \(\mathrm{Poisson}((1-\theta)t)\) count is zero. Thus its survival is \(e^{-\theta t}e^{-(1-\theta)t}=e^{-t}\), and consequently \(e^{-\lambda T}\) after any partition of physical time \(T\).

## Verification

The standalone `verify.py` checks the two conditional branches against finite Poisson summations, the exact clipped-state transition matrix on a truncated count grid, the limiting derivative, the three-quarter sharp minimum, and the unadjusted survival identity over multiple parameter values. The analytic argument above, rather than finite enumeration or floating-point tests, proves all quantified conclusions. Run `python verify.py` using the Python standard library.

## Relationship to prior work

Scott, McCallum and Foster [1], Definition 3 and Appendix A, introduce the dependent binomial backtracking correction and derive a generic first-order local weak-error coefficient when a reaction channel is degenerate. Their analysis already identifies a low-count sensitivity and gives a sufficient molecular-count threshold for improved local error. The present result does **not** claim that first-order sensitivity itself is new. It computes a complete finite-step survival semigroup, a sharp global three-quarter survival floor at the common midpoint parameter, the exact incorrect zero-step limit, and an exact per-step contrast with Definition 2; these statements are not supplied by their local bounds. The weak-order analysis of Hu, Li and Min [2] uses large-volume scaling, not this fixed one-molecule boundary. The earlier nonnegative population correction of Cao, Gillespie and Petzold [3] concerns a different tau-leaping rule.

## Limitations

The example is deliberately a low-copy-number boundary case. It does not contradict the conditional large-volume results in [1] or establish typical errors in high-population chemical kinetics. For \(\theta>1/2\), the one-step survival tends to zero as \(t\to\infty\); the sharp \(3/4\) floor and large-step recovery apply specifically to \(\theta=1/2\). The unadjusted comparator may still create negative states; exact one-molecule survival alone is not a guarantee of good full-distribution behavior. Historical novelty is based on the inspected sources, not on a proof that no other equivalent observation exists.

## References

1. M. Scott, S. McCallum and J. Foster, *A binomial-adjusted \(\theta\)-trapezoidal tau-leaping method for chemical kinetic systems*, arXiv:2611.16975v1 (first public version 2026-11-12), https://arxiv.org/abs/2611.16975.
2. Y. Hu, T. Li and B. Min, *A weak second order tau-leaping method for chemical kinetic systems*, Journal of Chemical Physics **135**, 024113 (2011), https://doi.org/10.1063/1.3609119.
3. Y. Cao, D. T. Gillespie and L. R. Petzold, *Avoiding negative populations in explicit Poisson tau-leaping* (2005), https://escholarship.org/uc/item/04x399h1.
