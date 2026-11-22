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

Run `python verify.py` in the same directory as `FINITE_CERTIFICATE.json`. Standard-library exact rational computations construct the actual generator transitions and independently check the pointwise drift for all labelled configurations at \((r,n)=(3,2),(3,3),(4,2)\), 1012 total. For \((3,2)\), the integer stationary vector in `FINITE_CERTIFICATE.json`, normalized by 8100, obeys every stationary balance equation for the exact 27-state generator. It yields the three explicitly claimed unequal finite composition probabilities, and all nine exact part/opinion means. The analytic proof of the limiting claim instead uses uniform \(L^2\) synchronization and the full stationary polynomial moment recursion at fixed \(r\); finite computations alone are not a substitute for these arguments.

The generator normalization was checked explicitly: the accelerated quadratic variation tends to twice the multinomial covariance, and the generator's half-Taylor prefactor produces diffusion coefficient one. The drift coefficient is \(1-rp_a\), yielding unique stationary moments \((r-1)!\prod_a k_a!/(r-1+\sum_a k_a)!\). No claim is made for unequal part sizes, more than one frozen agent per part, nonstationary convergence, or finite exact Dirichlet-multinomial stationarity. Independent external scientific review is not performed.
