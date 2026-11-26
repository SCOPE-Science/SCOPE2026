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

Independent exact census: construct the 11 neighbors lists for mu(C5), add the incumbent as an extra voter exactly at even-degree vertices (equivalent to tie retention), and evaluate strict odd-input majority simultaneously on all 2048 bitmasks. Seed the recurrent set by F(F(x))=x. Grow its inverse images one full breadth layer at a time, inheriting the least mask of the target orbit; since this exhausts every state by layer 7, no longer cycle can exist. The fixed/oscillating entry pairs for t=0,...,7 are (22,70),(262,130),(594,10),(290,0),(280,0),(230,0),(130,0),(30,0). The 30 last-layer masks lead only to unanimity. For example 107 -> 663 -> 363 -> 1687 -> 1003 -> 1695 -> 1023 -> 2047, then fixed. Basin counting gives the seven stated rows, including two unanimous basins of 884 (221/256 of all starting states). All twenty dihedral/complement maps commute with the full computed map and canonicalizing both phases under them gives precisely one symmetry class per basin row. This verifies the sharp identities and complete labelled/symmetry census without presupposing the clock or a period bound.

## originality

PASS

The supported contribution is the exact Grötzsch-specific entry and attraction-basin census, including its symmetry classes, not the general period restriction. The strongest distinct indexed matches share the rule on another graph or the graph under a different rule. Neither covers the census.

## value

PASS

The Grötzsch graph is the canonical pentagon Mycielski lift, a small triangle-free four-chromatic test graph. The general period constraint says nothing about the likelihood of unanimity, the exceptional attraction of nontrivial fixed points and oscillations, or the exact maximal transient. The seven-row labelled and symmetry classification gives these quantitative baselines for the standard deterministic process: unanimity dominates, and all sharp-depth trajectories reach it, despite 55 other recurrent orbits. This is useful as an exact benchmark on a motivated, structurally asymmetric graph, not a claim of a general convergence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
