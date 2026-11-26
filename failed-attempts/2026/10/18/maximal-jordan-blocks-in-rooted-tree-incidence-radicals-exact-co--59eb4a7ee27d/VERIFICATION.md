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

Checked RESULT.md lines 5–48, for h≥1 and the natural matrix representation. An h-step strict chain must advance exactly one depth per step and start at the root, hence is the unique saturated path to its endpoint. Therefore N^(h+1)=0, the only possibly nonzero row of N^h is the root row, and each entry there is its path product without cancellation. Taking all cover coefficients nonzero realizes the upper bound h+1, and rank(N^h) is exactly the multiplicity of that size block. Uniform coordinates give independent edge-success probability t=(q−1)/q. Independence between child branches yields the failure product and the terminal conditions at absolute depth h and at shallower leaves, with one operation contribution per edge in an arithmetic-operation (not bit-complexity) bound. The count of strict ancestor pairs is the sum of depths. For a full b-ary tree the cover count removes the freely chosen noncover entries, and for each new child branch there are q^{E_j+1} assignments of which (q−1)C_j succeed. Taking the complement of failure on all b branches gives the frozen integer recurrence, including C_0=1. The full-tree map is increasing and strictly concave for b≥2. In the supercritical case the positive fixed point has derivative in (0,1), so monotone iteration from one converges geometrically; b=1 gives t^h. At (b,q)=(2,2) the reciprocal increment tends to 1/4, so averaging gives s_h~4/h. The binary fixed point is (2t−1)/t² for q≥3. A separately written bounded matrix-power calculation (python3 /workspace/review_checks.py 5) checked exact counts including 624/1024 for the full binary height-two tree over F2, 64/512 on the unbalanced six-vertex tree over F2 and 144/256 on a smaller unbalanced tree over F4. The finite checks are not a proof of the general law or asymptotic. The frozen checker was inspected, not run.

## originality

FAIL

The distinct indexed result fcd29ef31ec1 gives the identical top-power law, whole-radical count and threshold for full b-ary trees, and its proof gives the pointwise identity on every element there. Although it does not state the arbitrary-tree recursion, that pointwise result applies to an arbitrary height-h tree embedded by retaining a rooted subtree in a full b-ary tree of the same height (b at least the maximum branching and at least two), by putting every extra incidence coordinate equal to zero. This is a direct restriction on each input, not an inference of a conditional probability from an unrestricted total. The remaining arbitrary-tree calculation is ordinary independent bond survival by child subtrees, and the integer recurrence is the same probability after clearing the cover-assignment denominator. There is no distinct nonmechanical remainder established. The comparator has a later catalogue path; this is a verdict on demonstrable coverage, not priority or provenance.

## value

PASS

The algebraic identification of largest-block occurrence in the whole natural incidence radical with a tree survival event is useful in its own right. It gives exact answers without materializing matrices, also when shallow leaves and deepest leaves differ, and yields a sharp field-dependent distinction for full binary trees. No separate value or originality is assigned to the standard branching law or an algebraic rewriting of it, and the cited comparator covers the substantive result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
