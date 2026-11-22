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

# Verification notes

The analytical verification is internal to `RESULT.md`: a full-rank truncated Vandermonde matrix proves the sole possible difference of moment-matched class infectivity weights; an exact divided-difference identity and derivative sign prove the all-pressure comparison; strict concavity proves the unique positive final-size root; and a binary infectivity coupling proves sharpness while keeping both marginals unchanged.

`checker.py` reproduces exact-fraction calculations for the three-susceptibility-class witness. It verifies the first two mixed moments are both one, the next moments are \(19/16\) and \(55/48\), and the root and attack-order inequalities. It also tests exact barycentric moment identities and same-marginal perturbations for each integer \(3\le k\le10\) and supplements this with numerical root comparisons for \(k=3,4,5\). A successful local execution printed `ALL CHECKS PASS`.

These tests are not an exhaustive search of infinite parameter families and do not substitute for the algebraic proof. They do not certify stochastic epidemics or mathematical originality. No independent audit or external validation was conducted.
