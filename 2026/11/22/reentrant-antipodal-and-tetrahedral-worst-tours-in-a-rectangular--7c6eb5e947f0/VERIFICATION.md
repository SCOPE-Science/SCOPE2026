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

A two-point antipodal cycle costs 2E; a four-cycle on a parity class omits a perfect matching and minimizes cost at min(4D,2C+2D). Verified the nonnegative-cone basis analytically on both parameter regimes. The inequalities D>A+B, E>B+C, E>D+A come from strict superadditivity of the three-halves power with strictly positive arguments. C>2A and all five coordinate generators are strict. In the low regime, 2(E-D)>C since the difference is increasing from C-1>C/2. In the high regime E-B>A+C since it increases from 3sqrt(3)-1>A+C. The only vanishing possibilities in the stated regimes are the two order comparisons at t=1. Independently parsed the frozen certificate with /workspace/review-evidence/prism.py, reconstructing the edge classes from actual bit-coordinate triples and the orbit action by coordinate reflections and swapping the horizontal coordinates. Checked coverage of all 247 subsets in 32 disjoint orbits, feasibility of each cyclic order, and all 64 vector identities in exact rational arithmetic. In particular, checked independently of the frozen code that every one of the 60 noncandidate-phase rows weights a uniformly strict generator, which excludes spurious co-maximizers even at t=1 or a crossing. The decreasing ratio E/D below 1 and increasing unbounded difference E-D above 1 give the two crossings, with the candidate order reversing at both. A decimal cross-check gives 0.8381016548840094 and 1.4357662186405674; the crossings use exact equations, not sampling. The unchanged source checker was inspected, not executed.

## originality

PASS

Best-of-knowledge pass restricted to the exact anisotropic profile and its equality classification for cubic cost. The parity-tetrahedron lower example is known, and the exact unit-cube specialization is separately covered.

## value

PASS

This is a natural deformation of a known sharp vertex extremum. It gives the entire exact corner invariant, including two sharp transitions and a return to the original extremizer geometry. It answers when the known cube witness stops being extremal, with no exceptional unclassified parameter values. That is more informative than merely computing the same finite optimizer at a few chosen aspect ratios.

The dated certificate retains the supplied scientific assessment, sources and limitations.
