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

# Reproduction and limits

Use Python 3 with only its standard library. Run `python3 verify_direct.py` and `python3 verify_gaussian.py` from the extracted package folder; no external data or services are required.

`verify_direct.py` enumerates all 8,191 binary words through length twelve and checks three independent characterizations: direct scattered \((ab)^k a\) containment for each relevant \(k\), direct pair count and occupied-interior-gap statistic, and a separate weak-composition histogram. `verify_gaussian.py` independently constructs q-binomial polynomials by recurrence and compares the signed \((u-1)\) expansion against complete slot-product convolution for 175 content pairs; it also tests binomial moments and reflection symmetry. Both scripts terminate with a PASS message and raise on any failure.

The programs check only finite lengths; the proofs for all integer parameters are in `RESULT.md`, including the Gaussian product identity, occurrence criterion, and fixed-\(k\) asymptotic. No independent review or external certification is claimed.
