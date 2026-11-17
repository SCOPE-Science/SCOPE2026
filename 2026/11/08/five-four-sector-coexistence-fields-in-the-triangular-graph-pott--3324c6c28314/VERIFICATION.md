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

The T(6)=L(K6) model has 15 labelled sites and 60 interaction bonds. The exact equal-color energy is F=sum_{v,c} binom(d_c(v),2), with each color-class degree sum 2t; discrete convexity gives a computable lower bound B(t) in every occupancy sector. Sixteen concrete color words from the pinned sector_witnesses.tsv attain the minimum L(s)=B(s)+min_t[B(t)+B(15−s−t)], proving e_s for all sixteen occupancies and the iff balanced-degree criterion. The lower convex hull has vertices (0,24),(3,12),(6,12),(9,18),(12,36),(15,60), yielding exactly five coexistence fields −4,0,2,6,8 with four consecutive tied sectors at each. Independently compiled C++17 fully enumerated all 3^15=14,348,907 assignments and reproduced all sixteen exact degeneracies and sector energies, including g_3=300,g_5=19530,g_15=1; this is exhaustive finite mathematics, not sampling.

## originality

PASS

Best-of-knowledge complete 16-sector minimal positive-frustration table and its five-field coexistence classification are not supplied by the checked general Potts external-field literature or the complementary Kneser graph field census. Their spectra are mathematically different: minimizing L(K6) monochromatic intersecting edge pairs requires maximizing complementary KG(6,2) penalties at fixed color sizes, whereas the earlier KG result determines minima. The result is not a new general partition-function formalism and does not assert novelty of each isolated small integer.

## value

PASS

T(6) is a canonical 15-vertex strongly regular graph and the line graph of K6. Three colors are fewer than the underlying graph edge-chromatic requirement, giving naturally unavoidable frustration and a nontrivial finite magnetic-field occupancy response. The sixteen exact sector minima, all degeneracies, and five four-sector coexistence fields constitute a complete, independently useful classification for this fixed model, supported by a constructive degree-convexity principle. A finite exact invariant can be mathematically valuable without a thermodynamic extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
