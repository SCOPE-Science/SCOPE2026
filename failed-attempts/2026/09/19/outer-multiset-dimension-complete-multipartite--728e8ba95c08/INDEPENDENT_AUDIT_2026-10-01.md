# Independent audit — 2026-10-01

## Final claim

For a complete multipartite graph, outer multiset resolving sets are exactly complements of capacity-one choices across equal-part-size blocks, yielding odim=n-d, the factored resolving-set enumerator, basis count and fixed-order spectrum.

## Correctness — PASS

For an omitted vertex in part P_i the multiset representation is determined exactly by s_i=|S∩P_i|. Hence two omitted vertices collide exactly when their s_i values agree. This forces at most one omission per part and, with one omission, s_i=n_i-1, so omissions from different parts collide exactly when the part sizes agree. The partition-matroid description, n-d dimension formula and product enumerator follow. A fresh independent exhaustive replay over all 58 connected complete-multipartite types through order 8 matched the direct definition, structural criterion and full enumerator.

## Originality — FAIL

Originality fails decisively because an earlier published finding from 2026-09-18 already states the same n-d formula, the same complete characterization of all resolving sets, the same basis count, and the elementary-symmetric count for every complement size. That coefficient-by-coefficient enumeration mechanically implies the current product generating function and total count; the partition-matroid wording and fixed-order spectrum are immediate reformulations/corollaries.

### Equivalent formulations

Searches: Published-record semantic search for complete multipartite outer multiset dimension and resolving-set counts

Evidence: The 2026-09-18 record was retrieved and its full RESULT inspected.

Reasoning: Its all-set characterization is equivalent to the current capacity-one blocks; its elementary-symmetric counts are exactly the coefficients of the current factored polynomial.

### Broader coverage

Searches: Earlier 2026-09-18 published finding

Evidence: The prior result covers arbitrary repeated part sizes, not merely balanced or distinct-size endpoints.

Reasoning: It is at least as broad as the central current classification.

### Exact database or table

Searches: Prior coefficient-by-coefficient resolving-set enumeration

Evidence: The prior formula e_k((c_m m)_m) gives every complement-size coefficient.

Reasoning: Multiplying ∏(1+c_m m y) is only repackaging the same table.

### Claim versus prior implication

Searches: Full prior RESULT comparison

Evidence: The current odim, all-set characterization and basis count are verbatim-equivalent; the enumerator and spectrum are mechanical corollaries.

Reasoning: Under the audit standard, corollaries and equivalent formulations are covered even when the exact displayed polynomial is absent.

### Source inspections

- **Outer multiset dimension of arbitrary complete multipartite graphs** — Decisive coverage of the central claim and coefficient enumeration. Material read: Complete RESULT.md. Evidence: It states odim=n-d, the same omission criterion, basis count, and all complement-size counts.

Checked sources: Earlier published finding: Outer multiset dimension of arbitrary complete multipartite graphs (2026-09-18), full RESULT inspected; Klavžar--Kuziak--Yero, Further Contributions on the Outer Multiset Dimension of Graphs (2023); Assigned Git tree and fresh independent definition-level enumeration through order 8; Published-record semantic search for arbitrary complete-multipartite outer multiset dimension

Residual risks: No correctness risk affecting the final formula was found; the scientific rejection is coverage/value, not correctness.

## Scientific value — FAIL

The current product polynomial, partition-matroid label, root observation and fixed-order spectrum are clean, but after the earlier all-set classification and coefficient enumeration they are routine repackagings or short arithmetic corollaries rather than a remaining motivated mathematical gap.

## Conclusion

The finding is scientifically rejected because all three axes must pass; correctness evidence is preserved, but originality and value fail under the implication-based comparison.
