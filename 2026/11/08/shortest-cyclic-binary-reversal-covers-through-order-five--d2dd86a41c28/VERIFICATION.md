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

The class count (2^n+2^ceil(n/2))/2 is a reversal-involution count. Every covering cycle has a 0^n window, so fixing one root loses no solutions. Inspected verify_dp.py and verify_census.py: the former traverses all class bitmasks and n−1-bit suffixes with all n−1 closing windows; the latter directly enumerates every 0^n-rooted binary suffix for every L from n through the claimed minimum, deduplicates rotations and both symmetries, and checks both attached optimal-cycle lists. An independently written exhaustive implementation recomputed for n=1..5 the shortest lengths 2,4,8,14,26, class counts 2,3,6,10,20, optimal cycles 1,1,2,8,128, and bracelet counts 1,1,1,3,36. With all shorter candidates checked, this is an exhaustive proof only for n<=5. Equality of rooted and necklace optima also verifies one occurrence of 0^n in each optimum.

## originality

PASS

The original finite exact cyclic minimum-and-necklace census is not immediately implied by previously studied unoriented de Bruijn linear constructions or ordinary de Bruijn necklace counts. The closest full primary Burris–Motta–Shipman text studies linear unoriented words, graphs and examples; the circular root and optimal-cycle multiplicity classification are additional. Searches found no exact earlier table but cannot exclude an unindexed enumeration.

## value

PASS

Reverse-equivalent coverage is a natural universal-cycle problem. n=4 and n=5 are the first nontrivial obstructed small instances; exact optimal necklace and symmetry counts, with witnesses and all-shorter-length exclusion, provide a mathematically motivated complete finite classification rather than only a witness or unmotivated statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
