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

FAIL

The conditional ratio and cancellation are correct, but the frozen Finding, line 6, calls both sequences positive under all allowed h. In fact h(0)=1 and h(d)=0 for d≥1 makes every outcome have unit weight, so A_2=1−1=0. Only T_m needs and has strict positivity. For the formula, the nearest earlier larger label marks the last vacant space before the target at the car's arrival. Induction over car labels shows that a fiber consists exactly of independent preferences from each ensuing contiguous interval, giving the weighted product of prefix sums. At the maximum label k the interval has length k and that label blocks any right-hand interval from reaching the left block. Thus the standardized left and right weights are unchanged and summing over actual left label sets leaves a common factor F(k). A left set {s_1,…,s_a} contributes precisely Σ(s_i−i) cross inversions, in addition to n−k from the maximum. The sign-weighted subset coefficient is (−1)^(a(a−1)/2)[z^a]∏_(j=0)^(n−2)(1+(−1)^j z); adjacent factors pair as 1−z², yielding G in both parities and also in the empty case n=1. T_a T_b>0 gives a well-defined ratio for every k. Summing over k gives the two recurrences. In the unit-interval specialization, pairing neighboring maximum positions in the even signed recurrence gives E′=O; the odd signed recurrence gives O=2E²−E, also the unsigned exponential-series equation. CHECK.py and VERIFICATION.md were inspected, not run; their finite tests do not test strict positivity of A_m or prove the all-kernel assertion.

## originality

FAIL

The conditional signed-shuffle argument at a fixed last-car position, including the factor G(n−1,k−1), already appears in earlier indexed results. Their bias theorems are uniform and unconditional, but the matching fixed-position argument in the proofs matters. Its labeled-subset sum only uses that the factorized fiber weight is constant under changing the left label set at fixed standardized subpermutations. The displacement-weighted case has precisely that property by substituting a prefix sum of h for the length of the same allowed displacement interval. Thus the extension is a direct reweighting of the existing fixed-position argument, not a distinct new sign decomposition. This is not a claim that an inspected earlier theorem literally states the arbitrary-kernel ratio.

## value

FAIL

Conditional parity under displacement weighting is a natural statistic, but the frozen contribution does not go beyond the known fixed-vacancy signed shuffle with the same factorization and substituted local weights. The cancellation and ratios transfer without a different structure or a new evaluation of the remaining signed sums. The recurrences and already-known ordered-Bell specialization do not leave a substantive additional finding to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
