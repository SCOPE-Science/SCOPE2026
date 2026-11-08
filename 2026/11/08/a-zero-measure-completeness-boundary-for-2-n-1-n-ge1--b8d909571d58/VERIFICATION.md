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

# Verification and limitations

The proof of the infinite and almost-everywhere statements is in `RESULT.md`. It establishes the exact missing-interval identity, excludes all scalings above one-half, constructs an infinite explicitly complete dyadic subset, and proves almost-everywhere equidistribution of dyadic multiples using exact orthogonality, a square-index subsequence, Borel--Cantelli and Weyl's criterion.

Run `python3 verify.py` beside the documentation. The standalone script uses only Python's standard library and exact rational arithmetic. Its tested assertions include 1,330 rational parameters for the exact gap identity through index 22, all dyadic binary-basis terms for \(1\le k\le32\) and \(1\le n\le84\), all rational parameters above one-half of denominators 2 through 60 for the explicit obstruction, and 12 deterministic binary fractions with absent integer intervals at index 180.

Observed output:

```text
GAP_IDENTITY_OK rational_parameter_pairs=1330 n=1..22
DYADIC_BINARY_BASIS_OK k=1..32 n=1..84
UPPER_HALF_OBSTRUCTION_OK denominators=2..60
FINITE_GAP_EXAMPLES_OK samples=12 n=180
VERIFY_OK exact_rational_arithmetic=true infinite_a.e._claim_proved_analytically=true
```

Finite calculations are not proofs of the almost-everywhere limit, measure zero, or universality; these conclusions rely exclusively on the proof. No independent audit or external mathematical certification was performed. The exact structure and dimension of the successful-parameter set are left open.
