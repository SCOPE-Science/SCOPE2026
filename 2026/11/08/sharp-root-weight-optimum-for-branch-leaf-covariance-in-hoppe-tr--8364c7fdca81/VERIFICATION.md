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

Run `python3 verify.py` with Python 3 and no external dependencies. The verifier uses `fractions.Fraction` to enumerate every parent-choice vector for each integer \(n\) from 2 through 8 and all eight positive rational root weights \(1/3,1/2,1,3/2,2,7/3,5,17\). It reconstructs the root degree and the number of leaves from the parent vector without invoking the theorem. It verifies probability normalization, two means, the covariance and each temporal contribution. It also tests the sharp maximum against several alternative weights for every integer \(n\) from 3 to 149.

Result: `PASS 1567 independent exact assertions`.

The script provides finite consistency tests only; the identity for arbitrary real positive root weight, uniqueness of the optimizer, and the weight-scaling asymptotics are established in the accompanying proof, not by computation.
