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

The executable `verify.py` uses only the Python 3 standard library. It reconstructs every cylinder from its node prefix, then directly computes the optimal depth of a complete adaptive membership-query tree using the minimax recurrence over all possible leaf queries. A separate independent enumeration checks VC shattering for every subset of each small test ground set. Cases: branching two and heights zero through three, branching three and heights zero through two, branching four and heights zero through one; both the empty-augmented and nonempty classes are tested, for eighteen exact cases.

Execute with `python3 verify.py`. A successful run ends in `ALL_PREFIX_BALL_CHECKS_PASS 18 independent finite cases`. Checks of the induction's integer-floor inequality are included for heights two through one thousand; these do not constitute infinite verification.

The proof of all heights is in `RESULT.md`. No independent mathematical audit has been performed. The finite verifier does not certify historical priority or full first-order model-theoretic reductions.
