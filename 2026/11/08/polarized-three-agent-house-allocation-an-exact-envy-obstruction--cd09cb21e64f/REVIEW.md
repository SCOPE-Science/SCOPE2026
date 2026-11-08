# Review of the polarized three-agent house-allocation theorem

## Correctness

**PASS.** The conclusion is an exact statement for all integers \(m\geq3\), not an extrapolation from tested cases. Envy-free assignments necessarily allocate the lowest-index selected house to the first polarized agent, the highest-index house to the second, and the middle house to the third; their unanimous satisfaction is equivalent to the third agent preferring the middle. A three-case constructive table guarantees at most one ordered envy edge even when full envy-freeness fails, simultaneously attaining minima of all three customary aggregate envy measures. Recursive endpoint deletion characterizes all and only forbidden third rankings, which are counted by \(2^{m-1}\). Tail summation then gives the exact first inventory size distribution, expectation, and variance. An independent exhaustive implementation compared all injective assignments with these predictions for every third ranking and \(3\leq m\leq8\). Boundary cases \(m=3\) and the impossible two-house prefix are treated explicitly.

## Originality

**PASS, with residual risk.** Hosseini–Roy–Sethia (2025, arXiv:2511.07022v1, Section 4.2, Lemma 4.10) already imply *one direction*: globally single-dipped rankings preclude full envy-freeness for three agents. The present theorem adds the conditional converse for a polarized pair, simultaneous exact optima of three envy measures, and a closed-form probability and first-inventory law. The Gan–Suksompong–Voudouris (2019, arXiv:1905.00468v2, Section 2) generic decision algorithm and independent-rankings asymptotic theorem do not state these results. Targeted searches using the alternate phrases 'opposite rankings', 'polarized house allocation', 'single-dipped', 'endpoint-deletable', 'minimum ordered envy', and 'first-success inventory' yielded no equivalent theorem. The count of endpoint-deletable rankings as such is elementary and is *not* asserted to be new; an unindexed application of it to this allocation family is a residual risk.

## Mathematical value

**PASS.** The fixed-size existence question and exact amount of unavoidable envy are intrinsic to spare-house allocation. Two perfectly polarized preferences are a natural extremal case, and the third agent's single-dipped property is an established structural restriction with an existing one-sided impossibility lemma. Proving that the restriction is also necessary in this case gives a complete classification and an unexpectedly common minimum for three different fairness measures. The exact conditional probability and expected inventory needed to restore full envy-freeness provide finite-market benchmarks not obtainable directly from generic asymptotic high-probability results. This is a deliberately restricted but motivated exact classification, not an arbitrary numerical slice or a claim about all house markets.

## Sources and scientific limits

Primary motivating material: https://arxiv.org/html/2511.07022v1 (Sections 2, 4.2, 4.3, 6). Closest general existence/probability material: https://arxiv.org/pdf/1905.00468 (Section 2). Possible prior restatements in house-market preference-domain and permutation-pattern literature are not excluded. The result requires exactly opposite strict rankings and randomizes only the third agent. Independent scientific assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.
