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

Run `python3 verify.py` in any standard Python 3 environment. It directly constructs every circular ladder on \(8\) through \(18\) vertices corresponding to rim orders \(4\) through \(9\), enumerates all \(349440\) sensor subsets, explicitly performs closed-neighborhood observation and unique-neighbor forcing, and checks the final observed count against the distance criterion and labelled coefficient formula. It identifies \(190\) failed sets. A separately implemented formal-series recurrence checks the complete polynomial through rim order \(160\) and compares Lucas totals through the same order. It also checks the \(11\)-regular third-power neighbor count for orders \(7\) through \(30\) and the triangular-prism boundary. Expected output begins `VERIFY_OK`.

These are finite experiments only. The distance-to-stopping lemma, cyclic gap count, rational generating function, exact probability formulas, and Poisson window have separate unrestricted mathematical arguments in `RESULT.md`. No code exhausts infinitely many graphs or establishes publication novelty. Verification state: self-reviewed, without independent mathematical audit.
