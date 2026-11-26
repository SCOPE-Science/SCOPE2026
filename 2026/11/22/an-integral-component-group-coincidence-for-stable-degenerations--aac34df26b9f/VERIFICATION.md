---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The marked graph is the connected Levi graph of the order-four Latin square: each crosspoint is incident to one line of each class and each distinct-class pair of lines has exactly one common point. Normalizing row and column zero and enumerating gives four reduced squares, exactly the Klein-four table and three simultaneous relabelings of the cyclic table. Their intercalate counts distinguish the two types. Independently I used an oriented incidence matrix with a line vertex removed (rather than rooting at a point as in the deposit), formed the 27×27 integer Gram/Laplacian and performed Smith reduction directly over Z with SymPy. All four gave eighteen 1s and 2,8,8,24,24,24,24,96,96. Replay: `python3 /workspace/net_snf_reproduction.py` with SymPy. The uploaded script and log were read, not run. As an independent check on order, the 12×16 point-incidence block has row Gram matrix with diagonal blocks 4I₄ and off-diagonal all-ones blocks, hence eigenvalues 12, 4 with multiplicity 9, and 0 with multiplicity 2. The block Laplacian matrix-tree product is 7·8⁹·4²·3⁶ divided by 28. The abstract nodal curve is stable since all rational components have valence at least three; its arithmetic genus is 48−28+1. Choosing all smoothing parameters of the form t in an unobstructed deformation gives unit thickness; Raynaud’s degree-class identification applies to this split regular model.

## originality

PASS

There is exact existing catalogue coverage of the Klein-four case under incidence duality: the Reye record computes the same group for the very same graph. No date-order inference is made, and no standalone novelty is credited to that case. The supported distinct central finding is the equality across both isotopy types and, in particular, the exact cyclic-type group. Neither the Reye result nor the checked broader results account for the cyclic type.

## value

PASS

The two realizable combinatorial types give a natural full small family of split unit-thickness degenerations. Their equal group orders are automatic from the block structure, whereas agreement of the entire integral groups supplies a sharper failure of a Jacobian invariant to distinguish the two types. This gives precise invariant data for the cyclic type and the exact comparison with the existing Reye/V₄ result, not another numerical computation of the Reye case alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
