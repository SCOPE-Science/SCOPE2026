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
# Exact finite certificate

Run `python3 verify.py` with Python 3 and its standard library, without optimization flags. The expected stdout is in `verification_output.txt`. The program reconstructs the Petersen graph as the disjointness graph of two-element subsets, constructs the cubical cells and every codimension-one incidence, and removes only a surviving square and its unique surviving cubic coface. Its assertion that no cubes remain certifies the two-dimensional spine. The check also verifies connectivity of the spine and Euler characteristic 20. The passage from the cubical model to the continuous configuration space uses Prue–Scrimshaw; the degree-one integral information uses Ko–Park. The program does not independently prove the cited general theorems or certify historical priority.
