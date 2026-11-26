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

Selecting one witness for each distinct external trace of size at least two and retaining only marked–witness edges preserves outerplanarity. In each incidence component, root the block decomposition at a marked vertex. The per-block charge 3a-2b for new vertices telescopes to 3(|A|-1)-2|B|. Bridges have charges -2 or +3 depending on the parent shore, and the alternating perimeter of a nonbridge block balances both shores, giving charges s-3 or s+2. A negative bridge's new witness needs a further incident block; an A-rooted 4-cycle has two witnesses with identical within-block neighborhoods, so at least one needs another block. In each case the required child is rooted at a newly introduced B-vertex and has charge >=3. Child blocks pay for at most one negative parent and are strictly positive after pairing. Summing over components, including isolated marked vertices, shows equality forces a single component and only zero-charge A-rooted six-vertex blocks. In an outer embedding the only bipartite candidate chords are the three opposite pairs on the perimeter, and any two cross, so there is at most one. The blocks' incidence with marked vertices is a tree (replace each block by a star at its block node), so distinct blocks share at most one marked vertex and their traces of size >=2 cannot coincide. This also verifies the converse by gluing these blocks at marked cut vertices and adding pendants for singletons and an isolate. The representative graph is determined by the family, so its blocks recover the packets uniquely. For the census, independently use the labelled bipartite tree degree polynomial: after factoring one variable per node its factors are (sum x_i)^{t-1}(sum y_j)^{m-1}. Taking degree three on each of t labelled block nodes, the y_j^2 coefficient gives (2t)!/(2!)^t, and x_i=1 gives m^{t-1}. Divide by t! for unlabelled block nodes and multiply by 4^t. This gives 4, 240, 47040 at m=3,5,7; m=1 has only the empty trace and the singleton at equality.

## originality

PASS

The distinct supported claim is the exhaustive packet rigidity of odd-size equality families and its application to the labelled trace census. The sharp numerical bound and the general labelled hypertree enumeration method are not new. The primary 1984 text remains an explicitly unresolved priority risk, not a reason by itself to reject or defer the result.

## value

PASS

This determines which sharp external type patterns coexist, not just how many vertices one can distinguish or whether a sharp example exists. The independent packet choices and unique hypertree reconstruction characterize all realizable boundary families and make the exact labelled count meaningful. This is a natural equality problem for a classical sharp inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
