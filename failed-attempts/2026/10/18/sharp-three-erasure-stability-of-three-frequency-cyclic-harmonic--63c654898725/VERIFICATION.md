---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Parseval reduces the minimization to maximizing the erased Gram eigenvalue, with retained bound 1−λmax(G_E)/N for the unnormalized Gram. Centering frequencies gives the real kernel D(h)=1+2cos(2πh/N); the consecutive matrix splits into a symmetric 2×2 block and the odd eigenvector, yielding the stated positive-root expression. A nonconsecutive triple has at most one distance-one edge. For N≥8, every other absolute kernel entry is at most d2≥1, so strict Perron comparison applies after relabeling. For N=7 the nonconsecutive row bound 3+d1+1 is strictly below the consecutive Rayleigh test 3+√2 d1+d2/2, since 2(√2−1)+(3−√5)/4>1. At N=6 the single-adjacency case has kernel magnitudes (2,1,0), giving 3+√5<3+2√2; no adjacency gives at most 5. Three retained distinct nodes give rank by Vandermonde, and the consecutive masks have a unique run start. This proves the complete equality and strict positivity claims.

## originality

FAIL

Substantive equivalent coverage is verified: distinct indexed results state the same fixed three-band worst-erasure bound and all N cyclically consecutive equality masks, one with additional retained spectral information. The exact duplicates inspected carry later date labels than the frozen record. This is a finding of equivalent coverage and no established distinct remaining claim in the present assessment, not a finding that any of those records was first or that the frozen record was derived from them. The older two-row and condition-number results are not the basis for failure.

## value

PASS

As a theorem this resolves a natural adversarial reconstruction question for a low-bandwidth Parseval frame: it gives exact noise amplification control through the sharp retained lower bound and identifies all loss patterns attaining it. A positivity-only Vandermonde argument cannot give this quantitative guarantee or equality classification. This is value of the mathematical result, not credit for a separate contribution where coverage duplicates it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
