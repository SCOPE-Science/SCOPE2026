---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The standalone `verify.py` constructs cycle graphs and their graph distances directly, tests the original paired-disjunctive condition, and decides perfect matching by a generic recursive search. It independently computes the proposed polynomial coefficients using a rational-denominator recurrence rather than the proposed cyclic-run description.

Direct exhaustive graph checking covers every nonempty vertex subset for all orders \(3\le n\le17\), totaling 262121 candidate subsets and 4136 qualifying sets. Exact-arithmetic checks cover \(3\le n\le250\) for the five-residue minimum-set multiplicities, support, and top coefficients. Executing the packaged file returned:

```text
VERIFY_OK graph_orders=3..17 candidate_nonempty_subsets=262121 paired_disjunctive_sets=4136 rational_coefficients_orders=3..250 minimum_residue=PASS support=PASS leading_coefficients=PASS
```

The arbitrary-order assertions rely on the proof in `RESULT.md`; finite computation cannot establish those assertions for all orders. Literature-priority checks were limited by inability to obtain the complete original 2023 paper. No independent mathematical audit or external certification has been performed.
