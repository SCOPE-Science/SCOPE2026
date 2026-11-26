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

PASS

The normalization in Ma's order-three defect was checked against Theorem 2.3 and independently by exact polynomial interpolation. With H(t)=(t+1)(t+2)(t+3), D(t)=H(t+3), R=diag(1−H/D), one has M* = BM and S=M*(I−B*B)M. The finite-support right inverse is (I−T)^3 diag(H)/6 for the unilateral shift T; multiplication on basis vectors follows by cancelling the generating series (1−z)^−3 and (1−z)^3, giving dense range. On −1<α<0 the signed weights have signs (−,+,−). Since D−H=9t²+63t+114≥60 for t≥−1, the v₂ weighted square sum is at most (1/60)Σ_{n≥0}[(n+3)(n+4)(n+5)]^−1=1/1440. Multiplication by |λ₂|≤20 and weighted Cauchy–Schwarz absorb that direction into R/72. The form is nonnegative on v₀⊥, so its pullback has negative index at most one (the preimage of v₀⊥ has codimension at most one). For 1 on 0..N and zero elsewhere, the diagonal is 9 log N+O(1), the v₀ pairing is log N+O(1), and the other pairings stay bounded; the quadratic form is 9α(log N)²+O(log N) and eventually negative for each fixed α<0. Density transfers a strict witness to S. R tends to zero and the correction has finite rank, giving compactness and exactly one negative eigenvalue with multiplicity one. Ma Theorem 1.1 supplies nonnegativity for α≥0, including zero. No finite spectral truncation was used.

## originality

FAIL

Direct equivalent coverage in a distinct published catalogue record: Resultary 88dd990f36ce states and proves the identical exact index-one theorem on the same operator and the entire same negative-shift interval, including compactness. It uses the same Ma defect and the same absorption mechanism. The remaining nonnegative-shift statement is already Ma's Theorem 1.1. This is a finding of coverage, not a determination of which result was first proved or communicated; the exact-match record's later catalogue label does not prove antecedence.

## value

FAIL

Negative inertia is intrinsically well motivated: order three is the first order where two signed defect terms threaten to produce a two-dimensional obstruction. However the submitted exact invariant is already present in a distinct catalogue result, and no remaining substantive increment is isolated. The tighter sufficient absorption estimate is neither claimed sharp nor shown to give a new spectral conclusion; the nonnegative range is also known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
