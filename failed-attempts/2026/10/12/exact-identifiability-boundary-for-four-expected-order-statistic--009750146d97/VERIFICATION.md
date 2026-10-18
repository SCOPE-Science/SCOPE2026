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

For sample size four, independent derivation of the Okolewski–Papadatos generator moment equations gives m=(3c+2b)/S, v=(9ac−4b²)/S², S=3a+4b+3c. Equality gives zero variance and unique point generator, hence unique two-point parent with p=√c/(√a+√c), x=β1−a^(3/2)/(4√c), y=β4+c^(3/2)/(4√a). Strict feasibility gives 0<v<m(1−m); for u in (v/(1−m),m), r=m−u,s=m+v/u,w=v/(u²+v) realize same mean/variance as distinct two-point generators, whose explicit three-point parent inverse yields required four order means. Independently computed an interior example a=b=c=1 and constructed three-point law with expectations (0,1,2,3) to 5.3e−16. This bounded test corroborates, while source bijection and algebra prove continuum.

## originality

FAIL

FAIL: the same primary source provides a general generator-to-parent bijection and general singular-moment uniqueness theorem together with the four-term 9ac≥4b² feasibility formula; its implication already covers every boundary and interior identification decision. The provided u-family is a standard two-moment construction and canonical inversion, not a distinct invariant.

## value

FAIL

FAIL as an independent contribution: explicit atom formulas are correctly computed but routine algebraic extraction from the published n=4 moment data and general identification criterion, without a new mathematical obstruction, additional inverse theorem, or substantively new structural classification beyond that implication. The natural question is important, but this submitted solution is already essentially settled by the cited stronger results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
