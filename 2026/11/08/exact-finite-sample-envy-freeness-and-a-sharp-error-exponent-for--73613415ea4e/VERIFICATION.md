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

# Reproduction and evidence limits

Run `python3 verify.py` with a Python 3 installation using only the standard library. The program checks six exact rational probabilities, an independent two-good order-statistic identity, six direct simulations with a fixed local seed, and the sign and numerical precision of the analytic saddlepoint parameters. The checker was run against the embedded program; it terminated with a PASS result.

The finite formula is proved by bilateral Laplace-transform inversion, rather than by simulation or enumeration. The sharp asymptotic uses exponential tilting and a local central limit theorem; the implemented finite numerical checks are not an independent proof of the limit. A second, separate numerical convolution of the single-good piecewise-linear density, with exact CDF bin masses and mesh \(1/2048\), matched the analytic probabilities for \(m=1,\ldots,12\) within \(1.2\times10^{-7}\). This independent discretization is corroborative only.

No independent scientific audit has been performed. Publication priority beyond the inspected literature and indexed research records is not certified.
