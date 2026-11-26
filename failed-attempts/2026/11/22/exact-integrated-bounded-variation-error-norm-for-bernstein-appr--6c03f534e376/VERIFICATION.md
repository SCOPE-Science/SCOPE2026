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

For pointwise Jordan BV the two monotone parts from the variation function have increments summing to Var(f). Their level sets are half-lines with either convention, so the layer integral controls the error including exceptional grid and endpoint values; each nonconstant indicator has variation one. The binomial tail is the specified beta CDF, and split integration gives the mean absolute deviation at a step. Convexity and reflection give the finite maximum; truncated first moments give the rational formula. Independently checked 528 grid cases through degree 32 and their reflections with exact Bernstein antiderivatives (`/workspace/reproductions/bernstein.py`). The beta CLT on every interior subsequence and uniform integrability from the rescaled second moments give sqrt(2p(1-p)/pi); the same moment bounds give zero at p=0,1. The midpoint lower bound forces all maximizing grid indices to approach the midpoint. Convexity extends this to any asymptotically norming jumps by moving to an endpoint of the containing cell with no loss. In particular the proof handles n=1 and permits incompatible-with-trace pointwise values that are charged to the Jordan variation.

## originality

FAIL

The main exact formula, leading constant, and localization have demonstrable coverage at b=0 of distinct indexed Resultary record b2f50bc0f568. Same-day dates do not establish priority. The representative classes genuinely differ, but allowing either one-sided value realizes the two limits already calculated there, without changing the supremum or localization. The rational rewrite is the integer-parameter evaluation of the other record's incomplete-beta formula. This is a coverage decision, not a deduction from inaccessible historical papers.

## value

FAIL

A sharp norm at all degrees is a meaningful target, but its informative values and localization already occur as the classical member of the Stancu result. What remains here is choosing actual grid representatives for limiting step responses and rewriting an incomplete beta expression as a rational sum; without a further substantive result this is a routine extension of that exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
