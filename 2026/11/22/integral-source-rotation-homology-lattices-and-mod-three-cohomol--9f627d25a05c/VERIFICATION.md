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

# Computational verification

Two pure-Python scripts are included. They require no third-party packages.

`python verification/quotient_orbit_chain.py 3 4 5 6 7` enumerates every allowed nonempty disjoint three-coordinate cell, chooses its cyclic orbit representative, tracks product-orientation signs, constructs each cellular boundary over \(\mathbb F_3\), and computes its rank. The expected mod-three Betti vectors are respectively \((2)\), \((1,5)\), \((1,1,10)\), \((1,1,1,21)\), and \((1,1,1,1,42)\). The first two cases are outside the quotient theorem's \(n\ge5\) fundamental-group assertion and verify the exceptional low-dimensional behavior only.

`python verification/cyclic_lattice_jordan.py 5 6 7` instead works with the unquotiented labeled top cells and their signed boundaries over \(\mathbb F_3\). It obtains kernel ranks \(29,61,125\); the ranks of \(g-1\) are \(19,40,83\), and of \((g-1)^2\) are \(9,20,41\). Thus the cyclic Jordan block multiplicities (size one, two, three) are \((0,1,9)\), \((1,0,20)\), and \((0,1,41)\), exactly as the theorem predicts.

These programs test finite cellular signs and modular group actions. They do not compute integral Smith forms, provide canonical integral cycle bases, establish the theorem for arbitrary \(n\), or supply independent review. The infinite proof rests on the explicitly stated classical complete-graph wedge theorem, two-periodic group-ring resolution, integral \(C_3\)-lattice classification, and Serre/UCT arguments.
