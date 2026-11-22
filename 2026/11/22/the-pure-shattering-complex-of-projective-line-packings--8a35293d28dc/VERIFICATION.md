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

The exact domain is the fifteen nonzero vectors of the binary four-space, with 35 projective lines, 56 five-line spreads, and 240 seven-spread packings. Run `python3 verify.py`, `python3 symmetry.py`, and `python3 verify_fano.py` to reconstruct the counts and Boolean traces. The first and third programs use different combinatorial descriptions of the same finite projective space; the second checks the 20160-element projective collineation group and support orbits. All checks were replayed from the files supplied here.

The proof of the universal statement about all supports on this fixed finite universe uses the exhaustive exact-cover enumeration plus the independent combinatorial sufficiency and obstruction arguments in `RESULT.md`. The programs do not establish any corresponding claim for larger spaces; no independent mathematical audit was performed.
