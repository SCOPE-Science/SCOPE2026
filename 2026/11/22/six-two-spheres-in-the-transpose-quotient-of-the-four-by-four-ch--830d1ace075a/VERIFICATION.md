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

# Verification of the finite calculation

Execute `python3 verify.py` in the directory containing the extracted files, using Python 3 standard library only.

**Exact checks:** enumerated 208 nonempty chessboard faces with counts (16,72,96,24); all strict face flags and their transposition orbits give quotient barycentric-cell counts (125,586,768,300); all signed integral boundary-square compositions vanish; mod-two ranks in degrees 1,2,3 are (124,462,300); 124, 462 and 300 integral unit-pivot cancellations leave residual ranks (1,0,6,0), proving no integral torsion; an independent fixed-point Burnside calculation confirms Euler characteristic 7. Final checker marker: `VERIFY_OK`.

**Topological steps not implemented by this finite checker:** the published chessboard connectivity bound gives simple connectivity of the covering complex; Armstrong's theorem kills the quotient fundamental group using a fixed diagonal rook vertex; Hurewicz and homological Whitehead turn the computed homology into a six-two-sphere wedge. These are cited and explicitly used in the proof. No larger boards or homeomorphism type are tested or claimed.

Independent mathematical audit has not been performed.
