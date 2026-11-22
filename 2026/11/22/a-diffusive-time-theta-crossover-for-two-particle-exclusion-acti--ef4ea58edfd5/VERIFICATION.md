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

Run the following scripts in this directory using Python 3 (no external packages):

```sh
python3 verify_event_moments.py
python3 verify_green_limit.py
```

The first script constructs the complete unlabeled particle-pair Markov chain and propagates the first two marked-jump counting moments, without using the reflecting-gap eigenbasis, checking 70 finite size/time inputs (size 3 through 16). The second checks 248 exact rational reflecting-gap Poisson equations (size 3 through 250), independently compares the already-published long-time variance formula, and evaluates 12 diffusive-time finite-size tests. Both passed in the research package.

These finite numerical and rational checks are **not** proofs of identities for arbitrary sizes. The analytical arguments in RESULT.md are the proof of the time-resolved covariance law, its all-size limit, and its asymptotic expansions. Independent scientific audit has not yet been performed.
