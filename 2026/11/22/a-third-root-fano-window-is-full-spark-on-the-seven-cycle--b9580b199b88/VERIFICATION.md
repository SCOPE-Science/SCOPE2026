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

# Reproducibility and verification

The positive result is certified by `ternary_full_spark.c` and `independent_ternary_check.c`. Both enumerate every \(\binom{48}{6}=12{,}271{,}512\) normalized maximal minor. The first uses rank-preserving elimination over the prime 2000000143; the second uses a separate prime 1300000003 and a mask-indexed Leibniz determinant algorithm without elimination. Both tests passed. Their deterministic results are proofs of nonvanishing over the complex cyclotomic field because a zero algebraic integer must map to zero under every ring homomorphism into a field.

The negative result is certified by the 64 rows of `binary_witnesses.csv`, one per binary sign word after global-sign normalization. `binary_certificates.c` finds each row and verifies vanishing at the six primitive seventh-root images, with an explicit coefficient bound ensuring exact lift. `direct_integer_checks.py` independently expands each displayed determinant over the integers and reduces by the seventh cyclotomic relation; all 64 are exactly zero. The same script independently spot-checks 300 positive minors over the integer group algebra. All checks passed.

`REPRODUCE.sh` is a standalone driver. The C tools require only a compiler supporting C11; the Python tool requires only Python 3 standard library. None of these checks relies on floating-point rank thresholds, untracked external data files, or an infinite/external certificate. The reported rank assertion is confined to dimension seven and the documented phase alphabet.
