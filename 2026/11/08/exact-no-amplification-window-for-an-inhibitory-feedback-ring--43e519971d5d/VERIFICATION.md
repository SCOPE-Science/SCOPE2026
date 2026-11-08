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

From a directory containing `RESULT.md` and `verify.py`, install NumPy if needed and run `python verify.py` with Python 3. The script performs 36 exact rational principal-minor PSD comparisons across six example orders, 12 exact determinant-zero endpoint checks, and 168 direct numerical eigenvalue and bound comparisons across orders 3 through 16. The expected output begins with `PASS`.

The general proof is analytic and appears in `RESULT.md`. Exact computations are finite and are not an exhaustive check of all integer orders or real parameters. No third-party code or database is needed for the checker; NumPy is a declared numerical dependency. Historical priority is provisional because one potentially relevant reactivity article was available only through its abstract.
