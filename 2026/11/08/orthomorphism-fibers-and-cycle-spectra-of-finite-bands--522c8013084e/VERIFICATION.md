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

# Direct enumeration verification

Run `python3 verify.py` with Python 3 and the standard library. The checker constructs complete multiplication tables for seven finite bands, checks associativity and idempotence, enumerates every permutation \(\alpha\), computes \(\theta_\alpha(x)=x\alpha(x)\), and tests exactly which permutations are complete. It then constructs the theoretically predicted image (the direct product of symmetric groups on Green \(\mathcal R\)-classes), verifies that every element of the image has the same predicted fiber cardinality, and independently compares the full cycle-type distribution.

The tests encompass rectangular bands of sizes \(2\times2\) and \(3\times2\), two multi-level bands with nontrivial cross-class multiplication, two one-sided-zero bands, and the free left regular band on two generators. All 41,952 input permutations are enumerated. The actual output is stored in `verification_output.txt`; all comparisons pass.

This is an exhaustive check of the **listed finite examples only**. The theorem for arbitrary finite bands follows from the ideal-preservation and rectangular-permutation argument in `RESULT.md`. No external theorem prover or independent human audit was used.
