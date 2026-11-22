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

# Verification and scope

Run `python3 check_multipartite.py` using only Python's standard library. It enumerates every vertex subset for fifteen nonuniform and singleton-shore multipartite cases with three to five shores, computes reduced mod-two homology, and checks the exact set of faces added by an edge deletion. This finite computation is independent corroboration and cannot certify the all-size theorem. The proof in RESULT.md gives the integral homotopy classification, signed lattice basis and primitive integral homology maps.

No independent mathematical audit has been performed.
