---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The closed form R_n^(s)=2^(n-2-2c_s(n))*3^c_s(n) for n>=2, with c_s(n)=max(0,floor(n/s)-1_{s=2,3}), follows by induction from the actual variable-order recurrence using reset multipliers 3/2 and ordinary multipliers 2. Positivity of exponents and strict increase from index 2 are checked at the starting values. Unique 2- and 3-adic valuations force common positive terms (including 1 counted only once) to occur at identical n. For 4<=k<ell matching floor quotients yield disjoint q=0 and q>=1 intervals of lengths k-2 and k-q(ell-k), giving the precise sum, last index k^2-1 for ell=k+1 and no later matches. The k=2,3 exceptional tables are explicitly verified by their shifted floor functions. Independent arbitrary-precision recurrence generation for s=2..13 and n<=249 reproduced the theorem across all 66 pairs. Those tests corroborate, not prove, the unrestricted interval argument.

## originality

PASS

The September 11 Abdelaidoum–Mehiri–Belbachir paper establishes individual term formulas and prime valuations, but the exact two-period intersection problem, synchronized common indices, all-pair exceptional tables and quadratic last index are not asserted in the accessible abstract or indexed individual-sequence entries. A full source-text check could not be completed; therefore originality is qualified rather than claimed certain. The intersection classification is not a mere reprinting of a single sequence table.

## value

PASS

Cross-intersections of recurrence value sets are a natural arithmetic invariant; here the all-parameter exact finite classification exposes a sharp quadratic number of common terms for neighboring periods, a quadratic terminal index, and disappearance of noninitial coincidences for ell>=2k. Those are meaningful structural answers to the two-sequence Diophantine comparison, not arbitrary isolated numerics, even though the calculation uses known closed forms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
