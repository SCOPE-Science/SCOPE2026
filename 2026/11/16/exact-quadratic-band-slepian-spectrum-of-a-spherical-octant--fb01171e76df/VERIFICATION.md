---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The full-sphere and conditional orthant Gram matrices of bases (1,x+y+z,xy+yz+zx) and (x−y,x²−y²,z(x−y)) follow from 3-variable absolute-Gaussian gamma moments. S3 representation splits the nine-dimensional V2 into 3 trivial and 3 copies of its 2d standard type, giving one cubic and a repeated cubic; generalized eigenvalues of (C/8,B) exhaust the spectrum. Symbolic checker orthant_band2_verify.py reconstructs full 9×9 moments, Shannon trace 9/8, exact B,C blocks and determines disjoint rational root isolating intervals via Machin-series π bounds; independent numerical generalized eigensolves confirm the six values and κ=362.61139026488. Rigorously isolated distinct intervals certify unique extremizers, not just approximate eigenvalues.

## originality

PASS

Best-of-knowledge: substantive comparison of the exact claim and implications with closest published scientific results, including generalizations and potential near-equivalences; residual priority risks explicitly retained.

## value

PASS

An exact rationally isolated nine-mode spectrum of the all-right spherical triangle is a natural continuous Slepian benchmark for low-band reconstruction, and the unusual small minimum eigenvalue determines a sharp stability invariant. The full-dimension orthant result supplies related general formulas, so the finite benchmark is valuable only insofar as its exact root separation and extremizer ordering are separately certified rather than presented as a wholly new symmetry reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
