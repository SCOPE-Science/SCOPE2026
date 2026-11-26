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

The earlier-start, overlap-permitted longest-factor convention and no sentinel are essential. Each of the first two runs needs a literal and one additional phrase precisely when its length exceeds one; an overlapping source within that run cannot cross its terminal change of symbol at the same time as the target. In the third run the first zero phrase is limited by a if c>a. At its next phrase a same-run source still has strictly more zeros left than the target and cannot copy across the terminal boundary; a first-run source can cross precisely when the remaining zeros are at most a. A copied zero-to-one boundary then matches at most b ones, with one later overlapping phrase needed precisely for d>b, which proves the three stated regimes including equality. Symbol exchange yields the reversed formula. The two separated defect components attain only the stated endpoints, giving the exact extreme conditions and both minimum-length witnesses. Uniform lattice compositions converge to the uniform simplex law; the disjoint-pair ratios of independent exponentials are independent uniforms, giving the stated convolution and expectation 13/9. A separately written parser checked both orientations on all 6,561 run quadruples with parts 1–9; the first extrema also checked against the formulas through total length 24.

## originality

PASS

Best of inspected evidence, the exact four-run phrase formula and its induced extremal and limiting classification are distinct. Existing overlapping-LZ reversal results concern arbitrary-string worst cases; neighboring exact four-run entries measure different invariants. The exact catalogue hit is the frozen record itself.

## value

PASS

Four alternating runs are the first structure in which both letters have a return run, so both parsing directions can encounter competing old boundary matches and overlapping copies. The formula identifies exactly which length ratios trigger new phrases, gives the first and all sharp witnesses for this regime, and supplies a quantitative average-case benchmark distinct from a global worst-case bound. No claim about compressed bit length or arbitrary input distributions is needed for that use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
