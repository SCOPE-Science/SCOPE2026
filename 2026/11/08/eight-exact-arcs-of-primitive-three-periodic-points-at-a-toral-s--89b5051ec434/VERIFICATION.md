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

# Reproducible checks and boundaries

Run `python CHECK.py` in a Python 3 environment with SymPy available. The checker uses exact rational linear algebra and exhaustively enumerates 512 three-step branch/wrap codes at \(\eta=1/3\). It verifies that twelve positive-dimensional affine itinerary cells combine into exactly the eight geometric segments in the theorem. It then tests 59 rational interior points on each of eight segments by exact threefold iteration, including the correct order of the two modulo reductions. The final message is `PERIOD_THREE_RESONANT_EIGHT_ARCS_OK; cells=12; arcs=8; exact_points=472`.

The analytic proof separately factors all four types of \(\det(I-DH_\eta^3)\) to rule out positive-dimensional cells for nonresonant parameters and treats the all-right branch by an orbit-barycenter argument. The checker supplements the finite classification; it is not a substitute for the parameter-uniform determinant reasoning or the non-overlap proof of the arclength identity. The code does not assess external originality or constitute independent audit.
