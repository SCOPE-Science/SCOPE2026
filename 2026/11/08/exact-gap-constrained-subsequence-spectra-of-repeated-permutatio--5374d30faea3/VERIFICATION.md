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

# Verification

The included `verify.py` independently constructs the set of query words satisfying each gap profile by a feasible-position state search, separately computes the polynomial coefficient sum by convolution, and checks the uniform alternating-binomial formula. Running `python3 verify.py` produced `VERIFY_OK uniform=1472 nonuniform=4000 example=23/27`. The 5,472 configurations include varied host repetitions, alphabet sizes, query lengths, positive local gap bounds and boundary regimes. The program is finite; the unbounded theorem is established by the phase-normalization and earliest-embedding proof, not by enumeration.

The mathematical comparisons are described in `REVIEW.md` and `AUDIT.json`. Novelty remains qualified by the possibility of earlier unindexed or implicit coverage. Independent audit and independent validation have not been performed.
