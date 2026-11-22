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

Invoke `python3 verify_pascal.py` with Python 3; it has standard-library dependencies only. Compare its complete JSON standard output byte-for-byte against `certificate.json`. It enumerates the 60 hexagons modulo dihedral equivalence, applies the 120 projectivities, computes all Pascal chord intersections in exact arithmetic modulo five, checks the third Pascal intersection, confirms the orbit sizes 30/20/10 and the ten-image sixfold fiber table, enumerates the 31 points and lines, and obtains 15 ordinary double and 10 ordinary triple intersections. The extension-field point counts are algebraic consequences of the reduced rational-line decomposition, not computational extrapolations. The scheme-theoretic line degeneration multiplicities and unrelated sextuples have not been checked.
