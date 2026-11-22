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

# Verification record

`python3 check.py` passed 417 exact rational assertions on 18 independent-Poisson multitype examples (1--6 types, 3 coefficient configurations each) and on the determinant of nine Beta-Hankel matrices. Each finite-model check obtains covariance by an exact deterministic mean/covariance recursion and extracts its highest-degree polynomial coefficient via exact finite differences; it checks the independently predicted universal expression. The determinant check performs fraction-preserving elimination and compares to the closed factorial product. The infinite-population theorem, all model-law quantifiers, asymptotic \(O(n^{-1})\) accuracy and the deep-type ratio limit are proved symbolically in RESULT.md, not certified by enumerating examples. No independent audit has been performed.
