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

Execute `python3 weak_vertex_verifier.py` using the standard Python 3 library. The script compares rational mean absorption times obtained from two differently organized finite-state recursions and compares the exponential-race product for the marked-last event for 44 parameter pairs with \(3\le N\le13\). It checks the uniform-rate identity separately. The program uses exact fractions for these finite-state calculations; its large-size floating-point product evaluations illustrate slow approach toward the limiting constant but do not certify an asymptotic theorem.

The analytical proof supplies the infinite-population statement: ordinary pure-birth concentration, convergence of integrated hazard, upper/lower coupling for ordinary completion, and uniform integrability of completion time. It assumes the slow rate lies in \((0,1]\), and the mean limit requires a strictly positive finite limiting product \(\rho_N\log N\).

An independent scientific audit or external reproduction has not been performed. Literature priority is provisional.
