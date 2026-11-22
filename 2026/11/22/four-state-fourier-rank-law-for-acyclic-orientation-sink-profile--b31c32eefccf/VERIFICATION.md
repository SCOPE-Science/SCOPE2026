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

Run `python3 verify.py` with the Python 3 standard library. The script has no input data or dependencies. Its checks are:

- For every \(2\le n\le14\), independently enumerate all \(2^{n-1}\) orientation words and exact sink profiles, then calculate all \(2^n\) signed Walsh coefficients by an integer fast transform.
- Independently evaluate all these coefficients by the signed two-state matrix product and check every individual zero/nonzero outcome against the run-length criterion.
- Compare resulting ranks with both the four-state transition count and the closed linear recurrence.
- Compare the transfer coefficients with a separate signed independent-set sum for \(2\le n\le8\).
- Compare the transition-count algorithm with the recurrence for \(2\le n\le200\).

Observed result: `PASS`. The proof for arbitrary \(n\) is the matrix factorization and Cayley–Hamilton argument in `RESULT.md`; finite computations are not asserted to establish the infinite claim. No independent audit has been performed.
