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

# Verification and scope

The optional scientific Python dependencies used by the fluctuation checker are listed in `requirements.txt`. The exact finite-state checker uses only the Python standard library.

Running `python verify_exact.py` checks the reduced two-count recurrence against an independently written exact recursion on explicitly labeled available-edge sets, for every \(0\le a,b\le6\). It verifies the normalization and the displayed exact \(S_{4,4}\) polynomial.

Running `python verify_limits.py` verifies the conserved fluid expression and the exact quadratic-variation integral with symbolic differentiation/integration, then compares three independently simulated large finite populations against the claimed asymptotic mean and variance using a fixed pseudorandom seed. These stochastic checks have explicit tolerances and are illustrations, not infinite-dimensional proofs.

The analytic proof of the limits uses a density-dependent pure jump process with bounded quadratic variation on finite intervals, the deterministic terminal sandwich, and a stopped martingale central limit theorem. The lower-barrier stopping becomes negligible because the limiting terminal independent vacancy density is strictly positive. Results do not address arbitrary edge rates, the regime of an independent population of sublinear order, exact finite-time loss rates, or independent external validation.
