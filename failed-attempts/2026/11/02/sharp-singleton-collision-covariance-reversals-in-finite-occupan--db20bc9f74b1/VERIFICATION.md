---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

By exchangeability it suffices to pair each singleton indicator with the match indicator for observations 1 and 2. The singleton can coexist with that match only when the matched category is different and there is exactly one occurrence of the singleton category in the other n−2 draws. This gives the joint expectation in (5), and subtracting the product of expectations gives (1). At n=2, the singleton count is twice the no-match indicator. Uniform substitution gives the sign of n−2m including zero; for two categories and n>=3 the conditional pair count on a singleton is exactly C(n−1,2), giving the binary factor and its roots. The diagrams are scoped to the uniform and two-category models respectively. Independent exact multinomial occupation-vector enumeration in `python3 /workspace/branches/independent_replay.py 3` matched the formulas in 96 cases. Frozen `artifacts/verify.py` exists and was read, not executed.

## originality

FAIL

Earlier indexed result SCOPE-9485777d7c83 uses exactly the same iid occupancy model and unordered pair count. It states the entire uniform singleton reversal (including the exact formula and equality case) and gives an identity for every occupancy score from which the nonuniform and binary formulas follow by direct substitution. The familiar neighboring literature is less decisive than this actual prior coverage.

## value

FAIL

The covariance question is natural and an accessible derivation is useful exposition. But the precise uniform reversal is already an explicit indexed case. The remaining displayed formulas and roots amount to immediate evaluation of its stronger all-score identity in the same model, not an independently useful unresolved boundary. No distinct surviving claim is established that would support a repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
