# Sharp four-good asymmetry and the quadratic rare-event law for realized EF1

## Finding

For two agents with independent agent-specific binary lottery values, allocating goods in equal numbers need not maximize the probability that the realized allocation is envy-free up to one good (EF1). Four goods are the first number for which unequal bundle sizes can be optimal. The complete four-good phase diagram below has a single critical probability and a nonmonotone interval for the second probability. For any fixed number of goods, a rare-value limit gives an exact quadratic-risk allocation rule.

**Four-good theorem.** Each of four indivisible goods is worth either zero or one to each agent. The values of all agent–good pairs are independent. For agent \(i\), every good is worth one with probability \(p_i\in(0,1)\), and zero otherwise. A complete deterministic allocation is fixed before the values are realized. Set

\[
 s=\min\{p_1,p_2\},\quad t=\max\{p_1,p_2\},\quad
 f(z)=1-z^2(1-z)^2,\quad g(z)=1-3z^2+5z^3-3z^4.
\]

The maximum probability of realized EF1, over all complete allocations, is exactly

\[
 \boxed{\max\{f(p_1)f(p_2),\,g(s)\}.}
\]

The first term is obtained by giving two goods to each agent. The second is obtained by giving one good to the lower-probability agent and three to the higher-probability agent. Giving all four goods to one agent is strictly suboptimal. If the displayed terms are unequal, the maximizing bundle-size pattern is unique (up to permutations of indistinguishable goods); on equality both patterns are optimal.

Define

\[
 H(s)=\frac{s^2(2-3s+2s^2)}{1-s^2(1-s)^2}.
\]

The unequal \(1:3\) allocation is strictly better than equal splitting precisely when

\[
 \boxed{t^2(1-t)^2>H(s).}
\]

There is a unique \(s_c\in(0,1)\) satisfying \(H(s_c)=1/16\). Equivalently,

\[
 33s_c^4-50s_c^3+33s_c^2-1=0,
 \qquad s_c=0.2032804404095\ldots.
\]

For \(s<s_c\), the unequal allocation wins exactly on the open probability interval

\[
 \frac{1-\sqrt{1-4\sqrt{H(s)}}}{2}<t<
 \frac{1+\sqrt{1-4\sqrt{H(s)}}}{2}.
\]

The endpoints give ties. If \(s>s_c\), equal splitting wins for every \(t\ge s\). If \(s=s_c\), the only tie is at \(t=1/2\); equal splitting is otherwise strictly better. In particular, the preference for a three-good bundle is *not* monotone in the high agent's Bernoulli probability.

For instance, \(p_1=1/100\) and \(p_2=1/10\) yield

\[
 \Pr(\mathrm{EF1}\mid 1:3)=\frac{99970497}{100000000},\qquad
 \Pr(\mathrm{EF1}\mid 2:2)=\frac{991802783881}{10^{12}},
\]

so unequal splitting increases the probability by exactly \(7902186119/10^{12}\). Every probability-maximizing allocation with at most three goods has bundle counts differing by at most one, making the four-good horizon sharp.

**Rare-value theorem.** More generally, for any fixed integer \(m\ge2\), let \(p_i=\varepsilon\lambda_i\) with positive fixed \(\lambda_1,\lambda_2\) and \(\varepsilon\downarrow0\). If agent 1 receives \(a\) goods and agent 2 receives \(m-a\), then uniformly for \(a\in\{0,\ldots,m\}\),

\[
 \Pr(\mathrm{EF1}\mid a,m-a)
 =1-\varepsilon^2\left[\lambda_1^2\binom{m-a}{2}
 +\lambda_2^2\binom a2\right]+O(\varepsilon^3).
\]

Put \(\theta=(m-1)\lambda_1^2/(\lambda_1^2+\lambda_2^2)\). If \(\theta\notin\mathbb Z\), then for all sufficiently small positive \(\varepsilon\), the **unique optimal number** of goods for agent 1 is \(\lceil\theta\rceil\). If \(\theta\in\mathbb Z\), for all sufficiently small positive \(\varepsilon\) every optimum belongs to the two candidate counts \(\theta\) and \(\theta+1\), without asserting that both remain optimal at finite \(\varepsilon\). Thus rare Bernoulli risks determine the preferred bundle sizes through their **squared rates**, rather than their rates. For four goods, an asymptotic three-to-one split is strictly preferred when the higher rate exceeds \(\sqrt2\) times the lower one.

## Assumptions and scope

There are exactly two agents and \(m\) indivisible goods, all allocated exactly once. Agent \(i\)'s utility of a bundle is the sum of its per-good values. For each agent, per-good utilities are identically Bernoulli-distributed with parameter \(p_i\), but \(p_1\) need not equal \(p_2\). All \(2m\) agent–good values are mutually independent. Both parameters lie strictly between zero and one. No reallocation, compensation, conditioning on values, or adaptive mechanism is allowed after realizations. EF1 means that, for each ordered agent pair, deleting at most one good from the envied bundle eliminates the envy in the realized valuation profile.

In this model, equal bundle sizes are ex-ante envy-free whenever \(m\) is even, since each agent evaluates every good at the same mean \(p_i\). The four-good result concerns maximizing the probability of EF1 *after* realization; it is not a statement about a lottery over allocations. It does not assert optimality for non-Bernoulli values, dependent utilities, more than two agents, or growing \(m\) in the rare-value limit.

## Proof

**Step 1: exact finite probability.** If an agent's own bundle contains \(a\) goods and the other bundle contains \(b\), the realized own and other values are independent \(X\sim\operatorname{Bin}(a,p)\) and \(Y\sim\operatorname{Bin}(b,p)\). Because every positively valued good has value one, EF1 is equivalent to \(Y\le X+1\). Hence, writing

\[
 T_{a,b}(p)=\sum_{x=0}^{a}\binom ax p^x(1-p)^{a-x}
 \sum_{y=0}^{\min\{b,x+1\}}\binom by p^y(1-p)^{b-y},
\]

independence of the two agents' entire value vectors gives

\[
 \Pr(\mathrm{EF1}\mid a,b)=T_{a,b}(p_1)T_{b,a}(p_2).
\]

For four goods, a \(2:2\) allocation fails EF1 for an agent precisely when she values both other goods and neither own good. Its single-agent success probability is \(f(p)\). In a \(1:3\) allocation the agent holding three goods cannot envy the other agent up to one good. The singleton holder fails precisely if her own good is worth zero while at least two of the three other goods are worth one, or if her own good is worth one while all three other goods are worth one. Thus her failure probability is \(3p^2-5p^3+3p^4\), giving \(g(p)\).

The \(0:4\) and \(4:0\) allocations are strictly dominated by moving one good to the empty agent: the other agent still faces only a singleton and cannot violate EF1, while the initially empty agent's EF1 event strictly expands (an event of positive probability is newly successful). Finally,

\[
 g'(p)=-3p(4p^2-5p+2)<0\qquad(0<p<1),
\]

since \(4p^2-5p+2\) has negative discriminant and positive leading coefficient. Among the unequal splits, the singleton should therefore be assigned to the smaller-probability agent. Taking the maximum with the balanced score proves the exact formula.

**Step 2: sharp phase boundary.** Since \(f(s)>0\) and \(f(s)-g(s)=s^2(2-3s+2s^2)\), the inequality \(g(s)>f(s)f(t)\) is equivalent to \(t^2(1-t)^2>H(s)\). Direct differentiation gives

\[
 H'(s)=\frac{s(4-9s+8s^2-s^3+s^5)}{f(s)^2}>0.
\]

Indeed, \(4-9s+8s^2\ge47/32\), while \(-s^3+s^5\ge-1\); hence the parenthesized polynomial is at least \(15/32\). Since \(H(0)=0\) and \(H(1)=1\), there is exactly one solution to \(H(s)=1/16\). The elementary function \(t^2(1-t)^2\) has its unique maximum \(1/16\) at \(t=1/2\), and solving the strict inequality gives the stated interval and critical tie. Moreover, \(H(s)>s^2(1-s)^2\) for \(0<s<1\), since \(f(s)\le1\) and \((2-3s+2s^2)-(1-s)^2=1-s+s^2>0\). Thus the lower endpoint of the unequal-optimality interval always exceeds \(s\) when \(s<s_c\), so it is compatible with \(t\ge s\).

**Step 3: minimal horizon.** With one good all allocations are EF1. With two goods, splitting \(1:1\) is EF1 surely, whereas a \(0:2\) allocation fails with probability \(p^2>0\) for the empty agent. With three goods, for a \(0:3\) allocation the empty agent's failure probability is \(3p^2-2p^3\); giving her one good while leaving two to the other agent reduces it to \(p^2(1-p)\), a strict reduction of \(p^2(2-p)\). The two-good holder cannot violate EF1 against a singleton. Therefore only \(1:2\) or \(2:1\) can optimize at three goods. The explicit four-good witness above proves sharpness.

**Step 4: rare-event optimization for every fixed \(m\).** For fixed nonnegative \(a,b\) with \(a+b=m\), the failure event \(Y\ge X+2\) has, at \(p\downarrow0\), leading probability \(\binom b2p^2+O(p^3)\): it requires at least two valued goods in the other bundle, and the unique order-two contribution comes from no valued own goods and exactly two valued other goods. Substituting \(p_1=\varepsilon\lambda_1\) and \(p_2=\varepsilon\lambda_2\) into the product in Step 1 proves the displayed expansion. Uniformity is automatic because there are only \(m+1\) bundle-size choices.

Let \(L(a)=\lambda_1^2\binom{m-a}{2}+\lambda_2^2\binom a2\). Its consecutive differences are

\[
 L(a+1)-L(a)=(\lambda_1^2+\lambda_2^2)(a-\theta).
\]

They are strictly increasing. If \(\theta\) is nonintegral the unique integer minimizer is \(\lceil\theta\rceil\); if integral the only minimizers are \(\theta,\theta+1\). The uniform expansion and the positive finite gap to all nonminimizers transfer this minimizer classification to sufficiently small positive \(\varepsilon\), as claimed. At \(m=4\), \(L(1)=3\lambda_1^2\) and \(L(2)=\lambda_1^2+\lambda_2^2\), so the sharp rare-event crossover is \(\lambda_2^2=2\lambda_1^2\) when \(\lambda_2>\lambda_1\).

## Verification

The included standard-library program `verify.py` checks the exact binomial formula against direct independent enumeration of the two agents' binary utility vectors for \(m=1,\ldots,5\) and six rational probability pairs, including the transition witness. It checks the four-good maximum against all five bundle-size possibilities and verifies the stated minimum-horizon claim on these test instances. For \(m=2,\ldots,8\) and five positive rare-event rate pairs, it checks the quadratic coefficient by exact rational evaluation at a small parameter and checks the predicted unique minimizers whenever the leading minimizer is unique. The script reports 330 checks and the exact witness gap. These computations are finite sanity checks, not a substitute for the all-parameter proof above.

Run `python verify.py` alongside this file; no third-party packages or external data are required.

## Relationship to prior work

Igarashi and Oh, *Fair Division of Lotteries* (2026), formulate independent agent–item random values and establish ex-post **envy-freeness** maximization under shared marginal distributions across agents, including log-concave convolution-power families. Their conclusion explicitly proposes studying EF1 as a further direction. The current result instead optimizes **ex-post EF1** with different Bernoulli probabilities for the two agents; neither their EF theorem nor their identical-distribution hypotheses imply the present phase curve or rare-event law.

Aloisio et al., *Approximately Fair Allocation of Indivisible Items with Random Valuations* (2024), study expected maximum envy for precommitted allocations, rather than the exact probability of EF1. Babaioff and Grofman (2026) study ex-ante fairness and ex-post support under randomness in **allocations with fixed utilities**, not Bernoulli uncertainty in utilities of one fixed allocation.

Related exact calculations for shared Bernoulli item values and for independent identically distributed values in equal-sized bundles do not imply this heterogeneous, independently valued, unequal-size optimization. The comparison does not establish publication priority in every unindexed source.

## Limitations

The result is specific to two agents, i.i.d. Bernoulli values within each agent, independence across both agents and all goods, complete nonadaptive allocation, and realized EF1 probability. The rare-value statement fixes \(m\) as \(\varepsilon\downarrow0\) and does not assert uniformity when the number of goods grows. On the leading-order tie \(\theta\in\mathbb Z\), it does not classify which of the two candidate counts wins at finite \(\varepsilon\). Unindexed earlier treatments of exact Bernoulli fairness probabilities remain a priority risk.

## References

1. A. Igarashi and Y. Oh, *Fair Division of Lotteries*, arXiv:2610.34906v1, first posted 2026-10-26, https://arxiv.org/abs/2610.34906.
2. A. Aloisio, V. Bilò, A. M. Caruso, M. Flammini and C. Vinci, *Approximately Fair Allocation of Indivisible Items with Random Valuations* (2024), https://iris.gssi.it/handle/20.500.12571/30247.
3. M. Babaioff and Y. Grofman, *On Best-of-Both-Worlds Fairness via Sum-of-Variances Minimization*, arXiv:2601.16579v1, https://arxiv.org/abs/2601.16579.
