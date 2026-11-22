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

# Verification instructions and scope

Run `python check.py` with Python 3 and SciPy installed. The checker evaluates the exact rate-mixture integral in two independent analytic/numerical representations: a Gaussian-tail reduction to one dimension and a direct integration over an exponential rate difference and its independent minimum. It checks the exact zero-discount success probability, positive discounted probabilities and mean reset times, the small-discount logarithm and large-discount exponential prefactor, and a representative interior improvement over extreme reset rates. The result is a deterministic PASS count or an assertion error.

The analytical proof in `RESULT.md` establishes the infinite-time claims and their precise parameter domain. Numerical agreement is corroborative only: finite quadrature does not prove the logarithmic asymptotic or rule out another optimizer. The first-passage Laplace formula conditions on the two hidden Poisson rates, and the reset formula assumes those rates are renewed after every positional reset. No independent scientific audit has been performed.
