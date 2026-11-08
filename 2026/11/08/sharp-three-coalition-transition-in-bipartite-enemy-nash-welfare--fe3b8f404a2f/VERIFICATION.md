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

# Verification record

The proof in `RESULT.md` supplies the infinite-domain justification: enemy-free cliques, coalition merging, exact finite-dimensional product, convexity of the log-product, and monotone crossing. The executable `verify.py` independently enumerated all 4,140 partitions at 8 agents and all 115,975 partitions at 10 agents, reconstructed all permissible enemy pairs, and confirmed the unique maximizing partition in both cases. The same script uses exact integer arithmetic for all reduced allocations through 80 peripheral agents per side and checks the first crossing at the 8-to-9 transition.

Run `python verify.py` with Python 3; no third-party dependencies. The printed final line is `PASS` if all assertions hold.

The finite enumerations do not establish completeness for arbitrary population size; the analytic proof handles all integers \(q\ge2\). No formal machine proof, independent audit, or external validation has been performed.
