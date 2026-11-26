---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Use the oriented edge difference on the cycle, which has kernel the constants and zero-sum image. If V(h)>0, couple the positive and negative gradient masses by e.g. t_pq=d_p^+ d_q^-/(V(h)/2). Each pair of boundary edges is the gradient of a contiguous arc indicator with the chosen orientation; the total coefficient is V(h)/2. Thus the sharp norm of a constant-preserving selector reduces to its largest variation on those cut indicators divided by two. Independent exact enumeration of actual selectors (8, 81, 243 per arc), rather than box vertices, gives maxima 1, 5/4, 7/5 after division by two; complements cover the remaining arcs. Along a segment every affine piece selects rows from these finite families, including when ties persist, and integration proves the pairwise upper bound. Exact ball averages recover all three claimed witnesses. The source's singleton uniqueness on the base signal is an incidental overstatement: there is a tie at vertex 0 on C4 and vertices 1 and 2 on C5. The specified selector is still active and the ratios are as stated; alternatively on those cycles both f+epsilon*h and f+2*epsilon*h lie in the strict chamber. Adding one makes the inputs positive. For the one-input comparison, above the mean any added three-ball superlevel vertex is adjacent to an original superlevel vertex, hence cannot create a cyclic superlevel component. The coarea formula bounds output variation by input variation above the mean. The omitted variation is at least 2(mean−min) ≥ V(f)/n, using V(f) ≤ 2 sum_i(f_i−min), and a point mass attains 1−1/n. Replay: python3 /workspace/checks/frozen_exact.py 4. The submitted checker was inspected but not executed. The pairwise result is for nonnegative data, ordinary finite counting balls, and unweighted cyclic edge variation.

## originality

FAIL

A distinct Resultary record, 26e43398e583, explicitly states the same exact pairwise centered graph-ball gains on nonnegative C3,C4,C5 and also gives the C6 gain. The three-cycle-size result is exactly the restriction of that published statement. This is verified statement-level coverage, not a date-based assertion of priority, attribution, or copying. No separate original theorem remains in the submitted Finding.

## value

FAIL

The diameter-two cutoff and contrast with one-input contraction are mathematically motivated. However, the submitted contribution is a narrow exact invariant already explicitly included through the larger natural cutoff n=6. Neither the redundant classification nor an independent verification of it, as supplied here, identifies an unknown exact fact or establishes a distinct new method theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
