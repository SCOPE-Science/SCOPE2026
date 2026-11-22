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

# Reproduction and scope

Run `python3 kautz_verify.py` using Python 3 with no third-party packages. The program constructs the labelled directed Kautz graph, enumerates all Boolean states for five cases, classifies first periodic entry using the explicit two-step recurrence test, computes exact independent integer first-entry counts, and asserts agreement. Its complete-case results have shell vectors \((5,3)\), \((5,50,9)\), \((5,968,1422,1701)\), \((6,10)\), and \((6,3768,322)\) in the order printed by the script. The code separately tests 4000 seeded random trajectories on the 36-vertex Kautz graph of degree three and word length three.

The program does not claim exhaustive verification at graph orders beyond the specified finite cases, nor does it prove the scalar critical limit. The mathematical proof derives those conclusions without extrapolating a sample. No independent external audit has been performed.
