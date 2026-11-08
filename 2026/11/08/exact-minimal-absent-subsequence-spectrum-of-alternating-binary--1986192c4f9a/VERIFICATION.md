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

# Verification and limitations

The mathematical proof reduces minimal scattered-subsequence absence to a weak-descent condition and two local pattern exclusions, and derives the complete bivariate series using an explicit four-state transfer matrix. The finite verifier, `verify.py`, independently constructs scattered-subsequence membership by matching, then checks all single-letter deletions of every binary candidate through the stated finite bounds. It also compares distributions with a distinct state-counting dynamic program and tests numerical recurrence coefficients.

Run `python3 verify.py` using the included standalone source. Only Python standard-library modules are needed. The verifier's finite upper bound is not used to justify the all-integer theorem; the exact embedding identity, deletion lemma, and matrix argument supply that proof.

Novelty has been assessed against the named publications and consulted research records, but not independently audited and not certified globally. No external independent validation has been performed.
