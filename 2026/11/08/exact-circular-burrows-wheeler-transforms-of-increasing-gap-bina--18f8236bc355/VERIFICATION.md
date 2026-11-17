---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

All k+1 marker one-starting and sum(g_j) zero-starting rotations are distinct because g_k is a unique maximum. A zero-starting rotation with t leading zeros sorts first for larger t; within a fixed t bucket the subsequent distinct zero gaps order the eligible j indices as k−1,...,m,k, so predecessor letters are 1 exactly at t=g_j. Counting intervening bucket sizes produces the full 1,0^(d_k−1),1, product_j 0^((k−j+1)d_j)1, 0^(kd_1),1,0 expression and run count 2k+2−2[d_k=1]. Explicit one-starting tail and k=2 empty product were checked. Independently sorted every full cyclic rotation for 1089 increment vectors d_i∈{1,2,3}, 2<=k<=6; full output strings matched.

## originality

PASS

Giuliani et al 2024/2025 primary paper studies polynomial zero-gap families and sensitivity/run-count phenomena; its section 4 rotation-comparison insight is acknowledged, but inspected theorem does not state the entire transform for arbitrary strictly increasing integer gaps or the d_k=1 boundary. Published Resultary BWT transforms for particular morphic words or fixed three/four ones are not general dominating claims.

## value

PASS

Exact run-length-encoded BWT for a full variable-gap family is a natural combinatorial compression invariant; gives O(k) compressed construction without sorting an O(sum g) word and a sharp single-increment phase switch.

The dated certificate retains the supplied scientific assessment, sources and limitations.
