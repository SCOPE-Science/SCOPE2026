---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For an exterior vertex, the complement trace is the set-theoretic complement in the code, so distinctness transfers and globality fails exactly for full original traces. For either graph, fixing a center, the other 15 vertices have distinct two-element traces on its six neighbors: each pair of the six has precisely the center and one other vertex as common neighbors. Deleting one neighbor preserves distinctness and nonemptiness of these pair traces, and the center has the full five-set trace. Thus all 16·6=96 five-subsets of neighborhoods are LD but not global, and none can be repeated because two neighborhoods intersect in only two vertices. The same trace argument gives faithfulness of neighborhood actions. A fresh exhaustive reproduction checked all subsets through size five in both graph/complement pairs; minimum 5 in each, LD counts 1584/1968 and global counts 1488/1872. Exhausting the legal exchanges gave jump edges 18432/27072, slide edges 8160/11520, and all-source distances gave connected graphs with all eccentricities 5 for jumping and 6 for sliding. The explicit edge-preserving permutation groups reach orders 192 and 1152, the upper bounds from the faithful local actions on C6 and 2K3. Orbits were reproduced as 192 six times, 96 three times and 48 once, versus 576 three times and 144 once. Common SRG parameters give A²=4I+2J in both cases and force the same adjacency spectrum; the different counts thus establish the separation.

## originality

PASS

The global location-domination definition, complement test, standard exchange rules and graph automorphism groups are background. The supported distinct claim is the exact pairwise comparison of global optimum multiplicities and exchange geometry. The closest distinct Resultary census uses identifying codes rather than global LD; the closest regular-graph literature concerns scalar parameters, with the same-family grid statements out of the audited order range. Priority is provisional given a genuinely relevant inaccessible optimal-ensemble paper.

## value

PASS

Shrikhande and the rook graph are a canonical pair with the same strongly regular parameters and spectrum. Their exact different global-optimum multiplicities and exchange edge counts therefore give a meaningful obstruction to parameter- or spectrum-based recovery. The orbit and diameter data give a reproducible comparison of how those distinct optimal spaces can be navigated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
