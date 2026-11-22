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

Run `python verify.py` with Python 3.10 or later. The script uses only Python's standard library, enumerates all extension words directly through six old vertices, and independently checks the matrix dynamic program across all three-colour path words through eleven old vertices. It verifies both sharp equalizer classes, the all-order recurrence at thirty-four finite sizes, and the exact characteristic polynomial with integer matrix arithmetic. `verify_output.txt` records the expected deterministic output, concluding with `VERIFY_OK`.

The direct enumerator exhausts finitely many instances, not an infinite family. All-order correctness rests on the sorted-deficit comparison proved in `RESULT.md`, especially its monotonicity under arbitrary continuation and strict tie analysis. The cited integer-sequence tables cannot certify the argmin/argmax theorem; they are explicitly acknowledged as partial numerical precedent. Independent mathematical verification has not been performed.
