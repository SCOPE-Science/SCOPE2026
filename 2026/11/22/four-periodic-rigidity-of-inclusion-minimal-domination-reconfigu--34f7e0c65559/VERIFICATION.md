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

The two accompanying Python 3 programs depend only on the standard library. Execute `python verify_exhaustive.py` and `python verify_structure.py` in the same directory as this file.

`verify_exhaustive.py` independently constructs the labelled cycle, lists every inclusion-minimal dominating set by direct deletion tests for lengths \(3\) through \(18\), enumerates all expansion/contraction moves, and asserts that only the four rotations of the periodic \(1100\) pattern are isolated, at positive multiples of four beginning with eight. Counts of vertices, edges and isolated configurations are printed for every tested length.

`verify_structure.py` independently builds an 11-bit neighborhood verifier and the associated finite de Bruijn automaton on 10-bit states. A self-contained Tarjan strongly connected component procedure proves that the only cyclic recurrent component is the four-state directed cycle with states 204, 409, 614 and 819. It covers all frozen words of arbitrary length at least eleven. This is a genuine finite-state proof, separate from bounded-length enumeration; it supplements but does not replace the elementary all-length proof in RESULT.md.

Both were executed successfully from the final source paths during preparation. Finite execution does not independently validate the modeling assumptions or prove the literature novelty claim. No independent external validation has occurred.
