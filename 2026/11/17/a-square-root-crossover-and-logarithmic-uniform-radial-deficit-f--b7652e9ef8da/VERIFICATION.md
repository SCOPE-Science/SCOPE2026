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

The included `verify.py` uses the Python standard library. Run `python3 verify.py` from the directory containing the script.

It enumerates all fine harmonic triples for dimensions 2 through 5, directly constructs the two coordinate blocks, checks squared Euclidean radii with integer arithmetic, compares each shell multiplicity with the exact combinatorial formula, and verifies the factorial-ratio representation. It also evaluates stable finite shell weights at dimensions 100, 400 and 1200, checking normalization and global bounds.

The observed check result is `HARMONIC_RADIAL_LOG_PASS exact_triples=34152 numerical_profiles=3 exact_shells=14`. These computations cannot prove the statements for all dimensions or the weak limit; the exact and asymptotic estimates in `RESULT.md` provide the proof. No external independent validation was conducted.
