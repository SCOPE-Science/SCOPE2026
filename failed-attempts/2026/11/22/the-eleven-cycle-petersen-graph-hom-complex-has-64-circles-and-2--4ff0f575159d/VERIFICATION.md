---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

An independent replay used the outer/inner presentation GP(5,2), explicitly explored the recoloring components, and counted cells by assigning each cell to its lexicographically least vertex. Square-freeness forces each coordinate enlarged beyond a singleton to have equal singleton neighbors; enlarged positions form an independent set of the source cycle. If a minimum-corner walk admits d greater colors at an eligible position, its positive-dimensional choices at that position have weight dz+binom(d,2)z². Counting independent position sets with these weights counts each cell once, separately by component. The replay reproduces the complete cell vector and the component data (size, Euler characteristic, multiplicity) = (1,1,2640), (198,0,40), (6600,0,24). Theorem 1.2 of Fujii–Kimura–Nozaki applies to the finite connected nonbipartite source and square-free nonbipartite target, so the Euler-zero components are homotopy equivalent to circles. Singletons are exactly the walks without immediate backtracking. Replay at 3,5,7,9 gives no two positive-dimensional size families, so the order threshold within odd simple cycles is correct.

## originality

FAIL

A distinct same-day Resultary record on exactly the ordinary Hom complexes into the Petersen graph proves a uniform primitive-period formula and explicitly records the same length-eleven circle, singleton and component-size counts, with stronger reduced-length labels. Together with its earlier-length rows this covers the asserted first odd-source split as well. Originality is not established for the frozen Finding. This is demonstrated scientific coverage, not a finding about chronological priority: the companion record credits accessible particular-length calculations including length eleven, but the date and mirror do not establish the relative publication order or independently resolve attribution.

## value

FAIL

The Petersen cycle-Hom family and the first size splitting are natural questions. However, the exact distinguishing invariant and its refinement are already supplied in a broader available account, so the frozen claim adds no distinct exact classification. The independent finite cell enumeration is useful as corroboration, but its global face vector is used here only to certify Euler characteristic; no independent mathematical need for that vector as an isolated result was established. A code replay or change of emphasis would not repair this finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
