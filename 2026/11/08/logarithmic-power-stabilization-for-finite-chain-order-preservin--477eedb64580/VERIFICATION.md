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

## Reproduction

Run `python verify.py` with Python 3 and its standard library. All checks operate on the embedded standalone source file.

The verifier directly generates all order-preserving contractions of sizes \(1\) through \(10\), calculates each power-stabilization index by literal composition and by the independently implemented tail-prefix recurrence, and compares these exactly. For sizes \(1\) through \(8\), it also generates every map separately from conditional fixed-interval Bernoulli-tail strings and verifies bijectivity. All joint image-rank/fixed-point counts match the **established** formula of Adeshola and Umar (arXiv:1303.7428v2), which is not presented as a new result.

Observed exhaustive totals for chain sizes \(1\) through \(10\) are \(1,3,8,20,48,112,256,576,1280,2816\). For size \(5\), the counts by stabilization index \(0\) through \(4\) are \(1,14,23,8,2\). Execution of the packaged script ends with `VERIFY_OK`.

## Limitations of computation

A deterministic, seeded Monte Carlo diagnostic tests three large finite tail lengths; its ratios are merely illustrations and play no role in proving the limit. Exhaustive enumeration over finitely many chain sizes does not imply a theorem as the size tends to infinity. The general theorem is proved in `RESULT.md` by an exact Bernoulli-tail coding, uniform prefix concentration, absorption-time bounds, and a uniform conditioning argument. Independent audit has not been performed.
