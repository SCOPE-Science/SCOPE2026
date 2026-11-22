---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

PASS: Reconstructed the deck quotient L/(i,a)~(i+n,1-a), with strip shortest-path distance |i-j|+row indicator; for r>=2 each finite full strip Rips complex collapses by successive left-column domination. Since n>2r, each downstairs Rips edge has a unique lift; since 3r<=n, a winding triangle would require three horizontal length-r edges at n=3r preserving row, contrary to the deck flip. All cliques lift, yielding a regular Z-cover by a contractible complex and hence K(Z,1)~S1. Stable r-to-s inclusions induce identity on the same deck group. At r=1 Euler count 3n-2n+1=n+1 and a rung-closed half-rim loop maps to a primitive generator, kernel rank n. Verified compatible triangle lifts for (n,r)=(6,2),(7,2),(9,3),(10,3),(12,4); finite checks do not establish the general argument.

## originality

PASS

PASS best-of-knowledge for the complete unbounded r>=2 and n>=3r stable interval classification; scale-two S1 and scale-one kernel are already proven in stronger published Oct25 and Nov1 records and are explicitly credited. The new portion is all r>=3 with sharp equality n=3r and stable persistence maps; neither previous scale-two proof nor untwisted prism threshold implies it.

## value

PASS

PASS: An all-r family of graph-metric Rips complexes has a sharp twist-dependent stability boundary, including the critical equality where an untwisted ladder exhibits a higher-dimensional sphere wedge; the persistent first-homology generator is identified. This resolves a motivated geometric covering phenomenon beyond a single finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
