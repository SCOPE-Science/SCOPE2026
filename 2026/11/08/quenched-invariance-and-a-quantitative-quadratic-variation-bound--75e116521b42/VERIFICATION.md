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

The analytic proof is in `RESULT.md`. Its critical steps are (i) binomial parity and a uniform binomial atom bound, (ii) an annealed quadratic-variation estimate, (iii) bounded differences across independent full time slices, and (iv) the martingale functional central limit theorem.

Run `python check.py` in the directory containing the supplied files. Its deterministic, exact-integer exhaustive calculations for horizons one through five passed 84,143 assertions, including the fair-environment mean-square identity, block replacement Lipschitz bounds, and binomial-coefficient parity. This is an independent finite diagnostic, not an infinite proof.

The theorem is restricted to mutually independent time-slice vectors, uniformly elliptic individual Bernoulli parameters, and fair independent input signs. The result is a quenched limit statement but has not received independent mathematical audit. Priority beyond the cited primary literature is not established by a negative search alone.
