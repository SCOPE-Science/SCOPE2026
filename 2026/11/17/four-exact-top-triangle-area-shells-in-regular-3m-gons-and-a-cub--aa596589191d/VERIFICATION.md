---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

With circumradius one and positive cyclic gaps summing to N, the chord formula gives area 2 times the product of their half-angle sines. Its logarithm is strictly Schur-concave. In a sorted triple with sum 3m, minimum at least m forces balance; minimum m-1 leaves exactly two possibilities; minimum at most m-2 forces maximum at least m+1 and hence majorization of (m-2,m+1,m+1). Strictness rules out every other shape even as a tie once the incomparable pair is ordered. As a separate gap calculation, the oriented shoelace formula gives half the sum of the three gap central-angle sines. Put x=2π/N, φ=2π/3 and g(t)=sin(φ+t). The three gaps are respectively sin φ(1-cos x), sin φ sin²x+cos φ sin x(1-cos x), and -2 cos φ sin x(1-cos x). These reduce to the three stated formulas and are positive throughout m≥3. Their expansions give the asserted quadratic/quadratic/cubic separation. Counting N starts per distinct gap ordering and dividing by three yields N/3, 2N, N, N, valid also at N=9. The accompanying Cartesian floating-point checker is supplementary, was inspected rather than executed, and is not needed for all-m ordering. Summing binom(3m,3) for 3≤m≤28 confirms the stated size of its test range.

## originality

PASS

Rank 1 and its count and the sine-product parametrization are not new. The supported distinct claim is the complete ordering of the next three vertex-triangle levels with equality cases and the exact positive cubic splitting. Checked sources do not supply it or imply it without the dominance and incomparable-pair arguments; priority remains provisional, specifically against the unread linked Huber text.

## value

PASS

For a regular polygon the leading discrete departures from the equilateral maximizer are natural measures of optimization stability. The fourth level is motivated by the two opposite nearly balanced gap shapes with the same quadratic deficit. The exact result distinguishes them at cubic scale, proves no other gap shape intrudes, and gives multiplicities rather than just four values. This is a useful exact boundary across an infinite natural family, beyond the routine maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
