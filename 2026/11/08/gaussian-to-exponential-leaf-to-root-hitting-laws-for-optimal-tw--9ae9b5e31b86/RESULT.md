# Exact deadline-optimal root hitting on complete two-choice trees

## Finding

Fix integers \(b\ge2\) and \(h\ge1\). Start at any leaf of the complete rooted \(b\)-ary tree of height \(h\). At each discrete step two neighbors are offered independently and uniformly, with replacement, and the controller chooses one of them. Write \(T_{b,h}\) for the time to hit the root under the parent-first rule: take the parent whenever it is offered, breaking ties among children arbitrarily. This single policy maximizes the root-hitting probability by **every** deadline among all history-dependent and randomized policies. In particular, the result is stochastic optimality, not just minimization of the mean.

The exact optimal finite-height law can be evaluated by the following continued fraction. Set \(p=(2b+1)/(b+1)^2\), \(q=b^2/(b+1)^2\), and for \(0\le z\le1\) define
\[
J_h(z)=z,\qquad J_i(z)=\frac{zp}{1-zqJ_{i+1}(z)}\quad(i=h-1,\ldots,1).
\]
Then \(\mathbb E[z^{T_{b,h}}]=\prod_{i=1}^hJ_i(z)\). For an integer deadline \(t\ge0\), the coefficient of \(z^t\) in \((1-z)^{-1}\prod_{i=1}^h J_i(z)\), expanded at zero, is the largest achievable probability of reaching the root by \(t\). This radial calculation uses only the height and degree; it does not enumerate the vertices or policies.

## Scope

Offers are freshly sampled at every step, uniformly at the current vertex and with replacement. There is no holding action. The root is treated as absorbing only when defining the first hitting time. The policy can use the full observed past and private randomization. The result concerns complete regular rooted trees and makes no assertion for arbitrary trees or nonuniform proposals.

## Proof

For a horizon \(t\), let \(u_i(t)\) be the maximal success probability from depth \(i\). Symmetry makes it independent of the vertex of that depth. To reach the root from depth \(i+1\) a path must first visit depth \(i\). Conditional on that first visit and on the past, the continuation has fresh offers and can do no better than \(u_i(t)\): the remaining horizon is at most \(t\). Thus \(u_{i+1}(t)\le u_i(t)\). At any interior depth \(i\) and any remaining positive horizon, Bellman's recursion selects the offered neighbor giving the larger value at the next step. A parent leads to depth \(i-1\) and a child to \(i+1\), so the parent is always at least as good. The leaf step is forced. Backward induction establishes optimality for all policies at every deadline using the very same parent-first rule.

Under this rule the depth process moves inward with probability \(p=1-(b/(b+1))^2\) and outward with probability \(q\) at interior depths, and inward with probability one at the leaf. For the first time to descend from level \(i\) to \(i-1\), an immediate inward step contributes \(zp\) to the generating function. An outward step instead requires a return to \(i\) and then an independent fresh attempt at the downward crossing. Thus \(J_i=zp+zqJ_{i+1}J_i\), with \(J_h=z\). The denominators are positive for \(0\le z\le1\) because \(q<1\) and each \(J_j\le1\). Strong Markov at the successive first downward crossings gives independent durations, so the generating functions multiply. Cumulative probabilities are the coefficients obtained by multiplying by \((1-z)^{-1}\).

## Earlier mean and fluctuation laws

The earlier regular-tree result [1] for an arbitrary fixed number of offers includes the following formulas as its two-offer case. With \(r=q/p\), the exact leaf-to-root mean is
\[
\mathbb E T_{b,h}=\frac{h}{p-q}-\frac{2pq}{(p-q)^2}(1-r^h).
\]
For \(b=2\) this is \(9h-40(1-(4/5)^h)\), with \((T_{2,h}-9h)/\sqrt{720h}\Rightarrow N(0,1)\). For fixed \(b\ge3\) the mean is asymptotic to \(2pq\,r^h/(q-p)^2\) and the time divided by its mean converges to a standard exponential. Neither that mean formula nor the drift-dependent fluctuation laws are new claims here. The finite generating function is included as an exact computational form of the all-deadline optimum, not as a new general birth–death generating-function method.

The general expected-hitting-time strategy framework of Georgakopoulos, Haslegrave, Sauerwald and Sylvester [2] orders neighbors by their expected-time values. Their maximum-degree-three and infinite regular-tree discussion already distinguishes the inward and outward biases. The finite-deadline assertion here instead orders optimal success probabilities simultaneously and covers every adaptive randomized competitor.

## Reproducibility

The accompanying source program `verify.py` checks parent-first probabilities against exact finite-horizon Bellman maximization on labeled trees and compares the continued fraction with a finite absorbing-chain linear system. Its additional mean checks concern the prior formulas. Finite diagnostics are not a substitute for the all-height policy proof above.

## References

1. *A sharp choice threshold and contrasting root-hitting laws on regular trees*, Resultary record, 2026-11-02, https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-a-sharp-choice-threshold-and-contrasting-root-hitting-laws-on-re--5d9f1265df29.
2. A. Georgakopoulos, J. Haslegrave, T. Sauerwald and J. Sylvester, *The Power of Two Choices for Random Walks*, arXiv:1911.05170, especially Proposition 3.4 and §7.1.
