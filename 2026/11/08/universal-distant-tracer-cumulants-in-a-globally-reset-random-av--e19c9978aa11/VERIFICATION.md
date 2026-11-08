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

# Verification details

Run the standalone `checker.py` with Python 3 and SymPy installed. It checks exact algebraic recurrence identities for the truncated exponential-age law through cumulant order ten, recovers the stationary factorial coefficients, and reproduces the finite-time second- and third-order expressions stated in RESULT.md. It also checks the Poisson jump-count moment recursion through order eight and selected rapidly vanishing fourth-moment tail sums for stopped-ancestor localization.

The principal infinite-volume convergence is an analytic proof: an individual backward ancestor has an annealed nearest-neighbor Poisson jump law; truncation at a distant boundary changes a tracer by an amount bounded in every fixed moment by a vanishing Poisson tail; truncated graphical windows are independent when separated; the common reset-age mixture then yields the result. The code does not verify the general graphical representation or prove infinite-order uniformity by enumeration, nor does it certify publication priority.

Direct scientific consistency check: the derived second connected plateau at finite time, \(v^2r^{-2}[1-2rt e^{-rt}-e^{-2rt}]\), agrees with Santra–Singh's Eq. (42) at unit spacing. The stationary third and fourth plateaus are \(2(v/r)^3\) and \(6(v/r)^4\). Tests on finite Poisson tails are illustrative only. Independent audit has not been performed.
