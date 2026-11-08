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

# Reproducibility and limits

Run `python3 check_stern.py` in a standard Python 3 environment. The independently computed Stern recurrence is compared with the two-permutation child model, for all 55 parameter pairs with 2 <= m <= 12 and 2 <= h <= 6, for each dyadic depth 0 through 9. State-space reachability and the aperiodic self-loop are also tested. The stored expected transcript is `check_output.txt`.

These are **finite verification tests**. They do not establish the universal theorem: the infinite proof invokes the exact lifted modular braid relation, elementary generation of the modular unimodular group, transitive Markov mixing and a binary decomposition of arbitrary cutoffs. The proof gives no explicit modulus-uniform saving exponent. Self-review has passed; independent audit has not been performed.
