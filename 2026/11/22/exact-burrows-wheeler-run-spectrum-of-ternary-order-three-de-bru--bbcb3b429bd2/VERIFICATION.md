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

A length-27 de Bruijn necklace has distinct triples, hence distinct rotations, ordered by their triples. For each two-letter prefix the three predecessors are a permutation of the three letters, since all triples ending in that prefix occur once. Thus the 18 within-block changes are forced; the eight inter-block changes and the wrap comparison give r and c as claimed. Independently enumerated last-column blocks with the predecessor/LF map i -> 9*L[i]+floor(i/3). It is injective already on assigned rows, and an irrevocably closed proper cycle cannot extend to a single cycle. At a leaf all 27 rows return on one cycle, and reversing the predecessor walk spells the cycle with precisely the 27 row triples; that gives one necklace and no extra quotients by reversal or alphabet relabeling. Exact output from `python3 /workspace/review-evidence/02_lf.py` (full log `02_lf.csv` in that directory) matches all 18 cells, total 373248, both marginals and the extrema including the wrap-sensitive minima. Both supplied C++ certificates were inspected as text rather than executed. This establishes only the specified sentinel-free finite case.

## originality

PASS

Credit the BWT block theorem, orbit correspondences and total count. The supported distinct claim is the exact joint run distribution and its extremal multiplicities. The closest inspected primary and indexed results neither give that distribution nor resolve its run-refined count by specialization of their statements.

## value

PASS

This is a natural first ternary case with nine independent local permutation blocks before imposing global connectivity. The joint distribution quantifies both attainment/rareness of the compression-extremal cases and the effect of the wrap comparison, which is lost in a linear-only spectrum. It is a reproducible benchmark for run-enumeration and extremal constructions, not just a recomputation of the de Bruijn total or a new general run law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
