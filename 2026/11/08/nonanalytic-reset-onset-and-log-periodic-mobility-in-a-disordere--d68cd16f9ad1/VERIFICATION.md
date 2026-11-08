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

The analytical argument rests on the exact stationary branch recurrence, finite-ring balance, a quenched strong-law limit, two-sided geometric domination of a shifted lattice sum, the nonzero Euler-beta Fourier coefficient, and a logarithmic cutoff estimate. Those are proved in `RESULT.md`.

Run `python3 check_comb.py` using Python 3 with no external packages. On the packaged source it reports **36 passed assertions**: exact-rational finite-branch solutions, exact-rational stationarity on a heterogeneous four-site-backbone comb, high-precision fractional-power comparisons at distinct logarithmic phases, and high-precision critical inverse-log comparisons. Its finite checks do not certify asymptotics for every parameter choice.

For the illustrative choice \(\alpha=100\), \(\beta=1\), \(\rho=1/10\), the predicted phase amplitudes are approximately \(\Theta_{1/2}(0)=0.7202400\) and \(\Theta_{1/2}(1/2)=0.6451692\). The theorem that the amplitude is nonconstant follows from an exact nonzero Fourier coefficient, not this sample.

The stationary theorem is not asserted for simultaneous thermodynamic and zero-return limits. The full article associated with DOI 10.3390/e25111529 was not accessible during the primary-literature comparison, so external publication-priority checking remains appropriate. No independent audit or validation has been performed.
