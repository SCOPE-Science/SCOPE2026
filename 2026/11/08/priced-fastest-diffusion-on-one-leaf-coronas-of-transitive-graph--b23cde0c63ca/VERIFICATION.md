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

# Reproducibility and verification limits

The file `verify.py` is standalone source, using Python 3 with NumPy and SymPy installed. Running `python verify.py` from this directory yielded `VERIFY_OK 1263`.

The script reconstructs each weighted two-layer Laplacian and checks (i) the proposed formula for its second eigenvalue, (ii) exact budget saturation, (iii) positive semidefiniteness, (iv) representative comparisons against independently randomized, unequal allocations, (v) exact symbolic semidefinite identities on small sunlets, and (vi) predicted cycle ratios and budget shares. It uses fixed seeds and reports a failed assertion on a discrepancy.

The proof for all graph sizes and positive prices is analytical in `RESULT.md`. No finite test establishes uniqueness over a continuum, the absence of all earlier equivalent literature, or independent formal verification. No external audit has been performed.
