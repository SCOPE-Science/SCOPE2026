---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Reconstructed the synchronous open-neighbor update on K_a join I_b. Monochromaticity of the six original colour classes is exact: while a class remains at its current colour it contributes zero to its own successor count; clipping each original class size at 2 preserves every at-least-two predicate after every transition. The finite quotient has precisely 3^6=729 clipped mass patterns. Independently enumerated all 729 at exact integer arithmetic and obtained F^7=F^4 on every nonempty class, 122 three-cycle-attracted patterns, 31 distinct EGF monomials and sharp first entry 4. Direct labelled small-graph dynamics and exact coefficient calculations corroborate. Symbolic coefficient weights 1,z,U and 1,w,V give Phi=U^3 exp(3w)+3U^2 exp(2w)[V+z(V+w)]+3V^3(z+z^2)+z^3(V+w)^3; coefficient extraction yields all labelled basins. The fixed-a Dirichlet-style occupancy union bound for three large independent-class occupancies gives the claimed p_a and uniform error. Boundaries a,b>=1 and explicit G_(2,5) sharpness respected; all-a,b proof relies on quotient exactness, not extrapolation from 752877 labelled finite states. RESULT.md blob 6f65013775aab7121f9816c4e3353ecfa7b5e076 and finite_certificate.py blob 367aba932fada56d23bf97eae6b4e6a4d244bd61 actually inspected.

## originality

PASS

Best-of-knowledge independent exact attraction basin count and fixed-clique oscillation law for the 3-color, threshold-2 complete SPLIT graph; retain meaningful archival priority risk.

## value

PASS

The exact universal four-step sharp first-entry bound, complete labelled transient attraction-basin generating function for two independent graph-size parameters, and nonmonotone fixed-clique-size limiting oscillation fractions are mathematically structural, not an arbitrary sample or standard textbook deduction. The natural system is a complete split network, and the exact basin census can be reused for parameter comparison and probabilistic initialization. Its value does not rest only on the small finite certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
