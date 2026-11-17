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

# Reproducibility and limitations

Run `python3 verify_fan.py` with Python 3 and no external dependencies. `verification_output.txt` records one complete run. The program forms every matching directly from the graph edges, assembles all augmented mod-two boundary matrices, and checks the reduced Betti groups for \(3\le n\le18\). It also evaluates an independent exact matching-polynomial recurrence for \(3\le n\le300\) and checks the link residue counts.

The all-integer and all-parameter homotopy theorem is proved in `RESULT.md` through a path-matching recurrence and cone attachments; neither finite enumeration nor mod-two ranks alone establish it. Reproducible tests do not establish novelty or independent validation.
