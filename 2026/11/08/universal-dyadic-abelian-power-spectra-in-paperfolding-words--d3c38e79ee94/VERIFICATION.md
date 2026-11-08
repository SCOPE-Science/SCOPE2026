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

# Reproducibility and proof checks

Run `python3 verify.py` from a directory containing the accompanying program. Python 3 standard-library functionality is sufficient. The check performed on the enclosed program returned:

```text
VERIFY_OK assertions= 3154986 exhaustive_instruction_prefixes=256 long_instruction_patterns=6 checked_lengths=1,2,4,8,16,32,64,128
```

The verifier computes paperfolding symbols directly from their 2-adic valuation formula, not by assuming a substitution or a fixed instruction sequence. It exhausts the \(256\) choices of eight initial instruction signs over all eligible four-block windows within a prefix of length \(256\), then evaluates six periodic instruction patterns across \(65{,}536\) starting positions each and the eight stated dyadic lengths. Exact integer checks include fourth-power exclusion, the three-value block-sum support, and the repeated halving identity on finite sample indices. The square/cube and Parikh probability comparisons use a finite tolerance of \(0.0035\), explicitly encoded in `verify.py`.

The logical steps requiring infinite reasoning are checked in RESULT.md: the even/odd decomposition, the alternating-sign obstruction to equal nonzero adjacent block sums, the no-four-equal-run property for the Boolean indicators, and existence of natural densities by valuation truncation and conditional-parity equidistribution. Finite tests cannot establish any of these universal statements on their own. Neither independent proof review nor external mathematical validation was performed.
