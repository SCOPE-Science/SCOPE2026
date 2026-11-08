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

# Reproducible checks and limits

The theorem concerns inclusion-minimal **ordinary** dominating sets. The packaged program `verify_minimal_dom_tensor.py` uses graph adjacency and closed neighborhoods to test candidate sets, independently generating each structural family for comparison. Exhaustive cases are \((2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5)\). Larger generated-set-only tests are \((3,8),(3,11),(4,7),(5,6),(6,8)\).

Exact output observed on executing the included program:

`VERIFY_OK exhaustive_instances=11 candidate_subsets=1419077 dominating_sets=1412493 minimal_sets=2231 generated_instances=5 families=PASS coefficients=PASS gap_spectrum=PASS`

Run `python verify_minimal_dom_tensor.py`; Python 3 is the only prerequisite. Finite enumeration is not a general proof, and the checker does not attest originality or independent external verification.
