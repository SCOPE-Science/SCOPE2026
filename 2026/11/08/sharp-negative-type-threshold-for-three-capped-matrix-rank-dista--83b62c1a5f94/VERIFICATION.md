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

# Verification of capped-rank metric result

Run `python verify.py` with NumPy. The independent finite calculation enumerates the binary rank-one two-step convolution coefficients, computes integer Walsh transforms of the two rank indicators \(\mathbf 1_{\{\operatorname{rank}=1\}}\) and \(\mathbf 1_{\{\operatorname{rank}=2\}}\) on all \(65{,}536\) matrix entries in \(M_{4,4}(\mathbb F_2)\), and matches every dual-rank eigenvalue to the claimed formulas. It also checks \(36\) parameter/root comparisons over \(q=2,3,4,5\). The expected final line is `CAPPED_RANK_THREE_VERIFY_PASS`.

The numerical root calculations are not proofs of the existence/uniqueness of roots for every field size; those statements follow from the proof's explicit positivity and strict-convexity arguments. No formal proof assistant or independent expert assessment has been used.
