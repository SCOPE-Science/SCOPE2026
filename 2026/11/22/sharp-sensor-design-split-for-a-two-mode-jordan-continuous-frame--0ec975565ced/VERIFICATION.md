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

The half-line moments yield W=|v|²M(w)/(2a), with det M=r² and trace 1+r²+|w|². Thus v≠0 is necessary and sufficient and the condition number is minimized uniquely at w=0. For a unit sensor set d=1+|w−r|²; the determinant of M−dI/2 is one quarter of 4r²−(1+r²+|w|²)²+4r²(Re w)², the stated negative square. At determinant zero the smaller eigenvalue reaches d/2 only for the nonnegative real root: the negative root at r>1 has d>2; the positive root has d<2 and gives a positive semidefinite rank-one difference. At r=1 the roots merge and the difference is zero. Sensors with v=0 have zero lower bound; compactness gives a strictly sub-ceiling maximum for r<1 and the positive real-direction derivative at w=0 for r≠1 proves the split. RESULT.md lines 31–49 suffice for exact replay; the unspecified supplemental numerical trial is unnecessary. No subcritical optimum value is established or claimed.

## originality

PASS

The distinct contribution is the exact unit-norm lower-bound ceiling, its attainment branch, and its comparison with condition-number design. The conditioning formula, optimizing direction, and existence threshold for half-line tightness are already implied by the same-day finite-horizon design statement; no separate originality credit is given to those components. This is coverage, not a claim about which record came first.

## value

PASS

The comparison settles a concrete sensor-design question for a basic nonnormal family: balancing the Gramian and protecting the weakest observable direction disagree except at one coupling. The exact ceiling and unique attaining branch for r≥1 give a usable performance certificate for the unit-norm objective; the subcritical conclusion is strict separation, not a formula for its optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
