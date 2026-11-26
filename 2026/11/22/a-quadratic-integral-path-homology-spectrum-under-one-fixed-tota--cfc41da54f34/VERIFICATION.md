---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Successor arcs give exactly the labeled total reachability order because every chord also increases labels. The endpoint sets defining the left and right bases are the upper and lower principal sets, respectively; the common preorder nerve is the simplex on a finite chain. For a two-step path, two successor arcs give a gap of two, whereas successor–chord and chord–successor give gaps of at least four with odd–odd and even–even endpoints respectively. The endpoints determine the middle vertex in each case; two chords cannot be consecutive because the chord source and target sets are disjoint. None of these three endpoint pairs is an arc. Projecting the formal boundary onto the missing arcs sends each two-path to its own distinct negative basis vector, so Ω₂ is zero over Z, with no hidden cancellation. Deleting vertices from an increasing path keeps them distinct, so regularization does not change the calculation. Chord coefficients give integer coordinates for all one-cycles: subtract the corresponding multiples of the displayed closed chord-minus-chain chains and the remainder is a cycle on a tree, necessarily zero. This proves freeness and every rank from 0 to m², including m=1 and the full and empty subsets. The ambient cycle-rank bound gives O(n²); the exhibited n²/16 lower bound for n divisible by four is an order statement, not a sharp leading constant.

## originality

PASS

Qualitative separation from reachability and the criterion for degree-two chains are known. Even arbitrary ranks on a fixed finite total order are available from the nearby barcode construction when the number of vertices grows linearly with the desired rank. The distinctive result here is the explicit family interpolating every first integral rank through order n² on the same n=4m labeled total order, with free integral generators and transparent proof. No compared claim covers that size bound.

## value

PASS

For one labeled rigid T₀ total order, varying only which additional arcs exist produces the full first integral rank interval of the same order as the ambient quadratic upper bound. That measures how much first-homology information the endpoint-set topologies and preorder nerve can lose, beyond a qualitative counterexample or an interval of linear size. Explicit free integral cycles also distinguish this from merely checking Betti numbers over a field.

The dated certificate retains the supplied scientific assessment, sources and limitations.
