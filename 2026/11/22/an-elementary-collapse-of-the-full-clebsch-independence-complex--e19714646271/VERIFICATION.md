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

# Standalone verification

From a directory holding the two artifacts, execute `python3 verify_clebsch_quotient.py collapse_certificate.json`. Python 3.10+ standard library only. The successful full run reports `CLEBSCH_FULL_SYMMETRY_QUOTIENT_19_COLLAPSES_PASS`.

The program reconstructs the even-parity folded five-cube, proves the sharp full automorphism group order, enumerates its 392 labeled nonempty independent faces and 19,992 strict flags, rebuilds the quotient of flag orbits using a generating set, checks the 39 cell representatives and incidences, verifies exact integer cellular boundary identities, then checks all 19 free-face pairs and the remaining vertex. Cell data and proof are finite, not extrapolations. The separately included JSON is a complete deterministic collapse witness, not a log from a different computation. This self-review is not an independent mathematical audit.
