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

# Reproducibility and limits

Run `python3 verify_betweenness.py` from the unpacked folder. This code uses only Python 3's standard library. It constructs every labelled tree via Prüfer words for orders three through seven and tests each marked cardinality of at least three using an initial marked block; relabelling ensures that no essentially different marked set is skipped at the same order. It obtains 89,629 tree/cardinality cases. For each case it constructs all marked-pair paths, calculates every signature independently, computes the compressed marked-hull formula, and asserts exact agreement and the claimed upper bound.

The code separately generates all unrooted binary labelled leaf trees on three through seven leaves by all edge insertions, realizes each maximal signature family in a minimum-order host, checks the \(3m-4\) distinct-trace count, and verifies respectively \(1,3,15,105,945\) nonidentical families. Expected final status: `ALL_CHECKS_OK`.

These finite computations cannot establish the general theorem. The universal claims are proved in `RESULT.md` by the complete-multipartite marked-component characterization, the essential-tree degree sum, explicit equality constructions and tree-split reconstruction. The proof does not rely on an external certificate or a timeout-based impossibility inference. No external validation has been performed.
