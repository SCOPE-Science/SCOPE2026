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

# Verification

Run `python3 verify_folded_hom.py` using Python 3 with no external dependencies. The included `verification_output.txt` is the successful replay and can be reproduced from the embedded source.

The verifier enumerates every one of the 1,920 source-to-Clebsch graph vertex maps for \(n=5\), independently derives each pair of possible target positions from graph adjacency, and checks every binary alternative cube subset against the independence criterion. For \(n=7\), the same checks use a deterministic sample of 12 out of 322,560 maps, and the exact cell enumeration formula is checked arithmetically. Mod-two homology checks on cyclic independence links cover \(n=5,7,9\). This finite sample is not an exhaustive verification for all odd \(n\); the general theorem follows from the algebraic and incidence arguments in `RESULT.md`.

The proof's use of the standard cubical flag-link curvature theorem is explicit; no independent audit or formal verification is claimed.
