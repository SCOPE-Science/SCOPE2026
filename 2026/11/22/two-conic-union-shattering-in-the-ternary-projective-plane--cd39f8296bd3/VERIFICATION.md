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

Run `python3 verify_arcs.py` and `python3 verify_quadratics.py` using only Python's standard library. Both executables directly rebuild their own mathematics: the first enumerates projective points, lines, four-arcs and symmetry classes; the second enumerates full-rank quadratic forms and all Boolean traces independently. The expected success lines begin with `ARCS_ORBITS_PASS` and `QUADRATIC_CENSUS_PASS`.

The group-orbit argument checks all six-, seven- and eight-point supports via exactly eleven representative traces. The second implementation checks all \(2^{13}=8192\) supports directly, every exceptional seven-support and every inclusion-maximal support. Those checks constitute finite exhaustive verification, not a sample or an infinite-field proof.

The result does not establish publication priority, an all-field classification, or an independent mathematical audit.
