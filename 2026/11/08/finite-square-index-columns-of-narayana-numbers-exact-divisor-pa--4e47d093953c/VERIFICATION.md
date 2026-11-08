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

Run `python3 verify.py` with Python 3 standard library. Expected successful output:

```text
VERIFY_OK square_indices=149 exact_divisor_families=4678 direct_scans_c=2..20 exact_binomial_c=2..6 nonsquare_Pell_witnesses=108 square_b4_b9_only_trivial=PASS all_comparisons_integer=PASS
```

The verifier constructs actual integer divisors, checks each parametrized row against the square criterion, checks exact counts and extrema, brute-force searches bounded ranges for \(2\le c\le20\), computes Narayana numbers with exact binomial arithmetic for \(2\le c\le6\), and checks explicit Pell constructions for nonsquare indices. This provides reproducible finite support but **not** a proof for arbitrary \(b\). The proof in RESULT.md supplies the unrestricted argument through exact factorization and Pell units. Independent mathematical audit: not performed.
