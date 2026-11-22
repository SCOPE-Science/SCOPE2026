# Review: sharpness of the ternary tagged-part internal congruence

## Correctness — PASS

The exact input \(\nu_3(\Lambda^m_{k,\ell})\ge2m+6+u_k+u_\ell\) for all \(m,k>\ell\) is Li–Tang's published Lemma 5.2(ii); its proof and quantifiers were read and checked against the recurrence. The two finite input columns of \(B\) appear explicitly in the source. Recomputing all fifteen exterior-square minors finds a unique weighted minimum \((2,1)\) with value three; all others have value at least four. This makes the leading term noncancellable at every induction level, starting from \(698368\cdot3^7\). The first two subsequence coefficients translate the vector minor into \(-D_m\); the first two sample indices exclude a stronger uniform modulus for any integer multiplier. The companion exact checker verifies the critical finite matrix arithmetic and several low-depth eta-quotient cases. The infinite theorem is deduced mathematically, not from those finite checks.

## Originality — PASS, with residual priority risk

The Li–Tang manuscript, read in its complete publicly available HTML presentation, states a **lower bound** for \(\nu_3(\Lambda^m_{2,1})\) and proves existence of a congruence modulo \(3^{m+5}\); it does not state equality at every depth or maximality of that modulus against all multipliers. Lower bounds by themselves do not imply equality. The new step is an exact, uniquely minimal exterior-square transition of the first two columns, giving both equality and a leading-unit recurrence for every \(m\). Singh–Barman's earlier \(\mathrm{PDO}_t\) work states limited-depth divisibility congruences rather than this all-depth internal sharpness. Indexed searches for exact determinant valuations, aliases, and optimality did not find equivalent statements. An unindexed equivalent, or an unstated deduction in other papers, remains possible. A related sharpness result for the separate \(8\cdot3^m\) progression uses a different extraction family and does not imply this one.

## Mathematical value — PASS

The specific invariant is motivated directly by whether a published infinite-family internal congruence is best possible. This proves an **all-depth** natural sharpness theorem in a previously unresolved family, with exact normalized leading signs, rather than a small computational improvement or an arbitrary truncation. The fifteen-pair certificate has a structural role: one term forces the minimum valuation at every step. No result is claimed for unrelated progressions.

## Sources, evidence and remaining limits

Primary: Li–Tang, arXiv:2611.15164v1, Theorems 1.1, 1.2(ii), 3.2 and Lemmas 4.4, 5.2(ii), first published November 11, 2026, https://arxiv.org/html/2611.15164v1 . Background: Singh–Barman, arXiv:2307.04687v1, https://arxiv.org/abs/2307.04687 ; Lin, Journal of Number Theory 184 (2018), DOI:10.1016/j.jnt.2017.08.020 . Access limits: the Li–Tang full HTML was inspected; Singh–Barman's abstract, introduction and early theorem statements were inspected; Lin's original article was available in bibliographic/abstract form only. Priority is not asserted as independently certified.

Self-review: passed. Independent audit: not yet performed.
