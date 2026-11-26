# A strict-majority parity law and a sharp even-electorate crossover under beta-binomial social influence

## Finding

Let \(\alpha>\beta>0\), let \(\Theta\sim\operatorname{Beta}(\alpha,\beta)\), and, conditionally on \(\Theta\), let \(X_n\sim\operatorname{Binomial}(n,\Theta)\). The stationary strict-majority correctness of the fully mixed binary zealot voter model is
\[
A_n=\Pr\{X_n>n/2\},\qquad p=\mathbb E\Theta=\frac{\alpha}{\alpha+\beta}.
\]
Here a tie is not a correct strict-majority decision. For **all integers \(m\ge1\)**, the even-size sequence is strictly increasing, \(A_{2m+2}>A_{2m}\), but its terms are strictly below both neighboring odd-size accuracies:
\[
A_{2m}<\min\{A_{2m-1},A_{2m+1}\}.
\]
Nevertheless \(A_2<p\) and \(\lim_{m\to\infty}A_{2m}>p\). Thus there is a finite, unique first even electorate strictly exceeding individual correctness; at most one even electorate can tie it. This characterizes the parity obstruction and the finite crossover left unresolved by asymptotic majority guarantees.

In the smallest integer asymmetry with two correct and one incorrect zealot, \((\alpha,\beta)=(2,1)\), exact expressions are
\[
A_{2m}=\frac{3m}{4m+2},\qquad A_{2m+1}=\frac{3m+4}{4m+6}.
\]
Therefore even electorates of sizes \(2,4,6\) underperform \(p=2/3\), size \(8\) ties it, and **size \(10\) is the first even size strictly outperforming it**. Every odd size at least three already outperforms \(p\), an odd-size fact covered by earlier jury theorems.

## Assumptions and scope

For all real \(\alpha>\beta>0\) and each integer \(n\ge1\), \(\Theta\) has density
\[
f_{\alpha,\beta}(u)=\frac{u^{\alpha-1}(1-u)^{\beta-1}}{B(\alpha,\beta)},\quad 0<u<1.
\]
Given \(\Theta=u\), free votes are independent Bernoulli trials with success probability \(u\). Marginally, \(X_n\) has the beta-binomial law
\[
\Pr(X_n=k)=\binom nk\frac{B(\alpha+k,\beta+n-k)}{B(\alpha,\beta)},\qquad 0\le k\le n.
\]
This is precisely the stationary free-voter count law in the fully mixed zealot model of Braha and de Aguiar (2025) when the two fixed-influence parameters are \(\alpha,\beta\). For actual graph-theoretic zealot counts these are positive integers; the result also covers the standard positive-real extension of the stationary count distribution. The electorate size counts **free** voters, not zealots. Inertia does not affect the stationary distribution under the source model's restrictions.

## Proof

Write \(g_n(u)=\Pr(\operatorname{Binomial}(n,u)>n/2)\). Conditioning on \(\Theta\) gives \(A_n=\mathbb E[g_n(\Theta)]\). Elementary conditioning on the last one or two Bernoulli trials yields, for integer \(m\ge1\),
\[
g_{2m-1}(u)-g_{2m}(u)=\binom{2m-1}{m}u^m(1-u)^m,
\]
\[
g_{2m+1}(u)-g_{2m}(u)=\binom{2m}{m}u^{m+1}(1-u)^m.
\]
Both integrands are strictly positive for \(0<u<1\); their beta-mixture expectations prove the adjacent parity dips. More precisely the positive gaps are the displayed binomial coefficients multiplied respectively by \(B(\alpha+m,\beta+m)/B(\alpha,\beta)\) and \(B(\alpha+m+1,\beta+m)/B(\alpha,\beta)\).

Conditioning on two added voters, now at even sizes, gives the **exact** identity
\[
g_{2m+2}(u)-g_{2m}(u)=\frac{\binom{2m}{m}}{m+1}u^{m+1}(1-u)^m[(2m+1)u-m].
\]
The right side can be negative for small \(u\); consequently its beta-mixture positivity cannot be deduced from pointwise binomial monotonicity. Integrating and using the beta mean \(\mathbb E_{\operatorname{Beta}(\alpha+m+1,\beta+m)}[u]=(\alpha+m+1)/(\alpha+\beta+2m+1)\) yields
\[
\boxed{A_{2m+2}-A_{2m}=\frac{\binom{2m}{m}}{m+1}\frac{B(\alpha+m+1,\beta+m)}{B(\alpha,\beta)}\frac{(m+1)\alpha-m\beta+2m+1}{\alpha+\beta+2m+1}>0.}
\]
Its last numerator is \(m(\alpha-\beta)+\alpha+2m+1>0\). Hence \(A_{2m}\) strictly increases. Also \(A_2=\alpha(\alpha+1)/[(\alpha+\beta)(\alpha+\beta+1)]<p\), because \(\beta>0\).

By the conditional law of large numbers, \(g_n(u)\to\mathbf1_{\{u>1/2\}}\) for every \(u\ne1/2\); bounded convergence gives \(A_{2m}\to L:=\Pr(\Theta>1/2)\). This limit exceeds \(p\) without invoking an external theorem: since \(f(u)>f(1-u)\) for \(1/2<u<1\) when \(\alpha>\beta\),
\[
L-p=\int_{1/2}^1(1-u)[f_{\alpha,\beta}(u)-f_{\alpha,\beta}(1-u)]\,du>0.
\]
The strictly increasing even subsequence starts below \(p\) and converges above it. Thus its comparison with \(p\) changes sign exactly once, allowing at most one equality at the boundary; the smallest index for strict improvement exists and is unique.

For \(\alpha=2,\beta=1\), the beta-binomial mass reduces to
\[
\Pr(X_n=k)=\frac{2(k+1)}{(n+1)(n+2)}.
\]
Summing from \(\lfloor n/2\rfloor+1\) to \(n\) yields the two stated rational formulas. In the even case,
\[
A_{2m}-\frac23=\frac{m-4}{6(2m+1)}.
\]
Consequently \(A_{8}=2/3\), \(A_{10}=15/22>2/3\), and all earlier even sizes are below the individual benchmark. This proves sharpness of the stated first even crossover. For context only, the odd-case formula gives \(A_{2m+1}>p\) for \(m\ge1\), consistent with established odd-jury theorems.

## Verification

The standalone standard-library program `verify.py` recomputes the exact beta-binomial probabilities as fractions for six positive-integer parameter pairs and checks probability normalization, both parity gaps, the even-size increment identity, and the \((2,1)\) closed forms. It completes 444 exact rational checks. These finite checks corroborate but do not replace the proof for all real \(\alpha>\beta>0\), all electorate sizes, or the limiting inequality.

## Relationship to prior work

Braha and de Aguiar (2025, Theorem 1 and Proposition 2) supply the stationary beta-binomial law and establish an **asymptotic** majority advantage, noting that the finite-size advantage is not uniform. Their 2026 follow-up, *Majority Correctness in Social Networks: From Well-Mixed Electorates to Complex Networks*, establishes the individual-versus-majority improvement for **odd** electorates. Its Appendix B explicitly attributes a Polya–Eggenberger odd-electorate inequality to Berg (1993). Those stationary laws and odd-voter advantages are not novel claims here.

The present statement instead resolves the distinct **even, strict-majority, tie-counts-as-failure** comparison: its full two-step monotonicity, the unavoidable odd/even sawtooth, the existence and uniqueness of the even benchmark crossing, and its exact first occurrence with the minimally imbalanced integer zealots. The known odd-only results do not imply the even theorem; the conditional even increment is sign-changing before mixture integration. Searching the nearby literature and indexed mathematical findings identified no inspected statement giving the same even-size classification. A potentially relevant original 1993 Berg paper could not be accessed in full and remains a historical-priority risk.

## Limitations

This is an exact stationary classification for fully mixed beta-binomial free votes and **strict** majorities. Ties are counted as failures rather than resolved randomly. A different tie-breaking rule changes the even-size conclusions. The theorem concerns positive beta shape parameters, not arbitrary dependent votes or arbitrary graph topologies; the threshold index for general \(\alpha,\beta\) is defined by an explicit finite tail and need not have a simple closed form. It does not claim original discovery of the beta-binomial law or the odd-size Condorcet comparison. Historical priority for the even-size result is not independently established; no external audit has been performed.

## References

1. D. Braha and M. A. M. de Aguiar, *Generalizing Condorcet's Jury Theorem to Social Networks*, arXiv:2510.16808v1 (first posted 2025-10-19), especially Theorem 1 and Proposition 2. https://arxiv.org/abs/2510.16808
2. D. Braha and M. A. M. de Aguiar, *Majority Correctness in Social Networks: From Well-Mixed Electorates to Complex Networks*, arXiv:2607.14288v1 (first posted 2026-07-15), especially Theorem 3 and Appendix B. https://arxiv.org/abs/2607.14288
3. S. Berg, *Condorcet's jury theorem: dependency among voters*, Social Choice and Welfare 10 (1993), 87–95. DOI:10.1007/BF00187435. Historical related reference; full text not inspected.
