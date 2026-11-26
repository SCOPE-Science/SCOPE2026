---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Normalize each edge column to e_i+λ_ij f_j. The determinant on a four-cycle vanishes exactly when the two diagonal gain products are equal. In any dependence, the nonzero-coefficient support cannot have a leaf. A simple bipartite graph on at most five edges with all support degrees at least two must be a 4-cycle: with five connected edges it would have at most five vertices, but a 2-by-3 bipartition with no leaves at its three-vertex side requires six edges. Hence all <=5 columns are independent under the gain condition. The six K_2,3 columns occupy five rows, so a weight-six dependence exists. A nonzero left row annihilator would make all gain rows proportional, contradicting a nonzero 2-by-2 minor. The exponent difference (i−k)(j−l) is nonzero modulo the prime p; F_8^× has order seven and z mod z³+z+1 is neither zero nor one (the cubic has no F_2 root). For any K_6,6 filling, six distinct ratios force q−1>=6. At q=7 normalize against one row: two permutations have product-of-values quotient 1, which cannot be the product −1 of a permutation of F_7^×. These are universal proofs; the inspected frozen verify.py records exhaustive concrete checks but was not executed in this review.

## originality

FAIL

The exact coding wording was not found in a prior paper, but both sides of the claimed sharp alphabet result and the prime-order family are mechanically covered after column normalization: the upper construction is the prime Fourier/difference array, and saturated width over F_7 would give a complete mapping of the even cyclic group C_6. The old complete-mapping obstruction is exactly the frozen product argument. The code dimension and distance follow by the mask's standard cycle and leaf tests. This is demonstrated implication coverage, not a finding based on an inaccessible source.

## value

FAIL

The full-support restriction and exact alphabet for the named benchmark are naturally motivated, and the proof is reusable as an exposition. But the specific cutoff and infinite family here reduce to the existing prime difference-array design and the saturated complete-mapping obstruction. No distinct unresolved coding invariant remains; the weak-mask question would be different and is not proved in the frozen record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
