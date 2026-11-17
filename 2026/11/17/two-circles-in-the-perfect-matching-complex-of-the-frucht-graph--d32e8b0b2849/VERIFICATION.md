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

# Exact finite verification

Execute `python3 verify.py` from the same directory. The script uses only the standard library, reconstructs all facets and all possible nerve faces, verifies the stated face vectors, confirms each elementary-collapse pair is a genuine free face, and proves the residual graph is connected of cycle rank two. It also independently enumerates six-edge covers out of all 262,144 subsets to check the eight facets and identifies 29 nonextendible disjoint edge pairs. `verification_output.txt` is the recorded stdout of a successful local execution; the proof is the program together with the explicit finite algorithms and mathematical nerve argument, not the log alone. NetworkX was used only as a separate optional check of the standard Frucht isomorphism type, not as a dependency of the certificate.

Boundaries: all computations concern the specified 12-vertex graph; no assertions of automatic generalization or independent external certification are made.
