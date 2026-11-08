# A sharp lower-quota boundary for full truthfulness in probabilistic serial assignment

## Finding

For unit-demand minimums probabilistic serial (MPS) with nonbinding object upper capacities, **one positive minimum quota is sufficient for full stochastic-dominance strategyproofness**, irrespective of the number of agents or objects. In contrast, **two positive minima permit full-strategyproofness failure already with three agents and three objects**, and these are the smallest possible numbers of agents and objects for such a failure in this domain.

In the smallest failing market, with three agents and three objects \(A,B,C\), lower quotas \((1,1,0)\), and upper capacities \((3,3,3)\), exactly \(30\) of the \(6^3=216\) labeled strict preference profiles admit a unilateral report that raises expected utility for some strictly order-consistent cardinal utility. There are exactly \(36\) improving (truthful profile, deviating agent, alternative strict report) triples. The profile count is \(5/36\) under independent uniformly random strict preferences.

## Assumptions and scope

There are \(n\ge1\) unit-demand agents and \(m\ge2\) distinct objects. Each agent reports a strict ranking and receives a probability distribution summing to one. Object \(j\) has an integer lower quota \(\ell_j\ge0\), with \(\sum_j\ell_j\le n\), and nonbinding upper capacity \(c_j=n\). Only unilateral ranking reports are considered. The result does not assert full strategyproofness when upper capacities bind, for multidemand, for group deviations, or for other mechanisms.

MPS is the unit-speed constrained eating process of Sandholtz and Tai, equivalently the lower-quota extension of probabilistic serial of Bojko in this unit-demand, no-upper-binding domain. At cumulative object mass \(q_j(t)\), the feasibility-of-completion constraint is

\[
\sum_{j=1}^{m}\max\{\ell_j,q_j(t)\}\le n.
\]

Agents eat their favorite currently available object. When this inequality binds, objects that have met their lower quota are unavailable, and each agent continues eating an object whose minimum remains unfilled. All upper capacities are \(n\), so none binds strictly before time \(1\). Stochastic-dominance (SD) strategyproofness means, for every profile, agent and unilateral report, the truthful lottery weakly first-order stochastically dominates the lottery under the report, evaluated against the agent's true order. This is stronger than weak strategyproofness, which prohibits only a *strictly SD-dominating* deviation.

## Proof

**1. Exact allocation with one positive lower quota.** Suppose exactly one object \(a\) has lower quota \(L\in\{1,\ldots,n\}\). Let \(s\) be the number of agents whose **reported** first choice is \(a\). If \(s\ge L\), everyone receives her reported first choice with probability one. Indeed, up to time \(L/s\), the feasibility left side is \(L+(n-s)t\), which is at most \(n\); afterwards it is \(nt\), less than \(n\) before completion. Thus no premature global restriction occurs.

If \(s<L\), the \(s\) agents preferring \(a\) eat that object and all other agents eat their respective favorite objects. Before any restriction, the global feasibility left side is \(L+(n-s)t\). Hence it becomes binding at

\[
\tau=\frac{n-L}{n-s},\qquad 0\le\tau<1.
\]

At that time the quota of \(a\) is not filled, so all other objects become unavailable and all agents eat \(a\) until completion. An agent who ranks \(a\) first obtains \(a\) with certainty. Each other agent with reported first choice \(b\ne a\) obtains the two-point lottery

\[
\tau\,\mathbf e_b+(1-\tau)\,\mathbf e_a.
\]

If there are no positive quotas, everyone simply gets her reported first choice.

**2. Full SD strategyproofness in this domain.** Fix an agent's true preferences and all other reports. If her true first choice is \(a\), truthful reporting gives \(a\) with certainty, a stochastically maximal outcome. Otherwise write her true first choice \(b\ne a\). If her truthful report yields \(b\) surely, no deviation improves it. If it yields the mixture above, then any report placing \(a\) first gives \(a\) surely, which is SD worse than \(\tau\mathbf e_b+(1-\tau)\mathbf e_a\) because \(b\) is truly best. Every report placing another object \(b'\ne a\) first leaves the count \(s\) unchanged and replaces \(b\) in that mixture by \(b'\) without changing \(\tau\). Since \(b\) is truly preferred to \(b'\), the truthful lottery SD dominates. Changes in rankings below the reported first choice are immaterial. Therefore truth is SD dominant.

**3. Minimal counterexample with two minimum quotas.** Take lower quotas \((\ell_A,\ell_B,\ell_C)=(1,1,0)\) and upper capacities all \(3\). The three true orders are

\[
1:A\succ B\succ C,\qquad 2:A\succ C\succ B,\qquad 3:C\succ B\succ A.
\]

Under sincere eating, agents 1 and 2 eat \(A\), and agent 3 eats \(C\), until time \(2/3\), when the global completion constraint becomes tight. All eat \(B\) thereafter. Hence agent 2's lottery, in \((A,B,C)\) coordinates, is \((2/3,1/3,0)\).

If agent 2 instead reports \(C\succ A\succ B\), agents 2 and 3 first eat \(C\) until time \(1/2\), then agent 2 eats \(A\) while agent 3 eats \(B\) until time \(3/4\), and all eat \(B\) thereafter. Agent 2's lottery becomes \((1/4,1/4,1/2)\). Under the strict true cardinal utilities \(u_2(A)=12>u_2(C)=11>u_2(B)=1\), the sincere and deviating expected utilities are respectively \(25/3\) and \(35/4\). The gain is \(5/12>0\).

No smaller **agent count** can fail while retaining two positive integer minima: at \(n\le2\), feasibility forces \(n=2\) and the two quotas to equal one, exhausting the entire assignment and restricting the active menu to those two objects. For a mechanism with only two active objects, weak strategyproofness (already established for this lower-quota probabilistic-serial mechanism in the cited primary literature) implies full SD strategyproofness, because the two-object lottery order by SD is complete. No **two-object** market can fail for the same reason. The above \(3\)-agent, \(3\)-object example is therefore sharp in both dimensions. This minimality statement is for the stated nonbinding-upper-capacity domain.

**4. Exact census at the sharp boundary.** Fix these three object labels and quotas. Enumerate all \(6^3\) strict profiles. For each profile, each of three agents, and each of the five alternative strict rankings, compute both lotteries using exact rational arithmetic. For a true order \(j_1\succ j_2\succ j_3\), write \(\Delta_r\) for the deviating minus sincere probability on object \(j_r\). A strictly order-consistent expected-utility improvement exists **if and only if** at least one of \(\Delta_1\) or \(\Delta_1+\Delta_2\) is strictly positive. Necessity and sufficiency follow by expressing every strict utility vector as a positive combination of the two top-set indicator utilities plus a constant, and choosing one increment large enough in the positive case.

The self-contained `CHECK.py` evaluates this necessary-and-sufficient condition for every report with exact fractions. Its independent breakpoint implementations give identical outputs for every enumerated profile. The counts are: \(186\) profiles with no improving report, \(24\) with exactly one improving agent-report, and \(6\) with exactly two. Thus \(30\) profiles and \(36\) improving report triples in total. The \(30\) susceptible profiles have first-choice count vectors \((2,0,1)\), \((0,2,1)\), \((1,0,2)\), \((0,1,2)\) with multiplicities \(9,9,6,6\), respectively. The full finite enumeration is exhaustive because all \(6^3\) profiles and all \(3\cdot5\) candidate deviations per profile are visited; it is not an inference from a random sample.

## Verification

Run `python CHECK.py` with Python's standard library. It cross-checks \(864\) complete three-agent profiles across four quota vectors by two structurally separate exact-rational implementations. It additionally checks the one-quota allocation formula on \(6{,}480\) four-agent profiles and verifies the \(30/216\) incidence, the \(36\) improvement triples, the \(186/24/6\) decomposition, and the explicit positive utility difference. The all-market assertion in Parts 1–2 and the dimensional minimality in Part 3 are analytic arguments, not extrapolations from these finite checks.

## Relationship to prior work

Bojko (2020) independently developed a minimum-quota probabilistic serial eating procedure, proved weak (not full) strategyproofness, and supplied a larger-market manipulation example. Sandholtz and Tai (2026) present the unit-demand MPS mechanism and prove weak strategyproofness together with efficiency and envy-freeness. Neither inspected primary manuscript gives the one-positive-minimum *full* SD-strategyproofness theorem, the sharp \(3\)-by-\(3\) two-minimum witness, or its full labeled-profile cardinal-manipulability incidence. Classical probabilistic serial for one-seat objects is distinct because its upper capacities are binding; its known small-market manipulability does not imply the present quotas-only results. The novel claim concerns incentive structure, not authorship of the eating algorithm.

## Limitations

The characterization assumes all upper capacities equal the entire agent count, one unit of demand per agent, strict rankings, and only one deviating agent. The census is exact only for three agents and three objects with the stated quota vector; it does not give a closed form for arbitrary market dimensions. These proofs provide no independent external audit or guarantee of novelty against inaccessible or unindexed manuscripts. The 2020 lower-quota antecedent is explicitly recognized, so the 2026 motivating paper is not represented as the first source of all underlying algorithmic ideas.

## References

1. Will Sandholtz and Andrew Tai (2026), *Random Matching with Minimums*, arXiv:2605.26367v1, initially public 2026-05-25. https://arxiv.org/html/2605.26367v1
2. Marek Bojko (2020), *The Probabilistic Serial and Random Priority Mechanisms with Minimum Quotas*, arXiv:2012.11028v1, initially public 2020-12-20. https://arxiv.org/pdf/2012.11028
3. Ivan Balbuzanov (2022), *Constrained Random Matching*, Journal of Economic Theory 203, 105472. https://doi.org/10.1016/j.jet.2022.105472
4. Anna Bogomolnaia and Hervé Moulin (2001), *A New Solution to the Random Assignment Problem*, Journal of Economic Theory 100, 295–328. https://doi.org/10.1006/jeth.2000.2710
