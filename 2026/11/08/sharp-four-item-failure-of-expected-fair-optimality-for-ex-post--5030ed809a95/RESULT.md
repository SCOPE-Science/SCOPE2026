# Sharp four-item failure of expected-fair optimality for ex-post EF1 with Bernoulli lottery goods

## Finding

For two agents and \(m\) indivisible lottery goods, suppose all \(2m\) agent-good values are mutually independent, and for every good \(j\), each agent independently obtains value \(1\) with probability \(p_j\in(0,1)\), and \(0\) otherwise. Utilities are additive. Every complete allocation that is envy-free under the expected valuations maximizes the probability of realized envy-freeness up to one good (EF1) whenever \(m\le3\), provided such an allocation exists. This guarantee fails already for \(m=4\), with strictly positive and bounded binary values, even though both agents have the same distribution for each individual good.

More precisely, for \(0<\varepsilon<1/3\), consider four goods with success probabilities
\[
(p_1,p_2,p_3,p_4)=(\varepsilon,\tfrac13,\tfrac23,\tfrac13+\varepsilon).
\]
The allocation \(A=(\{1,3\},\{2,4\})\) is ex-ante EF, and the allocation \(B=(\{3\},\{1,2,4\})\) is not ex-ante EF. Their ex-post EF1 probabilities satisfy the exact identity
\[
\Pr(B\text{ is EF1})-\Pr(A\text{ is EF1})
=\frac{\varepsilon(19-652\varepsilon+48\varepsilon^2-36\varepsilon^3)}{729}.
\]
The cubic factor decreases strictly on \((0,1/3)\), is positive at \(0\), and is negative at \(1/3\); hence there is one threshold \(\varepsilon_*\in(0,1/3)\), approximately \(0.0292025111\), with \(B\) strictly better exactly for \(0<\varepsilon<\varepsilon_*\). At \(\varepsilon=1/60\), the improvement is exactly \(5431/29160000\), and the only expected-envy-free partition is \(A\), up to swapping agents.

## Assumptions and scope

There are exactly two agents and a fixed finite set of labeled goods, completely assigned before their binary values are realized. The variables \(u_i(j)\) are independent across both \(i\) and \(j\), and \(u_i(j)\sim\operatorname{Bernoulli}(p_j)\) with a common per-good success probability for both agents. All \(p_j\) lie strictly between zero and one. A deterministic allocation \((S,S^{\mathrm c})\) is ex-ante EF when both agents, under expected values, weakly prefer their own bundle; equivalently \(\sum_{j\in S}p_j=\sum_{j\notin S}p_j\). A realized allocation is EF1 if each agent's value for her bundle is at least the other's bundle value after removal of some one good from that other bundle (the empty bundle is allowed and needs no removal). The objective is the probability that both agents are EF1 simultaneously. There is no randomized allocation choice and no conditioning on realized values.

## Proof

**One-agent and two-agent decomposition.** For a partition \((S,T)\), the two EF1 comparisons depend on disjoint sets of random variables, one set for each agent. Thus their probabilities multiply. In particular, for two goods, an allocation of one good per agent is EF1 in every realization, because the sole good of the other agent can be removed. Hence any ex-ante EF allocation when \(m=2\) is ex-post optimal. The assertion for \(m=1\) is vacuous: positive expectations prevent ex-ante EF.

**Three goods.** When \(m=3\) and an ex-ante EF allocation exists, after relabeling its singleton's mean equals the sum of the means of the other two goods. Write the three probabilities as \((x+y,x,y)\), where \(x,y>0\) and \(x+y<1\). A singleton-versus-pair allocation in which the singleton has Bernoulli probability \(z\) and the pair has probabilities \(a,b\) is realized EF1 unless the singleton-holding agent values her good at zero and both other goods at one. The pair-holding agent is always EF1 relative to the singleton. Consequently its EF1 probability is exactly \(1-(1-z)ab\).

For the balanced singleton \(x+y\), and for the alternative singleton goods \(x\) or \(y\), the respective probabilities are
\[
F_{x+y}=1-(1-x-y)xy,\qquad
F_x=1-(1-x)(x+y)y,\qquad
F_y=1-(1-y)(x+y)x.
\]
Their differences satisfy \(F_{x+y}-F_x=y^2>0\) and \(F_{x+y}-F_y=x^2>0\). The only other partitions put all three goods with one agent and leave the other empty. Such an allocation is EF1 precisely when at most one good has positive realized value for the empty-bundle agent. The failure event therefore contains the event that the balanced singleton has value zero and the balanced pair's two goods both have value one; hence these empty-bundle allocations cannot improve upon \(F_{x+y}\). This proves optimality for all \(m\le3\).

**Four-good counterexample.** Under \(A=(\{1,3\},\{2,4\})\), each agent's expected bundle value is \(2/3+\varepsilon\). For a two-good bundle, an agent violates EF1 only if she values both her own goods at zero and both the other goods at one. Using independence across agents gives
\[
F_A=\left[1-(1-\varepsilon)(1-\tfrac23)\tfrac13(\tfrac13+\varepsilon)\right]
\left[1-(1-\tfrac13)(1-\tfrac13-\varepsilon)\varepsilon\tfrac23\right]
=\frac{(3\varepsilon^2-2\varepsilon+26)(12\varepsilon^2-8\varepsilon+27)}{729}.
\]
Under \(B=(\{3\},\{1,2,4\})\), the three-good holder is automatically EF1 relative to the single-good holder. The singleton holder fails EF1 either when her good has value zero and at least two of the other three are positive, or when her good has value one and all three others are positive. These are disjoint, yielding
\[
F_B=1-\tfrac13\Pr(\operatorname{Bernoulli}(\varepsilon)+\operatorname{Bernoulli}(\tfrac13)+\operatorname{Bernoulli}(\tfrac13+\varepsilon)\ge2)
-\tfrac23\varepsilon\tfrac13(\tfrac13+\varepsilon)
=\frac{26-9\varepsilon-9\varepsilon^2}{27}.
\]
Expanding \(F_B-F_A\) gives the polynomial in the finding. The derivative of its cubic factor is \(-652+96\varepsilon-108\varepsilon^2<0\) throughout \((0,1/3)\). At the endpoints that factor is \(19\) and strictly negative, respectively, proving the unique crossing and strict gain below it. Substituting \(\varepsilon=1/60\) yields \(5431/29160000>0\).

Finally, for this numerical instance the four probabilities in units of \(1/60\) are \((1,20,40,21)\). Half their total is \(41/60\). The only subsets summing to \(41/60\) are \(\{1,3\}\) and \(\{2,4\}\); therefore the non-ex-ante allocation \(B\) outperforms every ex-ante EF allocation, not merely one particular tie-breaking of them.

## Verification

The included standalone \(verify.py\) computes EF1 probabilities by direct exact enumeration of all independent binary agent-good realizations. It tests the four-good rational witness against the exact polynomial formula, checks the two complete ex-ante partitions, compares all four-good allocations, and tests the three-good identities on a rational parameter grid. Run \(`python3 verify.py`\). The proof above is algebraic and does not rely on finite testing.

## Relationship to prior work

Igarashi and Oh, *Fair Division of Lotteries* (arXiv:2610.34906v1, public October 26, 2026), define ex-ante/ex-post EF under exogenously uncertain independent item utilities. Their Theorem 4.2 proves that ex-ante EF maximizes ex-post **exact EF** for two agents when item distributions are convolution powers of one generator; Theorem 4.5 and Proposition 5.6 provide further conditions for exact EF. Their conclusion explicitly raises EF1 as another fairness notion to study. The present theorem instead treats the realized **EF1** event and heterogeneous Bernoulli parameters across goods. Itemwise log-concavity does not imply a common convolution-power representation for distinct Bernoulli parameters. Results about ex-ante lotteries over deterministic assignments concern another source of randomness and do not imply the stated fixed-allocation claim.

## Limitations

This is a sharp boundary by number of goods for the specified two-agent independent Bernoulli model, not a characterization of optimal allocations for arbitrary numbers of goods or agents. The polynomial threshold compares two particular four-good allocations; it does not assert which is globally best for every value of \(\varepsilon\). The strict improvement at \(\varepsilon=1/60\) is small, but the substantive boundary is failure of an always-optimality guarantee, not the gain's magnitude. Independent validation has not been performed. The novelty assessment is limited to the inspected literature and available indexed records.

## References

- Ayumi Igarashi and Yeeseok Oh, *Fair Division of Lotteries*, arXiv:2610.34906v1, first posted 2026-10-26, https://arxiv.org/abs/2610.34906 . See Sections 3–5 and 8.
- Rupert Freeman, Nisarg Shah, and Rohit Vaish, *Best of Both Worlds: Ex-Ante and Ex-Post Fairness in Resource Allocation*, 2020, https://arxiv.org/abs/2005.14122 . Its lotteries randomize allocations with fixed values, unlike the exogenous-utility model here.
