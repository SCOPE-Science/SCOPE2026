---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Gauss–Bonnet and the exact complete-intersection total-Chern-class identity give χ=D[t^n](1+t)^{n+c+1}/∏(1+d_i t). If 4|D then χ=0 mod4. With exactly one even degree 2 mod4, reduce C mod2 to binom(n+2,2), odd exactly n mod4=0,1. If all degrees odd, write f for degrees 3 mod4: C≡[t^n](1+t)^{n+1}((1+t)/(1-t))^f≡n+1+2fn (mod4), then D≡(-1)^f. The asserted parity and valuation-one subclasses follow. Independently recomputed the integer Chern-series coefficient and checked all 5,928 cases with n<=12, codimension<=4 and degrees 2..9; proof is symbolic for arbitrary dimensions/grades.

## originality

FAIL

Navarro Aznar (1980) Theorems 1–2 already supply the exact characteristic-class and Euler-number formulas for every smooth complex projective complete intersection of arbitrary multidegree, determining strictly more information than χ mod4. The new three-branch residue is obtained by substituting degree classes into that published exact formula and the elementary mod4 binomial expansion (1+2t/(1-t))^f≡1+2ft/(1-t). No new geometric invariant, restriction, counterexample, or nontrivial computation not implied by the stronger prior expression remains. The exact mod4 cases may not be printed verbatim, but the claimed output is an immediate algebraic corollary of the same-object exact prior formula. This is a substantive prior-implication failure, not an inference from negative search.

## value

FAIL

The result is a compact computational restatement of a fully known exact invariant. Unlike an independently motivated unknown structural cutoff, its oddness and ν₂=1 tests follow from textbook coefficient reduction of the published Euler expression in a few lines; no distinct mathematical obstruction, new topology, or independently necessary precision unavailable from prior exact data is established. Reproducible enumeration and correctness alone do not rescue scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
