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

# Verification of signed reachability law

Run `python3 check.py` in this directory with Python 3.9 or newer. The script uses exact rational arithmetic and enumerates edge orientations directly, computing directed reachability by graph search. The replay outcome was `VERIFY_OK 710 exhaustive weighted-orientation and rational identities`.

The check covers \(n=1,\ldots,6\) and \(p\in\{1/4,1/3,1/2,2/3,3/4\}\). It checks exact joint probabilities, coefficientwise signed corrections, normalization, mean, pair covariance where defined, and total variation. These finite computations are not a certificate of the general theorem. The unbounded-\(n\) statements follow from the explicit four-type decomposition, coefficient sign comparison and binomial concentration in `RESULT.md`.

No independent audit has been performed.
