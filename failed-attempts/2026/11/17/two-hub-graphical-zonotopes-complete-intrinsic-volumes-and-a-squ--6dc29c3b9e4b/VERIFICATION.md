---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Forest incidence subsets are independent exactly for forests; Gram determinant of each tree is its order. For K2q, at most one double-attached leaf, yielding exactly D_q(k)+C_q(k). Independently enumerated all 2^(2q) edge subsets for q=3,5,7, reproducing both weighted classes. Multinomial/binomial concentration yields A/B~sqrt(3/(2q)), and expansion yields the second term; total variation to 2+Bin(q-1,2/3) follows from a vanishing disconnected fraction and bounded binomial tilting.

## originality

FAIL

FAIL: same-object published theorem explicitly gives every intrinsic V_k for K2q and the disconnected/connected expectations A_q(t),B_q(t), including A_q(1)=3^q(q/3+O(1)) and B_q(1)=3^q(sqrt(2/3)q^(3/2)/3+O(q^(1/2))). Their ratio immediately gives sqrt(3/(2q)) and the next -3/(2q), while the published binomial TV result is identical. There is no independent original remainder.

## value

FAIL

FAIL: exact coefficients, weighted class dominance, and Gaussian rank limit are already in the stronger published same-object result; the remaining disconnection probability is a direct quotient expansion, not an independently substantial new invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
