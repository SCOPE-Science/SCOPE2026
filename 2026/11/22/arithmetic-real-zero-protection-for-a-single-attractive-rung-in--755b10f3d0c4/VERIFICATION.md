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

# Reproduction and limitations

Run the included `verify_replica_rung.py` using Python 3.10+ and SymPy: `python verify_replica_rung.py`.

It independently computes the two-rail fugacity polynomial from all pairs of admissible independent sets and compares it with the squared-path formula on every marked site for lengths 1 through 7 and four exact rational rung activities. It also uses SymPy's exact Sturm count of distinct real roots for all marked sites on lengths 1 through 12, for activities \(1/4\), \(1\), \(3/2\), and \(2\); each count is compared with the stated gcd census. Its expected outputs are `IDENTITY_CHECKS_PASSED 112` and `ROOT_COUNT_CHECKS_PASSED 312`.

The computation is finite and does not certify the theorem for unbounded length. The analytic proof uses a weighted Jacobi matrix, exact trigonometric path roots, elementary divisibility, and the fact that sums of real squares vanish only when both summands vanish. The nonreal root motion is justified by a local analytic expansion, not by numerical plotting. A third-party review has not been performed.
