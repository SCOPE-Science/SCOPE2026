---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

An order-preserving regressive idempotent sends i to the largest fixed point at most i, since every smaller fixed point is at most its image. Commutation with this projection is equivalent to taking each block minimum to the minimum of a target block and sending that entire source block into the same target block. The induced block map g is weakly increasing and regressive. In each run of identical target blocks, monotonicity forces all but the final source block to be constant. The final block is independent of the other runs: its restrictions are Catalan maps for a self-block and arbitrary weakly increasing fillings of the noninitial entries for a strictly earlier target block, giving the stated binomial. This proves the product sum for all n>=1, including constant and identity projections. Accounting for the previous factor at each extension of a g-prefix yields exactly D_j(b), with the terminal weight applied once. The quadratic arithmetic count is for the transfer with weights supplied; if computing weights as well, precomputing factorials through 2n gives an O(n+k^2) arithmetic implementation, without a bit-complexity assertion. Independent enumeration over all 132 order-preserving regressive degree-six maps gave 18 and 31 by direct composition, the product sum, the transfer and Theorem 3.8 of the comparator. Frozen verify.py was read, not executed; bounded replay uses all tuples f(1)<=...<=f(6) with 1<=f(i)<=i and tests both compositions with each listed projection. This checks the two numerical examples, not universal validity.

## originality

FAIL

Konieczny and Korkmaz, Centralizers in Catalan Monoids, Theorems 3.4 and 3.8 and Eq. (3.2), cover the full general count exactly. Their pairs of ordered index sets encode the distinct values and run starts of g. The separate prefix recurrence reorganizes the same run weights by the last value via the immediate equality/strict-increase split. This is equivalent coverage for the count at review, not evidence of earlier priority: the inspected version is dated 2026-11-16 UTC, later than the frozen record's dated path.

## value

FAIL

The full-centralizer cardinality is a natural invariant, but the assigned contribution now reproduces a covered exact result. A prefix sum over the preceding label under a monotonicity constraint and two evaluations of the same count do not supply a substantive distinct result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
