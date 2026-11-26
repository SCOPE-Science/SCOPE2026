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

The ordered zero-run/one-run deletion pairs reduce by the credited collision theorem to Y=T(T+1)/2−A; deleting within the same run does not change the output, and the collision count is for contiguous 0101, not scattered subsequences. Independently reconstructed the exact joint generating function by marking factors: with x=u−1 and y=v−1, a one-domino cluster 01 has weight xz²; a cluster on k≥2 consecutive 01 dominoes has all k−1 intervening marked 0101 bridges, while each marked 01 is optional. Thus the cluster series is xz²+u²yz⁴/(1−uyz²), and the full word series is one over 1−2z minus that series. This gives the stated numerator and denominator, hence the coefficient probability including empty and one-letter words. For a derivative check write B=(1−z)², U=uz², D=B−U. At v=1 the series is 1/D and its first two v derivatives are U²/D² and 2U³B/D³. Using falling factorials, Y²=(T_(4)+8T_(3)+14T_(2)+4T)/4−(T_(2)+2T)A+A_(2)+A. The substitutions give the stated two moment series; their polynomial parts have degrees 2 and 5, respectively, explaining the cutoffs. Coefficient extraction and subtraction give the boundary values and cubic variance. For n≥2 the one-dependent 01 indicators give variance (n+1)/16. Their CLT gives the leading n/4 times the centered T fluctuation; the centered 0101 count has variance O(n), and the squared centered T contributes O_P(n), both negligible on the asserted scale.

## originality

FAIL

The exact joint enumerator is a direct substitution in the generalized Goulden–Jackson cluster enumerator: the prior implementation's example actually uses the same two motifs under the relabeling P=0 and I=1. Its separate-factor marking formulation gives the bivariate specialization by the explicit cluster sum in the correctness audit. The already published deletion identity pushes that joint law forward and fixes all moments; the reported variance is ordinary differentiation and coefficient extraction. The normal limit with its scale is the standard one-dependent CLT and first-order expansion of the credited identity. The verdict is based on prior implication, not a claim that the same variance polynomial was printed in a prior table.

## value

FAIL

Quantifying ambiguity of this prescribed deletion is a legitimate question, and the formulas could be convenient in use. But the accepted run-pair theorem already provides the substantive bridge to motif counts, whose full enumerator is a direct instance of an existing exact construction on these same motifs. The variance and normalized limit add a routine coefficient calculation and standard asymptotic transformation, with no independently useful exact fact beyond those prior implications for this scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
