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

For the exact 12-vertex Franklin graph with cycle edges and even-index +5 chords, the independent-set face numbers are (12,48,76,45,12,2), independently enumerated. Inspected check_franklin.py builds 195 independent faces, an exhaustive 95-pair acyclic Morse matching with one critical vertex/four critical triangles, and signed B2/B3 ranks 37/35. Twenty induced three-edge matchings give octahedral 2-cycles. Four specified cycles plus B3 form rank39 primitive lattice by all unit Smith invariants, hence integral H2=Z4 and a genuine integral basis. All 48 group automorphisms act by signed integer matrices; check_franklin.py explicitly verifies 2304 products, generator closure and determinant-one action, primitive vector (1,1,1,1) fixed, character mean 1 and squared norm 2, central half-turn trace -2 and S4×C2 splitting. The quotient has rational cohomology Q in degrees 0 and 2 because the finite group invariant rational H2 line has dimension one; integral quotient cohomology not claimed. Independent networkx confirms the Franklin distance-three graph is isomorphic to Franklin itself and the known VR-at-scale-2 complex is an isomorphic independence complex; independent matrix closure confirms 48 elements and fixed vector.

## originality

PASS

PASS solely for the additional exact integral 48-element automorphism representation/three generator matrices and primitive globally fixed class/rational symmetry quotient. A strong identical-object PRIOR Resultary October 25 theorem already proves H2=Z4, exactly 20 octahedral supports, 8+12 orbits, eight-orbit integral spanning and twelve-orbit rank3, under the equivalent VR_{<=2}(Franklin) formulation; these assertions are NOT novel here. The earlier full source and verifier compute generators and orbit lattices but do not state the entire signed integral group representation, character decomposition or ordinary quotient cohomology; these are meaningful but modest refinements. If a full earlier result elsewhere calculates the character, O would fail.

## value

PASS

Given the natural full 48-element graph automorphism symmetry, the exact integral representation and invariant primitive line refine a known geometric orbit-lattice classification and identify rational topology of its ordinary orbit space. This is an independently useful symmetry invariant, not mere repetition of previously known octahedral orbit counts; the accepted contribution is narrowed to the representation/quotient, although whole final claim is factually correct.

The dated certificate retains the supplied scientific assessment, sources and limitations.
