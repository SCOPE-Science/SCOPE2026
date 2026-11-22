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

# Verification and reproducibility

The claim is the exact positivity-horizon and sharp ratio theorem for degree-two and degree-three exponential Taylor steps on finite directed cycles with at least four vertices and strictly positive rates. The proof in `RESULT.md` treats all finite dimensions, all positive rates and all nonnegative timesteps. It needs no random sampling or limiting computational enumeration.

Execute `python3 verify.py` with standard Python 3. The checker independently builds each generator matrix, uses exact rational arithmetic to form powers, and compares all formula entries for cycle lengths four through nine. Its recorded successful output in `verification_output.txt` includes 52,032 entry comparisons, 7,488 row-sum checks, a cubic-root bracket, 2,240 floating-point tests straddling sharp horizons, and explicit rate-family checks. Supplementary numerical checks are not a proof of infinitely many dimensions or rate values; the entry enumeration and monotonicity/sign arguments in `RESULT.md` establish that result.

Exact hypotheses: the rates are finite positive real numbers, the generator has exactly one directed outgoing edge per state and the chain is homogeneous in time. Positive rates in the two limiting families tend to zero but remain positive at every tested instance; the universal bounds themselves are strict. The numerical check uses finite precision only for root bracketing and supplementary boundary stress tests. The endpoint result does not imply positivity of intermediate Runge–Kutta stages, improved accuracy or nonlinear strong-stability preservation.

No independent mathematical audit has been performed.
