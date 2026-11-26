---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The affine three-step update is a contraction with multiplier ρ³, so its periodic solution is unique. Iterating P_t backwards three steps gives the stated three weights on the predecessor, second predecessor and current crops. On reversal the two predecessor cross-sums exchange, while the constant-input and same-crop sums cancel. The remaining factor is η(1−ρ)/(1−ρ³)=η/(1+ρ+ρ²), including at ρ=0. For D=(A−B)(A−C)(B−C)>0 the alternating cross-sum equals −D g[A,B,C]. Independently, the pair secants for type II and III are K/[(K+x)(K+y)] and K²(x+y)/[(K²+x²)(K²+y²)], respectively. Subtracting the AB and BC secants and dividing by A−C gives, for type III, numerator K²(K²−AB−AC−BC) over the product of the three positive factors; type II gives −K over its product. This checks the signs, the unique positive tie and the absence of any other reversal, uniformly in the allowed ρ, b and η. At period two reversal is a phase shift, and period one is trivial. Direct orbit substitution in the example reproduces Δ₃(2)=1/325 and Δ₃(4)=−8/14875; the largest predator stock is 17/70<1, which bounds each year's modeled loss by less than the smallest crop. The supplied check.py was inspected, not executed; it iterates the recurrence with rational arithmetic and compares finite cases to the closed form. The argument concerns the periodic loss proxy, not an unconstrained physical seed budget or finite-time transients.

## originality

PASS

The supported distinct claim is the exact type-II/type-III ordering law and unique half-saturation switch for a periodically forced, lagged affine predator stock weighted by current-crop intake. Classical divided differences and earlier three-season orientation results are not claimed as new. The strongest inspected orientation theorem is for a different observable and gives a sign that cannot reverse with saturation, whereas the observed reversal here comes from the curvature of a function of the input crop. This is an evidence-bounded decision, not a priority certificate.

## value

PASS

Reversing a cycle controls for the crop totals and leaves only the ordering effect. The result identifies a sharp case where changing the intake shape can change which chronology loses fewer seeds, and proves that carryover changes the magnitude but not the preference. This separates a finite three-crop curvature effect from the pointwise inflection of a response curve and supplies a benchmark in the first period where reversal can matter. It is not a field prediction or an evolutionary-fitness result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
