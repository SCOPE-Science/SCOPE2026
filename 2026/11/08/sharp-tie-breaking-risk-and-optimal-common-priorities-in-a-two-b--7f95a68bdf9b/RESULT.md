# Sharp tie-breaking risk and optimal common priorities in a two-by-two matching market

## Finding

In a complete one-to-one market with two workers and two firms, assume each of the four agents independently reports indifference between the two possible partners with probability \(t\in[0,1]\), and otherwise ranks either partner first with probability \((1-t)/2\). Resolve all indifferences by any fixed, report-independent deterministic preference-refinement policy, and run worker-proposing deferred acceptance (DA). A failure occurs if the resulting complete matching is Pareto dominated with respect to the **original weak preferences of all four participants**.

The minimum failure probability among **all report-independent randomized preference-refinement policies** is
\[
P_{\min}(t)=\frac{t^2(1-t)(3t+1)}{4}.
\]
Every policy that gives both workers the **same** fixed priority over firms attains the minimum, regardless of the priorities used by the firms. A symmetric report-independent policy can attain the same bound by using one independent fair coin to determine the common worker-side priority, and a second independent fair coin to determine the common firm-side priority.

If, instead, every tied agent chooses its own ordering independently and fairly, the failure probability is
\[
P_{\mathrm{ind}}(t)=\frac{t^2(1-t)(7t+3)}{8},
\qquad
P_{\mathrm{ind}}(t)-P_{\min}(t)=\frac{t^2(1-t^2)}8.
\]
The improvement is strict for \(0<t<1\) and zero at the endpoints. At the uniform weak-order model \(t=1/3\), the independent-policy risk is \(4/81\), versus the optimal \(1/27\). As \(t\downarrow0\), the leading coefficient falls from \(3/8\) to \(1/4\), a one-third reduction.

## Assumptions and scope

Label workers \(w_0,w_1\) and firms \(f_0,f_1\). Every worker strictly prefers both firms to remaining unmatched, and every firm strictly prefers both workers to an empty position. Each participant independently has one of three weak orders on the two partners: strict priority for index \(0\), strict priority for index \(1\), or indifference. The respective probabilities are \((1-t)/2\), \((1-t)/2\), and \(t\). The participant's preferences over being unmatched never have a tie.

A deterministic tie policy is a vector \(b\in\{0,1\}^{4}\), with coordinates ordered \((w_0,w_1,f_0,f_1)\). If participant \(i\) reports a tie, the policy ranks partner \(b_i\) strictly first; an already strict report is left unchanged. The vector is selected independently of agents' reports. A randomized policy is an arbitrary ex ante distribution on these sixteen vectors, permitting correlation among participants' tie resolutions. After refinement, execute standard worker-proposing DA to completion. We ask whether the resulting matching is Pareto inefficient **for both sides jointly**, not whether it is dominated only for workers.

## Proof

**1. The possible failures have at least two but fewer than four tied agents.** Strict-refined DA produces a complete matching that is stable under the refinements, hence weakly stable under original orders. There are only two complete matchings in a two-by-two market; write \(\mu\) for the DA output and \(\nu\) for the other. Since every agent strictly prefers being matched to remaining unmatched, any matching Pareto dominating \(\mu\) must be complete and therefore must equal \(\nu\). The matching \(\nu\) consists of two worker–firm pairs, each absent from \(\mu\). Both members of such a pair cannot strictly prefer their partners under \(\nu\) to those under \(\mu\), or the pair would block \(\mu\) under the original weak orders. If \(\nu\) weakly improves everyone, at least one agent in **each** of the two disjoint alternative pairs must therefore be indifferent. Thus two distinct ties are necessary. If every agent is indifferent, no strict Pareto improvement is possible. Consequently only weak-order profiles with exactly two or three tied agents contribute to the failure event.

**2. Exact exhaustive coefficient table.** For each of the sixteen fixed bit vectors, enumerate the three weak orders at each of four participants, yielding exactly \(3^4=81\) possibilities per vector. Refine ties, execute worker-proposing DA, construct the other matching, and test whether every agent weakly prefers the other matching and at least one strictly prefers it. Let \(c_2(b)\), respectively \(c_3(b)\), count the failing weak-order profiles with exactly two, respectively three, tied agents. The following table is the complete classification; the four-character strings list bits in the order \((w_0,w_1,f_0,f_1)\).

| Policy vectors | Number | \(c_2\) | \(c_3\) |
|---|---:|---:|---:|
| `0000`, `0001`, `0010`, `0011`, `0110`, `1001`, `1100`, `1101`, `1110`, `1111` | 10 | 1 | 2 |
| `0100`, `0111`, `1000`, `1011` | 4 | 2 | 3 |
| `0101`, `1010` | 2 | 3 | 4 |

This is a finite exhaustive proof step, not an extrapolation from randomly selected examples. The standalone, standard-library `checker.py` enumerates all \(16\cdot81=1296\) cases, reproduces every row, cross-checks the strict DA result against an independent enumeration of stable matchings, and performs exact-rational numerical substitutions. Its complete source is included with this result.

**3. Convert counts into probabilities and minimize.** Every particular weak-order profile containing exactly \(k\) indifferences has probability \(t^k((1-t)/2)^{4-k}\). By step 1, for fixed vector \(b\),
\[
P_b(t)=c_2(b)\frac{t^2(1-t)^2}{4}
+c_3(b)\frac{t^3(1-t)}2.
\]
Both coefficients are nonnegative and the first class simultaneously minimizes \(c_2\) and \(c_3\), yielding \(P_{\min}\). The second and third classes have failure probabilities \(t^2(1-t)(2t+1)/2\) and \(t^2(1-t)(5t+3)/4\). A report-independent randomized policy is a convex combination of the sixteen deterministic policies. It cannot improve the pointwise minimum. The class table shows that all eight policies with equal worker bits belong to the first class, as do `0110` and `1001`. Two fair common-priority coins therefore give a label-symmetric optimal policy.

For independent fair tie-breaks, each of sixteen bit vectors has probability \(1/16\). Average the three class probabilities with weights \(10/16\), \(4/16\), and \(2/16\), and simplify to obtain \(P_{\mathrm{ind}}\). Direct subtraction gives the claimed strictly positive improvement inside \((0,1)\). At \(t=0\), no one is tied; at \(t=1\), everyone is tied, so all policies have zero failure probability.

## Verification

Run `python3 checker.py` with Python's standard library only. The program enumerates all \(1296\) deterministic policy/weak-profile combinations, checks the two matching candidates independently for stability and worker-optimality, confirms the full class table and the absence of failures with zero, one, or four ties, and compares the expectation at six rational values of \(t\) against the closed forms. It also verifies that the four implementations of the symmetric, common-priority fair-coin policy are optimal. The exact formulas and the proof apply to every real \(t\in[0,1]\); sampling finitely many parameter values is only a supplementary code check, while the exact coefficient table and polynomial identity prove the continuum statement.

## Relationship to prior work

Erdil and Ergin (2017) show that weak stability need not imply two-sided Pareto efficiency, including a two-by-two motivating example, and define **single tie-breaking**, in which each side uses a common ordering of its possible partners. Their Theorem 3 concerns efficiency when one side has strict preferences, while their Theorem 4 concerns which Pareto-efficient stable matchings can be supported by some single tie-breaking. Those statements do not directly give a risk-minimizing ex ante policy or a probability polynomial for random weak orders.

Domaniç, Lam and Plaxton (2017) construct a strategyproof Pareto-stable algorithm for two-sided indifferences; their object is the design of a different mechanism, not the exact stochastic failure probability of strictly refined DA. Kawase and Sato (2026) motivate the problem by noting that report-independent random tie-breaking followed by DA can be Pareto inefficient, and develop a deterministic generalized-DA replacement under gross substitutes. The present result instead quantifies and optimizes the failure risk **within the class of report-independent strict tie-refinement rules followed by ordinary worker-proposing DA**, in the fully specified smallest balanced market. No generalization to larger markets is claimed.

## Limitations

The result concerns exactly two workers and two unit-capacity firms, independent identically distributed original weak orders, full mutual acceptability, and an ex ante tie-refinement distribution independent of reported preferences. It does not imply optimality of common priorities with heterogeneous tie rates, in larger markets, or among all possible matching mechanisms. It does not bound worker-only Pareto loss, incentives under strategic reporting, or welfare magnitudes. Novelty assessment remains qualified by the possibility of a previously unindexed equivalent exact small-market enumeration.

## References

1. Yasushi Kawase and Ryosuke Sato, *A Weakly Group Strategy-Proof and Pareto-Stable Matching Mechanism with Two-Sided Indifferences under Gross Substitutes*, arXiv:2610.30807v1, first public October 22, 2026. https://arxiv.org/html/2610.30807v1
2. Aytek Erdil and Haluk Ergin, *Two-Sided Matching with Indifferences*, Journal of Economic Theory **171** (2017), 268–292, doi:10.1016/j.jet.2017.07.002. Open full text: https://www.isid.ac.in/~dmishra/gmdoc/indiff_match.pdf
3. Nevzat Onur Domaniç, Chi-Kit Lam and C. Gregory Plaxton, *Strategyproof Pareto-Stable Mechanisms for Two-Sided Matching with Indifferences*, arXiv:1703.10598v1 (March 30, 2017). https://arxiv.org/html/1703.10598v1
