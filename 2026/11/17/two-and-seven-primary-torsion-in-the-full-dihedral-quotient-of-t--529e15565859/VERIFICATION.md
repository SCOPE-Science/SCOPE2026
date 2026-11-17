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

# Reproducibility

All files required to reproduce the finite chain computation are included. Run `python verify.py --verify certificate.json` using Python 3.8 or newer with no third-party modules. The checker constructs the full geometric-orbit chain complex rather than a naive simplicial quotient, verifies Burnside counts and \(\partial^2=0\), replays exactly 1,705 unit pivots and checks the final differentials. The certificate stores pivot dimensions, row/column identifiers and signs, together with all expected numerical outputs. The modular-rank checks at two, three, seven and eleven are independent consistency checks and not used as a substitute for integral cancellation.

The group-theoretic assertion of trivial fundamental group is proved separately by the fixed-reflection argument and Armstrong's theorem; the checker does not certify it. The equivariant identification of the graph-associahedron boundary with a representation sphere is an explicit convex-radial mathematical argument, not a machine check. No higher homotopy classification, arbitrary-length extension, or independent audit is asserted.
