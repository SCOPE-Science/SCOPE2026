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

# Reproduction and limits

From a clean Python 3.9+ environment, execute `python3 CHECKER.py`. Expected output: `PIECEWISE_FOCUS_EXACT_IDENTITIES_OK 742`. The source uses only Python standard-library exact rational arithmetic. It verifies the polynomial branch derivatives, upper/lower switching roots, the composite ray return, the return regimes, and exact rational basin-area identities for each integer order from 2 through 15.

Separately, high-precision numerical event integration of 12 upper-half-plane excursions with k values 2, 3 and 5 and radii 0.5, 0.85, 1 and 1.2 confirmed crossing at the square of the initial radius to numerical tolerance. This numerical test is supplemental and is not needed to reproduce the analytical proof.

The results over all integers, all real initial points and infinite time follow from the explicit first integrals and monotone crossing-map proof in `RESULT.md`, not the finite checker or simulated orbits. The absorbing continuation at the origin is a hypothesis. The originating power-map identity is credited to the cited papers; only the stated full-plane geometry and exact quantitative classification are claimed here.
