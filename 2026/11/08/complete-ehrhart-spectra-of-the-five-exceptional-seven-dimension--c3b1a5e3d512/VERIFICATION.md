---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Using the 14-by-7 binary vertex matrices transcribed from the published five-column table, exact integer cofactor tests over all 3432 seven-vertex subsets per polytope identify 144,136,136,136,136 supporting facets. Complete containment tests over grid {0,...,q}^7 for each q=0..7 yield the submitted L_i(q), and finite differences of degree-seven Ehrhart theory give every h* coefficient for all dilations q>=0. Independently rebuilt exact integer enumeration for all five polytopes and confirmed h* rows [1,6,31,132,201,92,1,0], [1,6,31,112,171,64,1,0] (twice), [1,6,29,134,197,82,1,0], [1,6,33,148,231,94,1,0] and volumes 464,386,386,450,514. The complete finite certificate is mathematically exhaustive, not a mere sample.

## originality

PASS

PASS best-of-knowledge: Kaibel and Pokutta classify the five non-centrally-symmetric simplicial binary polytope orbits and ordinary f/h vectors, but the accessible primary abstract and related text do not substantiate prior computation of their Ehrhart h* series, normalized volumes and dilation-two/three distinguishing data. Ordinary face h does not imply Ehrhart h*; indeed four objects share face vectors but three different h* series. Full primary source could not be read in this run (OA attempts failed, Oxford returned VPN-disconnected), so an exact prior table in the uninspected appendix remains an explicit serious residual risk, not evidence of noncoverage.

## value

PASS

The five explicit first-dimensional exceptions to a natural cross-polytope symmetry conjecture form a strongly motivated canonical finite census. Exact Ehrhart series and lattice volumes distinguish affine/lattice behavior not captured by ordinary face vectors, giving an independently useful natural numerical invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
