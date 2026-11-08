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
# Reproducible verification

The provided `verify.py` is a standalone Python 3 source file. The proof in RESULT.md covers every integer \(m\ge2\), \(a\ge1\); this checker is a finite standalone implementation of the exact vertex-distance, support, contact-count and contact-barycenter formulas.

Run `python verify.py` in a directory containing this file. Its exact-rational portion uses the Python standard library only, enumerates all independent block supports in 274 parameter configurations and verifies 351,604 support-distance inequalities, contact support identities, contact counts, and barycentric minimax equalities, totaling 707,576 exact assertions. If NumPy and SciPy are installed, it also solves 70 separate constrained quadratic programs and compares their minimizers with the claimed exact centers. Both parts completed successfully in the delivered version.

No finite enumeration, numerical optimizer, or failed search is taken as a substitute for the all-parameter proof or as an independent mathematical audit. The original 2026 preprint full manuscript was not available to inspect; the absence of a prior matching theorem has only provisional status.
