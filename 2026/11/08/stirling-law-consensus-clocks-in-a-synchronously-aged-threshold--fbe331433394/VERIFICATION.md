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

# Mathematical and computational verification

The proof checks the prefix invariant separately at the interior and endpoint of the path; the strict threshold and frozen synchronous updates are necessary. Fresh independent activation coins give the exact Bernoulli coupling; standard permutation insertion gives the Stirling distribution. The tail and moments use recurrence asymptotics and Borel–Cantelli; the large-depth limit uses the Lindeberg central limit theorem and distribution-function inversion. These steps are in the accompanying `RESULT.md`.

`verify.py` requires only standard Python 3. Running `python verify.py` checks 3,887 exact equalities comparing a separate finite-state Markov recursion with the closed Stirling law, plus independent exhaustive permutations of up to eight symbols. The observed output was `VERIFY_OK 3887 exact equalities and independent exhaustive permutation counts`.

These finite checks do not establish universal or asymptotic claims; those depend on the written proof. The result is not a theorem about the random asynchronous update convention in the initiating paper. Independent audit has not been performed.
