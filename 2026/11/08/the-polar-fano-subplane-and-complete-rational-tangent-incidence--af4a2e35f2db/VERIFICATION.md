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

The complete classification follows from the displayed equation, derivative calculation, a 21-element symmetry orbit and the genus-three Serre bound, plus seven finite-field evaluations and Fano-plane incidence. The two accompanying standalone Python programs verify finite identities and incidence counts independently in different irreducible-polynomial presentations of the field of eight elements.

Run `python3 verify_tangents.py` and `python3 verify_symmetry.py` in the same directory. Neither program downloads external material or requires third-party packages. Each raises an assertion failure if any checked identity does not hold. The finite computations corroborate, but do not replace, the mathematical argument.

The theorem applies only to rational tangents of the displayed Klein quartic in characteristic two over the field of eight elements. Published earlier results on its 24 points, classical flexes and Fano incidence design remain prior work. Historical priority and independent proof audit remain unperformed.
