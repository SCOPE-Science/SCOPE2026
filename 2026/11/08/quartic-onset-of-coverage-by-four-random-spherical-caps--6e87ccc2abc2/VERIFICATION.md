---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: Four caps cover iff the convex hull of their unit centers contains a centered ball of radius cos(w). Tetrahedral Euler inequality and inradius/circumradius rigidity give threshold cos(w0)=1/3, equality only at two oriented labeled regular tetrahedron SO(3)-orbits. In the trace-free symmetric deformation chart, three off-diagonals enter linearly and two diagonals quadratically; the feasible five-volume equals 19683sqrt(3)π/512 δ⁴, and the eight-dimensional Jacobian is 2048/243. Multiplying two orbit volumes 8π² and dividing by (4π)^4 yields 81sqrt(3)/(4π)δ⁴ and 16sqrt(3)/π ε⁴. Independent differentiation and full Gram determinant corroborated constants; analyticity, local stability, compactness, and dominated convergence prove the limit.

## originality

PASS

PASS, best knowledge: Finch studies the identical four-random-cap probability but provides bounds away from the optimal tetrahedral threshold and does not give the exact quartic onset constant. Bürgisser–Cucker–Lotz give general sphere covering bounds and hemisphere-plus exact formulas; older deterministic tetrahedral cap multiplicities hold for fixed centers, not random near-optimal configurations. The five-dimensional anisotropic local-volume coefficient is not a known corollary of these inspected results.

## value

PASS

PASS: Four equal caps are the minimal finite random sphere-coverage setting, with a rigid unique tetrahedral threshold. The exact probability exponent and prefactor quantify a nontrivial mixed linear/quadratic rare-event geometry and provide a sharp benchmark for spherical random covering asymptotics; it is neither a mere deterministic covering radius nor a generic dimension count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
