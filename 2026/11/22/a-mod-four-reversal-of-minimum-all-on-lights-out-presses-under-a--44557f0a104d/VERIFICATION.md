---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1,
  "record_status": "passed"
}
---
# Reproducibility

The finite-word proof in `RESULT.md` reimposes the original all-on equations after deriving four-periodicity, so both necessity and sufficiency hold for arbitrary stated size. Each of the two complement constraints contains different coordinates; they generate four labelled patterns, all of Hamming weight \(n\).

Run `python3 verify_balance.py` using the standard library. The script builds the closed neighborhood of each vertex, performs exact binary elimination on its toggle syndrome while tracking press subsets, finds a representative of the all-on syndrome, and adds all kernel elements. It compares the full resulting set of vectors with the four claimed residue patterns. The standalone check covers \(n=20,24,28\); it is finite corroboration, not the all-order proof.
