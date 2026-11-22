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

The accompanying `verify_invariant.py` independently constructs the rim-first, leaves-second update over the integers \(3\le n\le17\), checks every cyclic independent input word and every leaf-flipping state, compares the exact one-step conjugacy, checks injection, overlap and Lucas–Möbius orbit populations. Run with `python3 verify_invariant.py`.

The separate `verify_full_small.py` represents graph states as tuples and constructs the complete functional graphs for \(3\le n\le9\), \(349504\) labelled initial configurations in total. For these **finite** graph sizes, the recurrent vertices coincide exactly with the constructed union. Run with `python3 verify_full_small.py`. No evidence beyond these finite orders is inferred from this enumeration.

The mathematical proof for arbitrary \(n\) appears in `RESULT.md`: its crucial local induction explicitly treats the first and last rim vertices, which have different already-updated neighbors, and shows the leaf update is exactly left rotation of a cyclic no-adjacent-ones word. Arithmetic orbit counts follow from the Lucas transfer matrix and Möbius inversion, independently of the finite checker.

The scripts use only Python's standard library and require neither network access nor external input datasets. They are ordinary reproducibility checks, not independent mathematical validation. External independent audit remains unperformed. The all-order completeness of the constructed recurrent family, attraction basins, and transient cutoffs are not proved.
