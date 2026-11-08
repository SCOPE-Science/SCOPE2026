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

# Verification record

The standalone `verify.py` was executed against the actual source in this package and returned `VERIFY_OK`.

The exact, infinite-family component constructs all 64 pair states, checks the 512 possible column triples, obtains 102 directed arcs, and computes the positive-return states by graph reachability. They are precisely the seven states of one loop and one six-cycle. The graph adjacency test independently builds the edges of every \(C_n\square K_2\) for \(3\le n\le7\), enumerates all \(2^{3n}\) edge subsets, and tests whether each omitted edge has exactly one selected adjacent edge. The resulting sizes and counts are \(n=3:(9,1)\), \(n=4:(12,1)\), \(n=5:(15,1)\), \(n=6:(6,6),(18,1)\), and \(n=7:(21,1)\). The six explicit periodic constructions were separately checked at \(n=6,12,18,24\).

The finite enumeration of column triples proves a fixed finite lemma once that lemma is checked, while the local-to-global bijection is an independent mathematical argument covering every integer \(n\ge3\). Small-order brute force alone does not prove the theorem, and no external or independent mathematical certification has been performed.
