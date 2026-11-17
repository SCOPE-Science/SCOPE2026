---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For n>=3 with precisely three ones, equal all-eight length-three scattered subsequence multiplicities force equal zeros N, P011=3x+y and P110=z+3t; the integer kernel is (1,-3,3,-1). The critical quadratic identity for P001 is Δ=s(z-y+3s). Thus only s=0 or a unique nonzero involutive partner is possible. P100 changes by the same quadratic; remaining patterns are fixed by N and triple totals. Orient y>z with d=(y-z)/3 and nonnegative x,z,v, yielding the unique two-word pair (x,z+3d,z,v+d)/(x+d,z,z+3d,v); the multivariate geometric-series count gives u^7/((1-u)^2(1-u^2)(1-u^4)). Therefore the full class GF is u^3/(1-u)^4 minus that term. All boundary cases n<3 vanish. Finite packaged DP inspected; this conclusion follows from algebra, not the finite log.

## originality

FAIL

Earlier fully inspected October 25 (also October 26 and November 2) published Resultary theorem proves precisely the identical three-gap-kernel involution, at-most-two fiber classification, and complete all-n rational generating function. The submitted claim is mathematically equivalent in the same fixed-weight, scattered multiplicity-deck normalization. Conjecture 1 was already posed in 2021, and now also solved before the submission.

## value

FAIL

The submitted theorem is correct and the underlying conjecture mathematically important, but every claimed final conclusion—exact two-element gap-class characterization, all-n counting function and finite onset—is already established in prior publications. Reproving the same formula with the same linear/quadratic mechanism is not an independently useful new mathematical fact. No surviving original valuable claim justifies a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
