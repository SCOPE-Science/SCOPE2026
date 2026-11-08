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

Run `python verify.py` and `python verify_certificate.py` in the same directory as `orbit_certificate.json`. Both perform exact finite-field arithmetic and assert all four orbit-size distributions before printing `VERIFY_OK`. The first program enumerates all canonical objects, verifies their pivot structure, closure, radical-square dimensions, and complete orbits under generating substitutions. The second replays a list of all forty explicitly supplied orbit representatives, checking orbit size, pairwise disjointness, and coverage. No random sampling or nonstandard package is involved.

The finite proof uses the published exhaustive normal forms (arXiv:1812.03576, Propositions 7--8); that prior theorem is a stated premise rather than a result independently certified by the code. The generating-substitution argument and the exhaustive parameter enumeration turn the finite searches into complete orbit certificates for the stated fields. The checked outputs are \(11\) orbits over \(\mathbb F_2\) and \(29\) over \(\mathbb F_4\).

No independent audit or external formal verification has been performed. No result beyond these two finite fields is claimed.
