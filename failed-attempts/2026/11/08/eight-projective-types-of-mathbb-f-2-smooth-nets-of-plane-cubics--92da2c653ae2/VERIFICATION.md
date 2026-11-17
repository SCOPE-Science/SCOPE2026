---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Geometric smoothness of a ternary characteristic-two cubic is equivalent via Euler identity and Jacobian partial quadrics to absence of a nonzero common projective root. The degree-four Macaulay multiplication map S_2^3→S_4 is onto iff the three quadrics form a regular sequence, so an exact binary rank15 test suffices for smoothness over algebraic closure. Independently tested 1023 nonzero cubic masks: 336 smooth; exhaustive addition of smooth cosets generates 5544 pencils and 864 smooth nets, and all 168 GL3(F2) coordinate transforms split these into five orbits size168 and three size8. Reconstructed all five point-count spectra of the eight representative nets. This is an exhaustive finite classification with algebraic-closure correctness, not mere F2^r point scans.

## originality

FAIL

A published October 18 2026 result explicitly gives the identical complete projective and arithmetic census of F2-smooth ternary cubic nets: 336 smooth forms, 5544 pencils, 864 smooth nets, eight PGL3 orbits in 3x8+5x168 distribution, stabilizer orders21 and1, all five rational-point spectra, no F2 rational base point. Candidate’s different mask ordering and chosen bases represent the same subspaces and orbits. Originality FAIL despite a correct independent calculation.

## value

FAIL

The classification is a natural, worthwhile mathematical problem but the complete enumerative answer and its point spectra are already published; the candidate merely independently replicates that census and provides alternate representatives, not a new invariant or demonstrably different classification. Value of the claimed new result FAIL.

The dated certificate retains the supplied scientific assessment, sources and limitations.
