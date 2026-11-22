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

The included `verify_cubic_fibers.py` implements arithmetic in the binary and quartic finite fields and exhaustively enumerates all rank-one square-zero perturbations of each irreducible cubic companion matrix. It checks the exact trace-dependent number of tripotent decompositions, without assuming the claimed projective parametrization when counting. It prints `IRREDUCIBLE_CUBIC_TRIPOTENT_FIBERS_OK` on success.

Reproduce with `python3 verify_cubic_fibers.py` using a standard Python 3 installation; no third-party packages are needed. Tested cases: two irreducible cubics and 42 rank-one candidate tests over \(\mathbb F_2\); twenty irreducible cubics and 6300 candidate tests over \(\mathbb F_4\). These are complete finite tests in the specified fields only. The general mathematical proof is in `RESULT.md` and independently does not assume an exhaustive finite check.

Independent audit: not performed.
