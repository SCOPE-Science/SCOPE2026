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

# Exact finite verification

Execute `python3 verify.py` in this directory. The code is a fully specified standard-library exact-integer certificate. No external data, tolerances, random seeds, or numerical transforms are required.

The group is the full \((\mathbb Z/3\mathbb Z)^{3n}\) with the positive-root Fourier convention. The algorithm enumerates the legal prefix-restricted words, confirms their hook-length totals, applies the full tensor Fourier transform in the integral basis \(1,\omega\), counts zeros only when both coordinates vanish, and proves every Fourier output accounted for by the factorization described in `RESULT.md`.

A second computation directly sums root-of-unity residue counts for all frequency degrees at most three, including 2049 distinct frequencies at width four. It also directly checks 67 other frequencies per width, all character-conjugation identities, the exact integer Parseval identity, and the full eight-frequency cubic-witness list.

Expected successful output:

```text
n=1 tableaux=1 frequencies=27 zeros=0 rank=27 low_frequency_tests=27
n=2 tableaux=5 frequencies=729 zeros=0 rank=729 low_frequency_tests=233
n=3 tableaux=42 frequencies=19683 zeros=1134 rank=18549 low_frequency_tests=835
n=4 tableaux=462 frequencies=531441 zeros=3996 rank=527445 low_frequency_tests=2049
exact_cubic_witness_list_verified: 8
ALL_CHECKS_PASS
```

These checks are exhaustive for the stated finite group Fourier transforms through width four; they do **not** prove a formula for larger widths. There has been no independent audit.
