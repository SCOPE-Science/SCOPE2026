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

Two-draw enumeration gives (1+s₂)s₃−2s₂². Padding to four coordinates, Cauchy–Schwarz on the other three bounds each coordinate by the larger root a of 4x²−2x+1−3s₂=0. With b=(1−a)/3, summing (x−b)²(x−a)≤0 and matching the first two power sums shows s₃≤a³+3b³. The resulting covariance bound is 2(a−1)³(16a²−2a+1)/27, which is strict for all non-point-mass laws. The five-letter witness gives 1/1600. Uniform laws give the negative values; continuity first extends positivity to each larger effective support and then produces an interior zero on the line to the uniform law. Independent exact enumeration of the witness and a uniform law and symbolic replay of the factor are in python /workspace/review_evidence/reproduce_1234.py 3. This is fixed-law covariance at sample size two, not a risk or pointwise guarantee.

## originality

FAIL

A distinct indexed result already gives the identical covariance, sharp support boundary, strict signs at every support size and exact positive witness under an affine change of the observed statistic. The zero case above the threshold is an immediate consequence by continuity. This is a concrete equivalence, not an inference from matching titles or dates.

## value

FAIL

The threshold is intrinsically a meaningful statistical fact, but as a research contribution this frozen record re-expresses a known exact cutoff, uses the same witness and obtains the missing equality case by immediate continuity. The more elementary proof does not leave a separately stated, motivated and independently valuable new invariant or theorem in the frozen claim. No repair is represented.

The dated certificate retains the supplied scientific assessment, sources and limitations.
