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

For every integer b>=3 and k>=0, a level-k block has signed total D=(b-2)^k, with exact prefix extrema H=sum_{j=0}^k(b-2)^j and m=min(0,2-k) when b=3, m=0 otherwise. The parent bigrams 01 and 10 provide opposite crossing factors with signed extremes +/- (2H-D); any moving window alters ones by at most one, so all intermediate counts occur. The k=0 two letters are treated separately. The recurrence yields rho_b(b^k)=2H-D+1. Independently enumerated complete two-block window spectra in 24 bounded (b,k) settings, not as an infinite proof; canonical seven-blob Git tree reconstructed exactly.

## originality

PASS

The examined exact primary statements and indexed Resultary claims, including direct implication/subcase checks, do not cover the surviving complete theorem as scoped. Specific overlaps and uncertain inaccessible full texts are recorded; negative searches are not taken as novelty proof.

## value

PASS

Substitution powers b^k are intrinsic scales rather than arbitrary samples. The exact entire Parikh-vector interval and explicit maximizing prefix give the sharp balance defect, while the b=3 logarithmic to b>=4 power-law change is a structurally motivated parameter transition. The prior b=3 formula is credited; the all-b (in particular b>=4) exact classification is not a known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
