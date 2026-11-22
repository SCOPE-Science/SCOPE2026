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

Restrict the ellipsoid support function to viewing plane: shadow squared semiaxes are eigenvalues of Q=diag(B+η,B,B−Δ) compressed to N⊥. Its 2×2 discriminant is exactly G²=(η−(η+Δ)x²−Δ y²)²+4ηΔ y². We independently assembled the 2×2 compression at six nonpolar normals/two parameter sets and matched this formula to numerical precision. G<tη implies transverse x,y=O(sqrt(η/Δ)); scaled u,v satisfy |1−(u+iv)²|²<t² in the limit. A bounded local chart and algebraic zero-area boundary permit dominated convergence even at t=1; the two hemisphere charts give factor 1/(2π). The branched map w=z² has Jacobian area conversion |C_t|=(1/2)∫_{|w−1|<t}|w|^(−1)dA; polar integration yields the stated E,K formulas, Φ(1)=1/π and Φ small/large limits. Differentiating K as k↑1 yields logarithmic slope coefficient 1/(2π). The open two lobes meet only at boundary at t=1, so the statement correctly distinguishes open from closed connectivity.

## originality

PASS

Older triaxial projection formulas and fixed-anisotropy near-round tails include the compression geometry, but do not give the singular simultaneous η-varying tolerance, normalized conditional Cassini law, or elliptic crossover singularity. The prior fixed-section quartic eccentricity result is a different sampling object and limit. The classical Cassini curve is not asserted new.

## value

PASS

A small non-axisymmetric perturbation changes near-round shadow probability from a quadratic to linear window law. The explicit interpolation across its singular topological transition and conditional viewing-direction law are independently motivated geometric-probability results for shape inference, rather than a bare elliptic-integral table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
