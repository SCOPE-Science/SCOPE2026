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

# Exact verification

Run `python3 verify.py` in the directory containing this file. The self-contained checker builds the regular icosahedral edge graph using exact squared distances in \(\mathbb Q(\sqrt5)\), constructs its 20 faces and the 60 directed-edge vertices of the regular truncated icosahedron, and verifies the 12 pentagonal plus 20 hexagonal supporting facets.

The 32 outward normal vectors give 16 antipodal pairs of great circles. In the affine chart of directions with positive last coordinate these give 16 distinct lines with 41 intersections (28 double and 13 quadruple). The Euler region formula certifies exactly 84 regions. Integer perturbation witnesses around these vertices yield 84 distinct exact sign patterns, which, together with sign reversal, exhaust all 152 spherical sign cells. This exact enumeration gives 132 cells with 20 illuminated vertices and 20 with 21. A direction on a boundary can be perturbed without losing any strictly illuminated vertices.

The script additionally verifies that each of 20 directions opposing an icosahedron face normal illuminates 21 vertices and that every truncated vertex is covered exactly seven times; weights 1/7 give fractional illumination 20/7. Summing 60 vertex constraints and the global 21-vertex maximum proves optimality. The optional ordinary-cover checks find a four-direction cover and rule out three covers using all 152 cell subsets.

All inequality signs and all combinatorial cell counts are exact. Floating point is not used in the proof's sign tests. Successful execution prints `EXACT_OK`. Computation covers finitely many algebraic incidences, not a continuous numerical sample; completeness rests on the proven cell count. Historical priority and any independent external audit are not certified.
