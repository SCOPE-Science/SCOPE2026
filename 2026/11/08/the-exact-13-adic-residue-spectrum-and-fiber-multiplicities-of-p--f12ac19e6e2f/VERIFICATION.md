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

# Reproducibility checks and boundaries

The standalone dependency-free Python file `verify_pell13.py` can be executed with `python3 verify_pell13.py`. It directly enumerates the Pell recurrence for the complete predicted least period at each modulus from \(13\) through \(13^6\); checks the seed matrix congruences, complete residue sets and per-residue multiplicities, and tests the branch distance identity for 1,120 bounded pairs.

Observed execution:

```
VERIFY_OK levels=1..6 max_period=799708 image_size_k6=371293 base_classes=13 isometry_pairs=1120
```

These are finite computational corroborations. The mathematical proof's unrestricted steps are the integral matrix congruence for \(A^{28}\), the matrix-binomial divisibility estimate, the Pell norm identity excluding derivative cancellation, and bijectivity of each branch at every precision. Verification of finitely many exponents and pairs does not constitute an infinite proof. Historical originality has a separate unresolved primary-source access risk; independent mathematical assessment has not been performed.
