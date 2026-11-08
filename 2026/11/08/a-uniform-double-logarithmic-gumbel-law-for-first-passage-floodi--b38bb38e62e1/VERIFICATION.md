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

## Reproduction
Run `python verify.py` with Python 3 and NumPy/SciPy available. The complete checker was executed from its accompanying package path and returned `VERIFY_OK 33396 assertions`.

## Actual checks
Exact rational products of the \(k-2\) intermediate exponential rates agree with \((k-1)^2\) for \(2\le k\le80\). The tilted means, rate inequalities, and bounded tilted variances are checked. The checker independently forms upper-bidiagonal phase-type matrices, evaluates survival probabilities for representative \(m\) and \(2\le k\le18\), and compares the \(k=2\) special law with an Erlang-two survival formula. It also checks exponential exploration boundary-edge counts for small complete graphs.

## Mathematical limits
No finite checker verifies the asserted infinite Gumbel or point-process limits. Those are justified analytically in RESULT.md using a uniform tilted exponential-moment bound. Source access was incomplete for certain earlier literature; historical priority is not independently certified. No independent audit has been performed.
