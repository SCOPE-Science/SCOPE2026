---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For an odd rung count, an independent colour class meeting consecutive rungs must meet opposite rows on those rungs. The unselected vertex across from one of these hits then has two neighbours in the class, forcing its third neighbour into the class. Repeating forces alternating selected rows around the whole cycle and violates independence on odd closure. Therefore each class occupies at most floor(n/2) rungs, and on odd n the ceiling of 2n/floor(n/2) is six at three and five at every n>=5. Even prisms are cubic bipartite, so the bipartition is a valid two-colour solution and an edge precludes one colour. On the triangular prism six distinct colours suffice. I independently generated cyclic triples for the printed blocks U^h V_5 and U^h V_7 at h=0,1,2; the union agrees with all 13 printed triples, and in each triple for each row the center, vertical neighbour and two horizontal neighbours have four different colours. Further U copies add only windows internal to the periodic block or across an already present U/U seam; the U/tail seams are unchanged. This establishes all odd n>=5 by locality, not extrapolation. The check can be replayed by zipping predecessor, center and successor in those six words cyclically and checking distinctness of those four digits. The frozen verifier and recorded output were inspected, not executed. Here n counts rungs, not vertices, and twisted ladders are outside scope.

## originality

FAIL

A distinct indexed result states the identical three-case formula on exactly the same graph and with the same strong-odd definition, and goes on to count optimal colourings. The extra odd-square existence assertion follows directly by combining that exact result with the indexed nonadjacent-rung structure of odd independent sets on this same family: three equal neighbours would occupy consecutive rungs. Thus the frozen finding is covered, even if the proof blocks themselves differ. This is coverage, not a conclusion on priority or derivation: the exact-formula comparison has a later catalog date and the odd-independence comparison has the same catalog date.

## value

PASS

The exact parity split is a natural classification on a standard cubic product family and is useful for testing bounded-width colouring methods. It has a structural explanation rather than a finite-list fit, and its square-colouring witness highlights a qualitative difference between even and odd rungs. This evaluates the mathematical question and result; no distinct scientific increment over the identical catalog formula and its consequences is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
