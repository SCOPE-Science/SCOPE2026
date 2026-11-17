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

# Verification and exact scope

Execute `python3 verify.py` in the extracted directory. No third-party Python dependencies are needed. The test reconstructs each graph from part transfers, checks the independent conjugate-coordinate edge criterion, tests a fixed explicit lexicographic domination witness for sizes 1 through 150, and replays all nine size-eight four-part folds. Every comparison is made on the current induced graph. The terminal six-vertex graph is verified to be the complete graph minus three disjoint edges; its flag complex is the octahedral two-sphere.

The accompanying `verification_output.txt` records the actual result. Finite tests support but do not replace the universal domination proof in RESULT.md. No computations outside the package are needed for the stated finite certificate. Independent audit is not performed.
