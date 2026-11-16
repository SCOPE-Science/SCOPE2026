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

The symbolic proof derives every Fourier multiplier from a permanent and a signed rook expansion. The 3-adic congruence proof is valid for all sizes \(n=3^a-1\) and \(n=3^a-2\), with \(a\ge1\), and separately for \(n=4,5\).

For the finite statements, run:

```text
python3 check_signed_permutation.py signed_perm_rank3_zeros.csv signed_perm_rank4_spectrum.csv
```

The checker tests all 512 zero-position boards in size three, all 65,536 in size four, compares two exact permanent evaluations, and checks all 19,683 direct signed-permutation character sums in size three. The 27 signed eigenvalue levels in size four are exact, but were not directly evaluated over all 43,046,721 ternary characters; grouping by zero-position boards with the proved character multiplicity \(2^{n^2-r}\) makes that larger enumeration exhaustive. These are mathematical verification procedures, not external independent certification.
