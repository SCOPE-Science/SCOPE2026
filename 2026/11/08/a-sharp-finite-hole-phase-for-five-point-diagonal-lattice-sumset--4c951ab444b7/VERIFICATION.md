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

# Reproducibility
Run `python verify.py` with Python 3.10+ in the extracted directory; the script uses only the Python standard library and integer arithmetic. It independently forms repeated sumsets, enumerates polygon points from inequalities, compares exact hole locations and the minimum-length function, and verifies sharp saturation including the preceding degree. Its captured output in `verification_output.txt` reports 119 parameter-degree tests and 64,855 polygon lattice points.

The finite domain is \(2\le m\le8\) and \(0\le h\le16\). This does not certify the infinite theorem; see the complete symbolic proof in `RESULT.md`. Independent scientific audit has not been performed.
