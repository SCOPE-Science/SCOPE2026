# Exponential lottery fairness: a sharp four-good boundary and a cubic phase transition

## Finding

Consider two agents and a complete division of indivisible goods. Each agent's value for good \(j\) is an independent exponential random variable with mean \(w_j>0\); distributions for the same good are identical across agents, but the means may vary across goods. Ex-ante envy-freeness (EF) means that the two bundle sums of means agree. Ex-post EF probability means the probability, over all independent utility realizations, that neither agent envies the other's realized bundle.

**Sharp size boundary.** For every such instance with at most three goods, every ex-ante EF allocation, whenever one exists, maximizes ex-post EF probability among all complete allocations. Four goods suffice for failure, even though every individual valuation distribution is exponential.

**Exact four-good phase diagram.** For every real \(t\ge2\), take four labeled goods of respective exponential means \((1,2,t,t+3)\). Up to exchanging agents, the unique ex-ante EF split is \(A_t=\{t+3\}\mid\{1,2,t\}\). Define \(B_t=\{1,t+3\}\mid\{2,t\}\), and let \(t_*\in(3,4)\) be the unique positive root of
\[
3t^3+2t^2-46t-33=0.
\]
The ex-post EF probability is maximized by \(A_t\) for \(2\le t<t_*\), by both \(A_t\) and \(B_t\) at \(t=t_*\), and by \(B_t\) for \(t>t_*\), with no other optimal unordered split. The exact success probabilities are \(P_A(t)=p_A(t)(1-p_A(t))\) and \(P_B(t)=p_B(t)(1-p_B(t))\), where
\[
p_A(t)=\frac{(t+3)^3}{(t+4)(t+5)(2t+3)},\qquad
p_B(t)=\frac{3t^3+24t^2+58t+33}{3(t+1)(t+5)(2t+3)}.
\]
For the rational four-good witness \((1,2,4,7)\), moving from the ex-ante EF split to \(B_4\) improves ex-post EF probability by exactly \(11081/141134400>0\).

**Robustness beyond a particular slice.** Given any \(0<a<b\), let the means be \((a,b,t,t+a+b)\). The ex-ante EF split is the largest singleton versus the other three goods. The alternative pairing of the largest and smallest goods versus the middle two has an ex-post EF probability advantage
\[
\frac{a(b-a)}{2t^2}+O(t^{-3})\quad\text{as }t\to\infty.
\]
Consequently, this reversal occurs for every fixed \(a<b\) once \(t\) is sufficiently large, and persists under small perturbations of the four means that preserve the ex-ante equal-sum constraint.

## Assumptions and scope

All agent-good valuation variables are mutually independent, with \(X_{ij}\sim\operatorname{Exp}(\text{mean }w_j)\), meaning density \(w_j^{-1}e^{-x/w_j}\) on \(x\ge0\). The agent-good distributions are identical in law between the two agents, not identical random realizations. Every good is allocated irrevocably and entirely to exactly one agent. Empty bundles are permitted but cannot be ex-post EF when at least one positive good exists. All comparisons are made before random values are revealed.

For a split \(S\mid S^c\), let \(p(S)=\Pr(\sum_{j\in S}X_{1j}>\sum_{j\notin S}X_{1j})\). Because the two agents' utility rows are independent and have the same distributions, and ties have probability zero,
\[
P_{\rm EF}(S\mid S^c)=p(S)(1-p(S)).
\]
A complete allocation is ex-ante EF exactly when the mean sums of the two bundles agree. These reductions are used throughout.

## Proof

**Step 1: no counterexample before four goods.** If two goods admit an ex-ante EF split, their means agree; the two independent exponential values are equally likely to be larger, so the resulting ex-post EF probability is \(1/4\), the universal upper bound on \(p(1-p)\). The one-good instance has no ex-ante EF split for positive means. For three goods, an ex-ante EF split, after relabeling, has singleton mean \(a=b+c\), with other goods of means \(b,c>0\). Exponential Laplace transforms give
\[
p(\{a\})=\frac{a^2}{(a+b)(a+c)}<\frac12.
\]
For each of the two alternative singleton splits of means \(s=b\) or \(s=c\),
\[
p(\{s\})=\frac{s^2}{(s+a)(s+u)},
\]
where \(u\) is the remaining other mean. Since \(a>s\) and \(x\mapsto x^2/(x+u)\) is increasing for positive \(x\), \(p(\{s\})<p(\{a\})<1/2\). Thus \(p(1-p)\) is largest for the ex-ante EF singleton split; every unordered two-way partition of three goods is represented by one singleton.

**Step 2: exact exponential formulas.** If \(X\) has exponential mean \(z\), independent of exponential variables of means \(u_1,\ldots,u_k\), then
\[
\Pr(X>X_1+\cdots+X_k)=\prod_{j=1}^k\frac{z}{z+u_j}.
\]
For independent exponentials of means \(a,b,c,d>0\), the probability of the first two beating the last two is, for \(a\ne b\),
\[
\Pr(X_a+X_b>X_c+X_d)
=\frac{aL(a)-bL(b)}{a-b},\quad
L(z)=\frac{z^2}{(z+c)(z+d)}.
\]
For \(a=b\), its continuous limit is \(L(a)(3-a/(a+c)-a/(a+d))\). These identities follow by integrating the survival function \((ae^{-x/a}-be^{-x/b})/(a-b)\) against the distribution of \(X_c+X_d\); thus they include all parameter boundaries.

**Step 3: only two candidates in the four-good family.** Write \(d=t+3\). For the four means \(1,2,t,d\) with \(t\ge2\), every unordered nonempty split is either a singleton versus a triple or a pair versus a pair. In the singleton class, the singleton \(d\) maximizes its probability of beating the other bundle by exponential stochastic ordering, while
\[
p_A-\frac12=-\frac{3t^2+13t+6}{2(t+4)(t+5)(2t+3)}<0.
\]
Since \(p\mapsto p(1-p)\) is increasing on \([0,1/2]\), \(A_t\) is best in the singleton class. In the pair class, orient each split so its first pair contains \(d\). Exchanging the other member of that pair from mean \(1\) to \(2\) or \(t\) makes its value stochastically larger and the opposite pair stochastically smaller. The smallest success probability of a pair containing \(d\) therefore occurs at \(\{1,d\}\), and the exact calculation yields
\[
p_B-\frac12=\frac{3t^2+32t+21}{6(t+1)(t+5)(2t+3)}>0.
\]
Because \(p\mapsto p(1-p)\) decreases on \([1/2,1]\), \(B_t\) is best in the pair class. Strict stochastic dominance for \(t>2\) excludes other optimizers (and any extra pair ties at \(t=2\) are suboptimal).

**Step 4: cubic transition.** Apply Step 2 to \(A_t\) and \(B_t\) to obtain the stated \(p_A,p_B\). Direct rational factorization gives
\[
P_B(t)-P_A(t)
=\frac{(3t^3+2t^2-46t-33)(6t^3+46t^2+103t+51)}{9(t+1)^2(t+4)^2(t+5)^2(2t+3)^2}.
\]
The second numerator factor and denominator are positive for \(t\ge2\). By Descartes' sign rule the cubic has exactly one positive root; its values at \(3\) and \(4\) have opposite signs. Combining with Step 3 proves the exact global optimality and uniqueness statements. At \(t=4\), the exact one-sided probabilities are \(p_A=343/792\) and \(p_B=841/1485\), giving the stated rational improvement.

**Step 5: robust large-scale reversal.** Let \(d=a+b+t\), define \(p_A=d^3/((d+a)(d+b)(d+t))\), and put
\[
p_B=\frac{aL(a)-dL(d)}{a-d},\qquad L(z)=\frac{z^2}{(z+b)(z+t)}.
\]
These are the probabilities for singleton \(d\) and the pair \(\{a,d\}\), respectively. Taylor expansion at \(1/t=0\) of the exact rational expressions gives
\[
p_B(1-p_B)-p_A(1-p_A)
=\frac{a(b-a)}{2t^2}+O(t^{-3}).
\]
For \(a<b\), the leading coefficient is strictly positive, completing the robustness claim. Small perturbations within the equal-sum constraint preserve strict inequalities by continuity of the probability integrals.

## Verification

Run `python3 checker.py` in the directory containing this document and the supplied standalone code. The checker independently enumerates all unordered nontrivial splits for integer three-good instances \(a,b\le24\) with singleton mean \(a+b\); for the four-good family it checks every integer \(2\le t\le100\), the closed-form probabilities, the exact difference factorization, and the optimizer among every split. It also spot-checks the general asymptotic coefficient at large \(t\). It uses exact rational arithmetic and does not establish statements for every real parameter; Steps 1–5 above provide those analytic proofs.

## Relationship to prior work

Igarashi and Oh, *Fair Division of Lotteries* (arXiv:2610.34906, first public October 26, 2026), prove that ex-ante EF splits maximize ex-post EF probability for two agents when item distributions lie in one common convolution-power family (Theorem 4.2). Their Proposition 5.5 and Appendix A.4 also give a tight general log-concave approximation bound and a four-good counterexample in a broader distribution class. Neither result states this all-exponential minimum-good boundary or the exact cubic global-optimizer transition for unequal exponential means. Exponential distributions with differing scales do not in general constitute convolution powers of one common distribution, so Theorem 4.2 does not imply our claim. This work is a specialized exact refinement, not a contradiction of those established results or a claim that four-good failure is new for arbitrary log-concave laws.

An existing extremal-pairing observation for stochastically ordered goods already ranks the three pair-versus-pair allocations. The distinct comparison here is between their best pair split and the only ex-ante EF singleton-versus-triple split. Aloisio et al. (AAMAS 2024) study expected maximum envy with random valuations, not the maximization of ex-post zero-envy probability considered here.

## Limitations

The exact phase diagram applies to two agents, mutually independent utility realizations, and the specified four-good exponential family; the minimum-size theorem applies to any positive exponential means with up to three goods. The robustness expansion establishes a large-\(t\) sufficient condition and does not classify all finite \((a,b,t)\). No claim is made for correlated utilities, arbitrary non-exponential distributions, more than two agents, or a universal welfare guarantee. The arithmetic checker is finite evidence, not an infinite verification, and no independent scientific audit has been performed.

## References

1. A. Igarashi and Y. Oh, *Fair Division of Lotteries*, arXiv:2610.34906, first public 2026-10-26. https://arxiv.org/abs/2610.34906 . Relevant: Sections 3–5 and Appendix A.4.
2. A. Aloisio, V. Bilò, A. M. Caruso, M. Flammini, and C. Vinci, *Approximately Fair Allocation of Indivisible Items with Random Valuations*, AAMAS 2024. https://iris.gssi.it/handle/20.500.12571/30247 .
