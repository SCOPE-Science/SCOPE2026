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

# Verification of the metric pair-spectrum theorem

The independent finite verifier is supplied as `artifacts/verify.py`; it runs with standard Python 3 without packages. Its recorded output is `artifacts/verification_output.txt`. Running `python3 artifacts/verify.py` should end with `ALL_CHECKS_PASS`.

The verifier reconstructs the three four-class weight rows from the defining triangle inequalities and separately enumerates every admissible distance profile for \(m=0,1,2,3\), then every ordered pair of these profiles under each specified new-new distance. It checks the exact formulas, checks the channel inequalities through \(m=16\), and uses exact fractions for the limiting expressions. No probabilistic simulation or floating-point inference is involved.

**Proof boundary.** These finite computations confirm all local coefficients and small cases. The claimed formulas for every \(m\ge1\) require the mathematical argument that no new coordinate can have distance-one witnesses in two distinct old blocks, and that this is the only cross-block restriction. The proof of this step appears in `RESULT.md`. The asymptotic fractions follow algebraically from leading polynomial coefficients. No independent mathematical audit has been performed.
