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

By Poisson addition N/K has mean s and variance s/K. Within distance d_s of a noninteger s, integer C is above the same threshold for C≥N/K and C>s; the explicit C≥1 clause excludes zero-total retention. Bounding the exceptional probability by Chebyshev gives the stated inequality without needing independence of C and N. On (j,j+1), the limiting Poisson upper tail has positive derivative γe^(−γs)(γs)^j/j!, and the change of the required count at j produces exactly the mass of Z_j=j as a downward jump. For finitely many j, choose a common small η and use strict increase to make every interior witness beat both endpoints of its bracket; the pointwise quantitative bound transfers all finitely many strict gaps. Adjacent closed brackets share an endpoint (the text's 'disjoint' is imprecise); their interiors are disjoint and every maximum lies inside. To check analyticity directly, condition on N=n: the probability is e^(−Ks) times the exponential generating series with coefficients in [0,1] and coefficient 0 at n=0, hence entire and nonconstant (positive for s>0). Isolation of level-set zeros makes the interior maxima strict; an interior minimum between consecutive strict maxima follows by compactness. The arbitrary-count claim varies K with L; it does not give unbounded peaks at a fixed cutoff. At K=1000 and γ=1/4, an independently written standard-library computation at all 15 rational points checked all 14 inequalities using a 90-digit bracket for exp(−μ), positive outward-rounded recurrences, and an upper geometric remainder for C>30. For example, at j=7 the certified lower endpoint for the witness exceeds 0.00189099, and both upper bounds at the adjacent endpoints are below 0.00116238. Read VERIFICATION.md and check.py as text; from the frozen package, the supplied replay path is `python3 check.py`. Neither check counts every peak or verifies a field-data claim.

## originality

PASS

The supported distinct result is the unbounded finite peak count across relative cutoffs for a continuous Poissonized probability at fixed below-threshold composition, together with an exact seven-peak lower bound at one specified cutoff. Fixed sample size sawteeth and qualitative depth dependence are not claims of novelty. Actual adjacent catalogue claims were compared, and the plausible power-function sources that could not be read are identified rather than ruled out.

## value

PASS

This supplies a structurally informative counterexample to the intuition that more reads should steadily reduce retention of a particular below-threshold spurious taxon. It explains how a random denominator and the advancing integer retention count produce repeated peaks even after averaging over total depth. The finite certificate makes the effect concrete at a specified small relative cutoff rather than relying entirely on extreme K. It does not address total richness, effects across taxa, or practical optimal sequencing depth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
