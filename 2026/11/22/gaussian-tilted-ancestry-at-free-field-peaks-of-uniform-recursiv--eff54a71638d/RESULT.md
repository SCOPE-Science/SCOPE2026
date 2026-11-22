# Gaussian-tilted ancestry at free-field peaks of uniform recursive trees

## Finding

Let \(T_n\) be the uniform random recursive tree with root \(1\) and independent choices \(\operatorname{parent}(j)\sim\operatorname{Unif}\{1,\ldots,j-1\}\) for every \(2\le j\le n\). Label each edge independently with a standard normal \(\xi_e\), and write \(\eta(v)=\sum_{e\in[1,v]}\xi_e\) for the root-pinned Gaussian free field. Select the almost surely unique maximizer \(v_n\) of \(\eta\) among all vertices; let \(K_n\) denote its depth and \(\xi_{n,i}\) its root-to-maximizer increments, in ancestral order.

**Theorem (extremal ancestral law).** Put \(c=\sqrt e\). Under the joint law of tree and Gaussian marks, as \(n\to\infty\),

\[
\frac{K_n}{\log n}\xrightarrow{\mathbb P}c,\qquad
\frac1{K_n}\sum_{i=1}^{K_n}\delta_{\xi_{n,i}}
\xrightarrow{\mathbb P,\mathrm{weak}}N(1,1),
\]

\[
\frac1{\log n}\max_{0\le j\le K_n}
\left|\sum_{i=1}^j\xi_{n,i}-j\right|
\xrightarrow{\mathbb P}0,\qquad
\frac1{K_n}\sum_{i=1}^{K_n}\xi_{n,i}^2\xrightarrow{\mathbb P}2.
\]

In particular, the fraction of negative ancestral increments converges in probability to \(\Phi(-1)\), strictly between zero and one, rather than the unbiased fraction \(1/2\). Also the rescaled ancestral field profile converges uniformly to the straight line \(s\mapsto cs\):

\[
\sup_{s\in[0,1]}
\left|\frac{\eta(v_n(\lfloor sK_n\rfloor))}{\log n}-cs\right|
\xrightarrow{\mathbb P}0,
\]

where \(v_n(j)\) is the depth-\(j\) ancestor of \(v_n\). For all sufficiently large \(n\), the event \(K_n=0\) can be assigned any arbitrary empirical measure; its probability tends to zero.

## Assumptions and scope

All probabilities are **annealed**, meaning they include the random tree and its independent Gaussian edge labels. There are no restrictions on hidden tree randomness, and all vertices, not only leaves, are eligible for maximization. The theorem uses the previously published law \(\max_v\eta(v)/\log n\to c\) in probability for this same model (Angel–Goldschmidt–Michaeli, Corollary 13). We prove the additional extremal-depth and whole-ancestry assertions below. Neither a quenched conclusion conditional on \(T_n\) nor a second-order law is asserted.

## Proof

**1. Exact exponential-spine identity.** Let \(\xi_{v,1},\ldots,\xi_{v,k}\) be the marks on the root-to-\(v\) path if \(|v|=k\). For every nonnegative measurable functional \(F\) on finite marked paths, Gaussian tilting gives

\[
\mathbb E_{\xi}\!\left[e^{\eta(v)}F(k,\xi_{v,1},\ldots,\xi_{v,k})\mid T_n\right]
=e^{k/2}\,\mathbb E F(k,G_1,\ldots,G_k),
\]

where \(G_i\) are independent \(N(1,1)\) variables. The random tree's expected depth profile has generating polynomial

\[
\mathbb E\sum_{v\in T_n}z^{|v|}
=\prod_{t=1}^{n-1}\left(1+\frac zt\right).
\tag{1}
\]

Indeed, at birth time \(j\), the expected total profile increases by its former expectation multiplied by \(z/(j-1)\); starting at one proves (1) exactly. Set \(c=e^{1/2}\) and

\[
C_n=\prod_{t=1}^{n-1}\left(1+\frac ct\right)
=\frac{\Gamma(n+c)}{\Gamma(1+c)\Gamma(n)}
\sim\frac{n^c}{\Gamma(1+c)}.
\tag{2}
\]

The probability generating function of the depth under the normalized exponential-size-biased path law is

\[
\frac{\prod_{t=1}^{n-1}(1+cz/t)}{C_n}
=\prod_{t=1}^{n-1}\left(1+\frac{c(z-1)}{t+c}\right).
\tag{3}
\]

Consequently, for every such \(F\), the **exact** many-to-one formula is

\[
\boxed{\ \mathbb E\sum_{v\in T_n}e^{\eta(v)}F(|v|,\xi_{v,1},\ldots,\xi_{v,|v|})
=C_n\,\mathbb E F(K,G_1,\ldots,G_K).\ }
\tag{4}
\]

Here \(K=\sum_{t=1}^{n-1}B_t\), where the \(B_t\) are independent Bernoulli variables with means \(c/(t+c)\), and the independent \(G_i\sim N(1,1)\) are independent of \(K\). This is an equality of joint marked-path measures, not merely an equality of generating functions.

**2. Exponentially small spine deviations.** Write \(L=\log n\). From the Bernoulli representation,

\[
\mathbb E K=cL+O(1),\qquad\operatorname{Var}(K)\le cL+O(1).
\]

Bernstein's inequality, or the direct Chernoff bound for a sum of independent Bernoulli variables, yields for every fixed \(\delta>0\) a positive \(a_1(\delta)\) such that

\[
\Pr(|K-cL|>\delta L)\le 2e^{-a_1(\delta)L}
\]

for all sufficiently large \(n\). Conditional on \(K=k\), the \(G_i\) are iid \(N(1,1)\). Restricting first to \(cL/2\le k\le2cL\), Hoeffding's inequality applies to the empirical mean of any fixed bounded measurable \(f(G_i)\), and Gaussian exponential-martingale maximal inequalities give

\[
\Pr\left(\max_{0\le j\le k}\left|\sum_{i=1}^j(G_i-1)\right|>\delta L\mid K=k\right)
\le2\exp\left(-\frac{\delta^2L^2}{2k}\right)
\le2e^{-\delta^2L/(4c)}.
\tag{5}
\]

Finally, \(G_i^2\) has an exponential moment in a neighborhood of zero, so the ordinary Chernoff method gives exponentially small deviations of its sample mean from \(\mathbb E G_i^2=2\). Therefore for every fixed \(\delta>0\) and bounded \(f\) there exist \(A<\infty\), \(a>0\), depending on \(\delta,f\) but not on \(n\), such that the spine probability of **any** of the following failures is at most \(Ae^{-aL}\): depth differs from \(cL\) by more than \(\delta L\); empirical \(f\)-average differs from \(\mathbb Ef(N(1,1))\) by more than \(\delta\); the partial-sum deviation in (5) exceeds \(\delta L\); the empirical squared-mark mean differs from \(2\) by more than \(\delta\). Let their union be \(\mathcal B_n\).

**3. No high-field vertex has anomalous ancestry.** Fix \(\varepsilon>0\) and put \(b=c-\varepsilon\). On the event that \(\eta(v)\ge bL\), the exponential weight satisfies \(e^{\eta(v)}\ge n^b\). Formula (4) and a first-moment bound therefore give

\[
\Pr\bigl(\exists v:\eta(v)\ge bL,\ \operatorname{path}(v)\in\mathcal B_n\bigr)
\le e^{-bL}C_n\,\Pr_{\mathrm{spine}}(\mathcal B_n)
\le C n^{\varepsilon-a}.
\tag{6}
\]

Choose any \(0<\varepsilon<a\). The right-hand side vanishes. This is a simultaneous statement about **all** vertices above the fixed near-maximal level, not an assertion about a randomly selected size-biased vertex alone.

**4. Transfer to the actual maximizer.** Angel–Goldschmidt–Michaeli (2026, Corollary 13) prove for exactly the current tree/Gaussian model that \(M_n=\max_v\eta(v)\) obeys \(M_n/L\to c\) (indeed almost surely under the natural growth coupling). Hence \(\Pr(M_n\ge(c-\varepsilon)L)\to1\), and (6) applies to the actual maximizer \(v_n\). Each fixed bounded Lipschitz \(f\) consequently has the stated empirical limit in probability; a countable convergence-determining bounded-Lipschitz family yields weak convergence in probability of the empirical probability measures. Applying the same reasoning to the squared marks and the path maximal inequality proves the remaining assertions. The uniform rescaled linear profile follows from these two limits by \(j/L=(j/K_n)(K_n/L)\). Weak convergence plus continuity of the \(N(1,1)\) distribution at zero gives the negative-step fraction \(\Phi(-1)\). This finishes the proof.

## Verification

The separate standalone \(checker.py\) exactly enumerates all recursive parent arrays up to eight vertices, checks polynomial identity (1) coefficient by coefficient with rational arithmetic, checks (3) and the weighted polynomial equality symbolically, and checks the first seven Gaussian tilt moments. Executing the packaged script reports 105 passing exact identities. These are **finite algebraic checks only**: the infinite-limit proof is the displayed concentration and maximal-displacement argument, not the enumerations.

## Relationship to prior work

Angel, Goldschmidt and Michaeli (arXiv:2611.18353, first posted 2026-11-13) establish the Gaussian free-field maximum's first-order speed \(c=\sqrt e\) and heuristically suggest a depth near \(c\log n\), but do not state the joint extremal-depth, empirical-increment or uniform ancestral profile limits proved here. The classical many-to-one/spinal change of measure is pre-existing probability theory and is explicitly not claimed as new. Mallein (arXiv:1605.08292) studies genealogical separation and the path of extremal particles in **fixed-generation** Galton–Watson branching random walks, rather than the growing **fixed-population** recursive-tree model with random depth and the exact tilted Bernoulli depth law (3). Jagannath (arXiv:1509.07527) studies overlaps and the Gibbs measure of a Gaussian branching random walk on a binary tree. Those conclusions are scientifically related but do not directly state these particular recursive-tree ancestral empirical limits.

## Limitations

The maximum-speed input is cited from prior work, not independently reproved. This is an annealed theorem; conditioning on a particular realization of the recursive tree is not covered. The result gives first-order path law, not a rate for the actual maximizer's convergence, fluctuations around the line, a limiting extremal point process, or direct cover-time path statistics. Broad general branching-random-walk spine or path-localization results could subsume the assertion after a nontrivial specialization; that historical-priority possibility has not been completely excluded. No independent mathematical audit has been performed.

## References

1. O. Angel, C. Goldschmidt and P. Michaeli, *Cover times of random recursive trees and linear preferential attachment trees*, arXiv:2611.18353 (first public version 2026-11-13), especially Section 2 and Corollary 13. https://arxiv.org/abs/2611.18353
2. B. Mallein, *Asymptotic of the maximal displacement in a branching random walk*, arXiv:1605.08292 (2016), Sections 1, 2 and 4. https://arxiv.org/abs/1605.08292
3. A. Jagannath, *On the overlap distribution of branching random walks*, arXiv:1509.07527 (2015). https://arxiv.org/abs/1509.07527
4. J. D. Biggins, *The growth and spread of the general branching random walk*, Annals of Applied Probability **5** (1995), 1008–1024 (classical branching-random-walk maximal-speed theory; used in Ref. 1).
