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

# Reproduction and verification

From a directory containing `verify.py`, run `python3 verify.py`. The direct, standard-library-only checker constructs reflexive closed neighborhoods on each labelled graph and computes both lower and upper approximations directly, without using the counting theorem. It enumerates all crown subsets through nine matched pairs and all corresponding undeleted biclique subsets through seven matched pairs, including explicit small-order exceptions. It compares the resulting distinct observations, complete multiplicity histogram, predicted nonfull upper-output classification, and two-nonfull complement cases. The executed output is `VERIFY_OK family_cases=15 crown_subsets=349524`.

The all-parameter proof is the five-step argument in `RESULT.md`, not a finite verification certificate. It uses only elementary set membership, a disjoint upper-output classification, an explicit complete list of two-nonfull cases, and a binomial fiber calculation. The formula is not established for arbitrary partial matching deletion, unbalanced bipartite graphs, or nonreflexive relations. This document does not represent independent external validation.
