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

The standalone program `artifacts/verify.py` uses only Python's standard library. Run `python3 artifacts/verify.py` with Python 3.10 or later. The expected terminal marker is `VERIFY_OK`.

The program recreates the prescribed Möbius-ladder graphs and both edge orbit representatives. It checks bounded-independence face counts and square numbers through eight rungs. At eight vertices it enumerates every total-cut face; it exhaustively verifies the acyclic Morse orientation on the entire nonempty face poset and checks the exact elementary relative collapse pairs. The 4-simplex/sphere distinction at eight vertices is not extrapolated. These finite checks are a supplement to the all-order argument about connected graph bounded-independence complexes, the absence of odd cycles of length at most five for larger ladders, and Alexander duality.

The integral primitive-kernel assertion is structural: the inclusion of three-cycle kernels is saturated in a coordinate chain lattice, then duality and universal coefficients transfer the map. No external audit, expert endorsement, or formal proof assistant certification is claimed.
