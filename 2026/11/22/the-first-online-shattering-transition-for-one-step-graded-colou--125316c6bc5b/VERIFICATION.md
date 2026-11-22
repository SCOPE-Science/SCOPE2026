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

Run `python3 artifacts/check.py` from the extracted package root using Python 3 with the standard library. The program checks that the semantic hypotheses are distinct; computes exact online dimensions by exhaustive splitting of the finite active-hypothesis set for all \(q=2,3,4\) and \(d=1,2,3\); computes VC dimensions by exhaustive traces for \(q=2,3\); and verifies every branch of the explicit full depth-\(q+1\) mistake tree for \(2\le q\le9\). It finishes with `VERIFY_OK`.

The all-parameter mathematical proof appears in RESULT.md: a matrix sign obstruction for the uniform VC upper bound, a complete root-query count that prevents a degree-two perfectly balanced split, and an explicit degree-three mistake tree. Finite cases cannot certify the infinite family; the analytic proof does not rely on extrapolation. No independent mathematical audit or general-purpose formal proof assistant validation has been performed.
