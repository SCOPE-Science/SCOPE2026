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

# Verification scope

The proof consists of exact algebraic identities, density of irrational rotations, elementary polygon geometry and convergence of a Taylor expansion; it does not rely on a finite experiment for infinite-angle claims. The supplementary pure-Python `verify.py` can be run with `python3 verify.py` and requires no third-party packages. It independently iterates the original branch-defined map and compares the predicted strict itinerary, exact period and polygon support data for all 153 reduced rational angles with denominators at most 31, plus 400 strict interior/exterior samples at one irrational angle. A successful execution printed `ALTERNATING_ISLAND_CHECK_OK rational_angles=153 rational_interior_samples=21215 irrational_samples=400`.

The symbolic number-theoretic reduction of the order of \(-e^{i\alpha}\), the density argument, and all-parameter continuity are verified in the analytical proof of `RESULT.md`, not by randomized sampling. Floating-point tolerance near exact side boundaries is a numerical limitation; no boundary sample is used as an analytic certificate. The theorem intentionally excludes boundary point itineraries and does not classify other components.
