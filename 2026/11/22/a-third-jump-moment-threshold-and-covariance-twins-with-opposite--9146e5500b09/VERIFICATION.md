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

Run `python checker.py` in Python 3. The script uses only standard-library rational arithmetic, binomial coefficients and exponentials. It independently generates the stationary raw moments from the jump generator and compares their centered chronological contrast with the factored theorem expression exactly for 64 parameter/law choices. It verifies the two strictly positive burst distributions' first two moments agree while their third raw moments differ, validates the exact opposite coefficient signs at the common contraction, and checks representative positive time lags. It also handles the complete-reset sign and calculates the interior threshold only when its existence condition holds.

The mathematical proof in `RESULT.md` establishes the infinite-law and continuum-time theorem. The checker is an auxiliary finite test, not a computer-assisted exhaustive proof. Independent audit remains unperformed.
