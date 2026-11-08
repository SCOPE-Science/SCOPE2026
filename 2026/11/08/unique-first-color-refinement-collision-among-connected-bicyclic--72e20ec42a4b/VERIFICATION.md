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
Run `python3 verify.py` (Python 3 standard library). Expected output lines are `4 1 1 []`, `5 5 5 []`, `6 19 18 [[2, 0]]`, `CENSUS_OK`, `FAMILY_OK t=0..20`. The code enumerates all simple edge subsets of the required edge count through order six, tests connectivity, computes globally consistent color-refinement signatures, and uses exact adjacency backtracking for isomorphism. The family check verifies twenty-one sample parameter values; the proof of all parameters is symbolic. Historic priority is not certified; independent audit remains not performed.
