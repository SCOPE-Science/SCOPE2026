# Sharp one-particle survival floor for a binomial-adjusted tau-leap

## Finding

For the one-particle linear death reaction with rate constant \(\lambda>0\), extend the propensity to all integers by \(a(x)=\lambda\max\{x,0\}\). In the binomial-adjusted \(\theta\)-trapezoidal tau-leap, with \(1/2\le\theta<1\), the exact probability of retaining one particle after a step of length \(h\) is, for \(t=\lambda h\),
\[
s_\theta(t)=e^{-t}+e^{-(1-1/(2\theta))t}-e^{-\theta t}.
\]
For \(n\) equal steps the retention probability is \(s_\theta(t)^n\). At any fixed physical time \(T>0\), taking \(h=T/n\) gives
\[
\lim_{n\to\infty}s_\theta(\lambda T/n)^n
=e^{-\lambda T(2-\theta-1/(2\theta))}\ne e^{-\lambda T}.
\]
At \(\theta=1/2\), the survival probability has a unique global minimum of \(3/4\) at \(t=2\log 2\) and increases to \(1\) as \(t\to\infty\). In contrast, the unadjusted method under the same extension has exact one-particle survival \(e^{-t}\) at every finite step.

## Assumptions and scope

Start at \(x=1\) in the reaction \(S\to\varnothing\). Apply the update from Definition 3 of Scott, McCallum and Foster [1] with the clipped propensity just specified, fixed \(\theta\), independent fresh draws per step, and no added rejection, truncation or critical-event handling. The state output is \(x-Q\) for a nonnegative reaction count \(Q\). The same propensity extension applies to the comparison with Definition 2 of [1]. Survival here is the event \(\{x=1\}\), not a statement for arbitrary initial states. Negative counts are possible after an accepted Poisson burst, but nonpositive states are absorbing. The clipping is part of this test problem, not asserted to be specified by [1].

## Proof

Set \(\alpha_1=1/(2\theta)\) and \(\alpha_2=1/(2\theta)-1+\theta>0\); thus \(\alpha_1-\alpha_2=1-\theta>0\). At state one, the predictor is \(N\sim\mathrm{Poisson}(\theta t)\). If \(N=0\), the predicted propensity is \(\lambda\), and the nondegenerate branch adds a Poisson count of mean \((1-\theta)t\). Its contribution to \(\Pr(Q=0)\) is \(e^{-\theta t}e^{-(1-\theta)t}=e^{-t}\).

For \(N\ge1\) the predicted propensity is zero, so the adjusted reaction count is \(\mathrm{Binomial}(N,p_0)\) with
\[
p_0=\frac{1-1/(2\theta)}{\theta}\in[0,1].
\]
The unconditional contribution from this branch to zero reactions is
\[
\sum_{k\ge1}e^{-\theta t}\frac{(\theta t)^k}{k!}(1-p_0)^k
=e^{-\theta p_0t}-e^{-\theta t}.
\]
Adding the two terms proves the one-step formula. States never increase, and there is no return to one after a departure. The survival probability after successive equal steps is therefore the product of the identical one-step probabilities.

At zero, \(s_\theta(t)=1-c_\theta t+O(t^2)\) with \(c_\theta=2-\theta-1/(2\theta)\). On \([1/2,1]\), the minimum of \(\theta+1/(2\theta)\) is \(\sqrt 2\) by AM–GM and its maximum is \(3/2\) by convexity and the endpoint values. Thus \(1/2\le c_\theta\le2-\sqrt2<1\). Taking logarithms with \(t=\lambda T/n\) yields the stated limit, distinct from the exact death process. At \(\theta=1/2\), the substitution \(u=e^{-t/2}\) gives \(s_{1/2}(t)=1-u+u^2=3/4+(u-1/2)^2\). The unique minimum has \(u=1/2\); for larger \(t\), \(u\) decreases to zero and the square increases to \(1/4\).

For the unadjusted update, \(N\ge1\) already rules out survival because the predictor count is retained. On \(N=0\), survival requires the second Poisson count to vanish. This gives \(e^{-t}\) as above, and multiplication gives \(e^{-\lambda T}\) after any partition of \(T\). This comparator need not preserve nonnegativity or the full physical distribution.

## Verification

Run `python verify.py` with Python's standard library. The checker compares the one-step expression with a truncated Poisson sum and checks sampled first-order rates, powers at fixed physical time, the midpoint identity and lower bound, and the unadjusted survival formula. It does not construct a transition matrix. The proof above, not the numerical checks, establishes the identities, the minimizer and the limits for all parameters in scope.

## Relationship to prior work and limitations

Scott, McCallum and Foster [1] introduce the correction in Definition 3 and analyze weak local error, including degenerate low-count cases, in Theorems 2–3 and Appendix A. The separate local weak-order law [4] also covers the exact first-order coefficient: in the accumulated-death coordinate \(j=1-x\), apply its first regime at \(a_0=\lambda\), \(a_j=0\) for \(j\ge1\), and \(f(j)=\mathbf 1_{\{j=0\}}\). This gives \(s_\theta(\lambda h)-e^{-\lambda h}=\lambda h[1-(2-\theta-1/(2\theta))]+O(h^2)\), which also yields the refinement limit by the no-return argument. Neither the first-order coefficient nor that limit is claimed as a distinct novelty. The additional statements here are the exact finite-step survival law under clipping, its sharp midpoint floor and large-step recovery, and the exact unadjusted survival contrast. The observed failure occurs at a fixed one-particle boundary, rather than under large-volume scaling as in [2]; [3] concerns a different tau-leaping adjustment. For \(\theta>1/2\) the one-step survival tends instead to zero as \(t\to\infty\). No statement about general reaction networks or typical large-population behavior follows from this example.

## References

1. M. Scott, S. McCallum and J. Foster, *A binomial-adjusted \(\theta\)-trapezoidal tau-leaping method for chemical kinetic systems*, arXiv:2611.16975v1, https://arxiv.org/abs/2611.16975.
2. Y. Hu, T. Li and B. Min, *A weak second order tau-leaping method for chemical kinetic systems*, *Journal of Chemical Physics* **135**, 024113 (2011), https://doi.org/10.1063/1.3609119.
3. Y. Cao, D. T. Gillespie and L. R. Petzold, *Avoiding negative populations in explicit Poisson tau-leaping* (2005), https://escholarship.org/uc/item/04x399h1.
4. *A sharp three-regime local weak-order law for binomial-adjusted tau leaping*, Resultary, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-sharp-three-regime-local-weak-order-law-for-binomial-adjusted--8a00c845f4a5.
