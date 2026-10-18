---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For allowed harmonics 1,2,4, the two nonnegative values at t=1/2 and t=1/3 give T(1/2)+2T(1/3)=3-2lambda>=0, so lambda<=3/2. At lambda=3/2, b=7/12,c=-1/12 gives exact factor (2-x)(x+1)(2x+1)^2/6, nonnegative on [-1,1]. Contact at x=-1 and double interior zero x=-1/2 uniquely determines b,c; Fourier/positive-definite normalization is lambda=2psi(1). Independent Sympy exact rational expansion and general-family m=2 numerical specialization checked. Thus local algebraic theorem is true.

## originality

FAIL

DECISIVE PRIOR COVERAGE: published Resultary 2026-10-11 all-m doubled-harmonic theorem proves for every m>=2 the sharp unique M({m,2m})=3/[1+2cos(2pi/(3m))]. Setting m=2 gives exactly M({2,4})=3/2 and coefficients b=7/12,c=-1/12 with uniqueness. The complete published RESULT.md explicitly singles out m=2 as previously known. Current isolated case is a direct corollary of a stronger published formula and not original as of audit.

## value

FAIL

The natural sparse value is mathematically meaningful as part of the general problem, but the standalone exact invariant and unique extremizer are now explicitly known as m=2 of an established published all-m family. Recomputing the already supplied exact constant and extremizer without an additional substantive new question or method does not fill a remaining worthwhile research gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
