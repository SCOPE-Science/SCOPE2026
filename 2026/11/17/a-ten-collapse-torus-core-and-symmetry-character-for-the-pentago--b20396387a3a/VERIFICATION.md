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

Execute `python3 verify.py` with Python 3 standard-library dependencies only. Its recorded complete standard output is in `verification_output.txt`. The script reconstructs the entire 15-vertex matching complex from the fifteen graph edges, checks the ten specified free pairs, a branching link in the original complex and the residual surface links, and verifies the explicit integral orientation cycle. It calculates signed chain and homology traces for every one of the twenty graph automorphisms and checks mod-two chain ranks independently.

The exact orientation chain checks each integer boundary coefficient, not merely an Euler characteristic or a floating-point rank. The surface classification argument in RESULT.md proves the integral homotopy claim. These checks do not prove global mathematical priority, establish results for other bipyramids, or constitute an independent external audit.
