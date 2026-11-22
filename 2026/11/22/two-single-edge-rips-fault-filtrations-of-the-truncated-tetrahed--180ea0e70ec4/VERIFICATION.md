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
# Verification of the finite integral classification

Use Python 3 and the standalone `verify.py` in the same directory. There are no nonstandard imports. Run `python3 verify.py`; the required success marker is `EXACT_RIPS_FAULT_VERIFICATION_OK`.

The script checks all twenty-four permutations of four symbols and their edge action; identifies orbit sizes twelve and six; enumerates all 4,095 possible nonempty subsets of the twelve graph vertices; recomputes distances separately after each fault; performs literal free-face collapses at each required integer radius; and establishes simple connectivity from a presentation on the actual collapsed two-dimensional complexes. The two residual Euler characteristics are four and three.

It then builds signed integral chain boundaries and uses determinant-one elementary row/column operations. In the fault complexes, the radius-two boundary ranks are \((29,10)\) and \((26,10)\) in degrees two and three. In the intact radius-two complex they are \((31,12)\). Appending embedded fault two-cycles to intact three-boundaries yields lattices of ranks fifteen and fourteen, both completely reducible using unit pivots. This proves that fault second homology embeds primitively; the stated cokernels are free. This is a stronger check than comparing calculations over one or several finite fields.

The exact higher-scale collapses are 1151 pairs at scale three for a triangular fault, 543 pairs at scale three for a reversal fault, and 1535 pairs at scale four for a reversal fault. After the respective graph diameters the Rips complexes are full simplices. The procedure does not claim to classify multi-edge faults, all homotopy maps, or any unindexed literature. No independent external audit has been performed.
