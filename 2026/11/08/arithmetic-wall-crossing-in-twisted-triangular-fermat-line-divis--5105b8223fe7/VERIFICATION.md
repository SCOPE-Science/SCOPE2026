---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PASS. With n≥2 invertible in k and a,b,c nonzero, the 3 families of n distinct geometric lines have vertices at the three coordinates and inner triple concurrence iff root parameters u*v*w=1, equivalent to abc=1. The normalization is the disjoint union (E_a+E_b+E_c)×P^1. Each pencil vertex contributes 1-[E_v]; nodes contribute minus the corresponding étale product, triple points contribute -2[E_a×E_b]. Thus [D]=3+LΣ[E_v]-Σ[E_v×E_w] off the wall, or 3+LΣ[E_v]-2[E_a×E_b] on it. Point counts and zeta follow from finite-field counting as a ring realization and exponentiating; verified F_7 n=3 (2,2,2) has N_2(r)=0 for 3∤r and 3 otherwise, giving 3 or 9·7^r-15. Independent direct projective-point enumeration in 3,856 small prime-field parameter cases agreed. No claim for char(k)|n; the proof, not finite tests, covers all stated fields and extensions.

## originality

PASS

PASS with historical-priority risk. The geometric three-pencil Ceva/Fermat concurrency is known and explicitly not new; the contribution is the simultaneous *ground-field finite-étale motivic normalization class*, two torsor-concurrency regimes, all-extension Hasse–Weil zeta and nonsplit example. Resultary semantic search returned nearby arithmetic twist/line-divisor records on different surfaces but no theorem implying the exact three-torsor plane divisor formula. Marchesi–Vallès treats geometric three-pencil classification, not the arithmetic realization. Scissors inclusion-exclusion is standard; its concrete application is an independently useful arithmetic arrangement calculation, subject to possible older aliases.

## value

PASS

PASS. Computing rational points and zeta for a geometrically reducible plane line arrangement with no rational component is a natural arithmetic-geometric invariant problem. The exact abc=1 wall and the infinite extension fields with only three rational points expose a meaningful distinction between geometric incidence and arithmetic descent; formulas determine all extensions rather than an arbitrary small case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
