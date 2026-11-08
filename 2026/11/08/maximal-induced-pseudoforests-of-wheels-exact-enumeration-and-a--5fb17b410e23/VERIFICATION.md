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

# Reproducibility

Run `python verify.py` using Python 3.10 or newer with only the standard library. The verifier independently builds every wheel on rim orders \(3\) through \(16\), enumerates all nonempty induced vertex subsets and checks each component's edge count against its vertex count. For each feasible subset it checks inclusion-maximality by separately adding every omitted vertex. It compares all size profiles to the theorem. It then computes the bivariate rational generating function's coefficients via a separate recurrence for rim orders through \(180\), comparing each size profile, deletion-size spectrum, and extremal multiplicity.

Actual execution:

`VERIFY_OK wheels_n=3..16 direct_nonempty_vertex_subsets=262114 maximal_induced_pseudoforests=1504 rational_and_gap_n=3..180 PASS`

The program tests only finite orders. The unrestricted statements and asymptotic are consequences of the written combinatorial and analytic proofs, not of the execution log. No independent audit was performed.
