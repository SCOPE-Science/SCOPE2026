---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For each of 720 permutations, the 56 Boolean queries (unlabeled subsets of sizes 2..5) produce exactly 360 distinct response masks, paired by reversal. Both sliding-window and position-span definitions match. Hereditary exact bitset splitting enumerates all supports and gives [1,56,1540,17640,54810,20160,0], facets4=25830, facets5=20160. Complete all-positive-order mod-2 elimination gives rank4=5040, rank5=15120, independent of chosen positive order, with orbit sizes 47 and 29. Separately reconstructed integer enumeration and orbit checks corroborated these exact finite outcomes, not sampling.

## originality

PASS

PASS best-of-knowledge: the directly relevant interval-poset literature studies intervals of consecutive VALUES, not querying every arbitrary unordered subset of labels for consecutiveness. No inspected primary source supplies the 56-query six-label shattering polynomial, nonpure 25,830/20,160 facet strata or 5,040 mod-2 boundary-rank obstruction. Exact normal-form enumeration is fully scoped to n=6.

## value

PASS

PASS: the natural set system of permutation consecutive blocks has a complete nonpure finite shattering complex, with all maximal supports and a surprising rank-deficient extremal family. The six-point cutoff is mathematically motivated by simultaneous all-subset block constraints; exact classification and boundary-rank counterexample are usable independently of any all-n theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
