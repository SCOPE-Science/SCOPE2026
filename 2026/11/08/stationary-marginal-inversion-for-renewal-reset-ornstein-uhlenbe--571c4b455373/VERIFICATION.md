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

# Reproducibility and limitations

Run `python3 verify.py` with Python 3 standard library. The script performs 45 exact-arithmetic assertions: 17 exponential-reference Gaussian-moment identities, exact vanishing of the first three powers against a third derivative of a compact polynomial, a nonzero higher moment, two additional even-moment cancellation checks, endpoint normalization cases, and elementary stationary-age total-variation checks. It is independent of third-party numerical packages.

The full proof proceeds analytically via the renewal equilibrium-age identity, an Ornstein–Uhlenbeck Gaussian variance-mixture change of variables, Hausdorff moment determinacy and a monotone reconstruction of the reset survival function. The finite-moment counterexamples use compact smooth perturbations whose first prescribed polynomial moments vanish by integration by parts. The smooth inverse instability follows from a high-frequency derivative perturbation: the Gaussian-mixture input changes by order inverse frequency but the reset density has a nonzero limiting total-variation distance. The oscillatory averaging step is established by the standard mean of the absolute cosine function, not by the finite script.

The tests do not certify infinite-dimensional uniqueness, uniform limits, novelty, independent verification or any finite-sample statistical guarantee. The equilibrium-time convention is essential for arithmetic reset intervals.
