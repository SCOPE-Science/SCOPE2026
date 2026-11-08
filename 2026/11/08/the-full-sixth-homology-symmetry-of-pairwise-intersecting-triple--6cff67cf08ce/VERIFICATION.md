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

## Reproducible verification

The accompanying `verify.py` is a self-contained Python 3 integer-arithmetic checker. Execute `python3 verify.py`; the recorded run is in `verification_output.txt`. It reconstructs all seven-label triples, every orbit under each of the fifteen cycle types, valid orbit selection, cross-orbit incompatibility, and the exact independence-polynomial recursion at \(-1\). The algorithm does not use a precomputed character table.

It also independently reconstructs the entire rational character table from Young permutation modules and weighted inner products, checks the exact Specht multiplicities, the identity dimensions \(29\) and \(7\), the character parity formula, and the sum \(5040\) of conjugacy-class sizes. Its only external mathematical premise is the published rational Betti concentration and ranks; the ninth-degree character follows independently by virtual-character saturation and is compared with the existing exterior-power calculation afterward.

The identity case was separately checked by cardinality-counting all independent triple families; its size-distribution vector sums to \(1,278,686\) and has alternating sum \(-22\). No large-matrix integral rank computation, torsion calculation, or homotopy-type assertion is made.
