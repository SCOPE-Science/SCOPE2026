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

Run `python3 verify_orbit_exact.py q4_certificate.json` and `python3 verify_full_states.py q4_certificate.json` with Python 3, SymPy, NumPy and SciPy. The former independently reconstructs all 222 exact orbit probabilities and compares every reduced fraction; the latter re-enumerates all 65,536 labelled spin configurations, 720,896 admissible directed transitions and ten singleton recurrent classes. It checks every full-state weighted harmonic equation using exact rational arithmetic, all six Hamming-distance seed classes and the exact ensemble means. Both tests passed on the included source files and certificate.

The output is an exhaustive finite proof-checking computation, not an external audit or a universal statement in the cube dimension. The third-party literature comparison is documented in `REVIEW.md` and `AUDIT.json`, with an unresolved possibility of unindexed prior equivalent calculations.
