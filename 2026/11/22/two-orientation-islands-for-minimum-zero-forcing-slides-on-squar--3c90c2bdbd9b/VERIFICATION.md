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

# Verification

The theorem is proved for every integer \(n\ge3\), with a separate \(n=2\) exception, by the explicitly documented forest-support argument, orientation obstruction, canonical-double-star edge pivots, missing-row transfer, and cross-orientation jump. The programs are supplementary finite checks only; they do not establish an all-size theorem independently of that argument.

Run `python3 verify_bruteforce.py` and `python3 verify_trees.py` using Python 3 and only its standard library. The first enumerates board-colouring subsets and executes the ordinary colour-change rule; the second directly enumerates auxiliary bipartite tree supports and their shared-endpoint exchanges. The reproducible output in `verification_output.txt` confirms precisely 4, 72, 3456 optima at sizes 2, 3, 4; slide component profiles \((1,1,1,1)\), \((36,36)\), \((1728,1728)\); slide-edge counts 0, 162, 22272; and jump connectivity (4, 414, 52368 jump edges). The two independent methods agree on the slide components.

Previously known inputs—the scalar zero-forcing number, optimum spanning-tree characterization and counts—are not treated as new. The new infinite structural statement is conditional only on the definitions and is proved in the supplied result. No formal proof assistant, independent audit or exhaustive historical novelty certification is claimed.
