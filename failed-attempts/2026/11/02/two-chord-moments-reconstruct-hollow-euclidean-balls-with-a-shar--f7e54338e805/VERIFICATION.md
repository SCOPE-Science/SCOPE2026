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

For spherically symmetric independent volume samples, isotropy gives E[(X·Y)^2]=u²/d with u=E‖X‖², so μ₂=2u and μ₄=2v+(2+4/d)u² with v=E‖X‖⁴. The radial power density gives the asserted F_d and scale. For an independent monotonicity check put s=−log q and k=(d+2)/2. The hyperbolic factor in F_d is 1−[sinh(s)/sinh(ks)]²; the ratio strictly decreases in s because x coth x strictly increases for x>0. This yields the two open endpoints and strict inversion. Both endpoints decrease with d; subtracting the lower endpoint in d from the upper one in d+1 gives (d−5)/[d(d+1)(d+5)], including the nonattainable equality at d=5. Fixing any positive μ₂ by scale makes a ratio in an overlap a genuine moment collision, not a claim that all d≥6 shells are ambiguous. At q=0 expansion starts at q^d with the displayed coefficient. At q=1, expanding the hyperbolic ratio at s=0 gives F_d−(1+1/d)=s²/6+O(s⁴), hence (1−q)²/6+O((1−q)³). The rational function extends analytically at both endpoints, so differentiation gives −F'_d(q) comparable to q^(d−1)(1−q). Integrating on the halves of [0,1] bounds the decrease below by a constant times interval length to the power d (on the right half the lower bound is quadratic). The endpoint orders prove sharpness for the radius ratio. A bounded independent Fraction check corroborated the radial identities and overlaps; the bundled script was inspected, not executed.

## originality

FAIL

Material equivalent indexed coverage: the distinct same-day record bc270d434482 gives the identical forward statistic, strict monotonicity, exact realizability range (explicitly including its positive-hole restriction), recovery formula, and both sharp endpoint expansions and inverse exponents. Its statement even extends fixed-dimension recovery to a full ball, and its proof includes the global q-Hölder estimate. The frozen unknown-dimension paragraph is not stated there verbatim, but follows by comparing two endpoints of its already exact realizability intervals at unrestricted positive scale: U_(d+1)−L_d=(d−5)/[d(d+1)(d+5)]. Their monotone order makes this sign test sufficient for low-dimensional identifiability as well. There is no additional inverse analysis in that remainder beyond the interval corollary. This is a finding about equivalent coverage and implication, not a finding of chronological priority between same-day records.

## value

PASS

Two population moments are a natural restricted-data inverse problem for a two-radius shape; an exact attainable range and endpoint conditioning identify what this measurement can recover, and comparing dimensions exposes a real identifiability limit. This is useful as a classification, independent of the finding that it repeats or directly follows from indexed mathematics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
