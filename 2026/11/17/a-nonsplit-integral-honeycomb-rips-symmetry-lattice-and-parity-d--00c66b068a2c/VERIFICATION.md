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

For every L>=5, the relative Y formed from centered tetrahedra retracts to the honeycomb graph H_L; only the 2L² alternating color triangles lie outside. Each pair of black/white relative 2-cells has the same facial boundary c_f; the unique integral facial relation is sum_f c_f=0 (fundamental class of torus). Thus H2 is exactly the kernel whose per-face coefficient sums are a single integer, with basis T=sum_f e_f^W and s_f=e_f^B-e_f^W, rank L²+1. The group action follows from orientation and color-exchange signs: g(s_f)=delta*epsilon*s_(gf), g(T)=delta(T+((1-epsilon)/2)S). Translations force a potential equivariant integral section T+aS with a integral; a color-flipping orientation-preserving 60-degree rotation requires 2a=1, impossible, while a=1/2 splits rationally. Coinvariants reduce to 2T=0, 2s=0, L²s=0, giving Z/2 for odd L and (Z/2)^2 for even L; rational invariants in H1,H2 vanish, so the finite quotient is rationally acyclic in positive degrees. The proof explicitly distinguishes algebraic coinvariants from integral homology of the orbit space. The checker sources reconstruct orientations and Smith forms for L=5..8, which are finite corroboration only.

## originality

PASS

PASS best-of-knowledge: exact earlier full-text honeycomb theorem establishes the same nonequivariant T² wedge L² spheres and relative two-color face model, but expressly leaves integral symmetry action undetermined. A homology rank does not specify a nonsplit Z[Gamma]-extension, parity coinvariants or rational full quotient. Related square torus grids and affine Coxeter Rips complexes treat other graph metrics/scales; neither mathematically dominates this lattice result.

## value

PASS

The complete integral symmetry extension is a natural next invariant after the known underlying topological type. It distinguishes an integral nonsplitting invisible to rational representations, with a sharp parity jump in algebraic coinvariants and a striking rational quotient consequence. This is structural equivariant topology, not arbitrary finite enumeration or a rephrasing of the Betti numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
