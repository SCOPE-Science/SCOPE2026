---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The cut removes area √3 st/4 exactly. For each fixed positive ratio, oriented projected edge contributions give W_new−W=−sX_c−tX_b+X_e, with e=sc+tb. Integrating the positive-sine overlap gives the stated V and uncut first two moments. Differentiating their normalized quotient cancels the pure perimeter term, leaving −κ₀ℓQ/(3δ₀A) in δ; the sine rule converts it to the claimed coefficient per √(st). On [0,π/3], Q is even about π/6, zero at both ends and positive between by monotonicity of x cot x. The strict reflection comparison excludes the right half, and the negative derivative at π/6 excludes the midpoint (the reflection alone does not exclude it). The quotient F/θ² has positive left limit and negative right endpoint; its derivative has numerator H=θF′−2F. Independent symbolic series and rational interval bounds (`python3 /workspace/review_checks.py 3`) confirm the trigonometric identity and uniform H/θ³ upper bound below −0.16 via the tenth-order remainder. Thus the maximizing root is unique in the fundamental sector, and arm reflection gives exactly two reciprocal ratios. The same replay gives θ≈0.452676127273466, r≈2.28062656213330 and C≈0.033215170664714. At equal arms θ=π/3 and C=0; the word ‘positive’ does not apply to that explicitly stated exception.

## originality

PASS

The edge-correlation mechanism and qualitative distinction between parallel and nonparallel cuts are prior work of Akiyama and Kamae on exactly this statistic and triangle. The distinct claim is the optimum of the area-normalized first variation and its uniqueness up to reflection. The inspected sign theorem and nearby width-extremal records do not settle that optimization.

## value

PASS

Once an oblique cut improves projection-width uniformity, the fixed removed-area budget naturally asks which asymmetry delivers the most improvement. The exact coefficient and unique optimum answer that comparison, not just the known sign; the asymmetric ratio gives a precise small-area benchmark and the proof distinguishes local sensitivity from finite-cut optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
