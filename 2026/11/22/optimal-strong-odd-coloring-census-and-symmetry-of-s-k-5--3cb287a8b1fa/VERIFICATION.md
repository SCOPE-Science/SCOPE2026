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

A subdivider has degree two and forces its two root-neighbor colors to differ. The five roots therefore use all five colors in any optimum, giving one unique fixed-root normalization per color partition; an independently found valid square assignment supplies the upper bound of five. In the normalized edge model each color class avoids the root of that color. If no positive degree is three on the remaining four vertices, such a class is a matching. If a vertex has degree three, its three neighbors must have even degree within their triple, hence induce either no edges or a triangle. This proves the list of fifteen possible classes and validates the disjoint exact-cover recurrence. Independently, /workspace/reviews/evidence/sk5.py joins compatible local star assignments, enumerating each valid normalized coloring once. It found 201, including 6 with no repeated star colors, with profile histogram (0,6),(2,90),(4,45),(5,60) and respective orbit-size lists [6], [30,60], [15,30], [60]. Degree partitions the roots from the subdividers; every root permutation extends uniquely, acting on the root-normalized color names by the same permutation. Independent fixed-point calculation over all 120 permutations, grouped by cycle type, agrees with the seven displayed counts and gives Burnside sum 720. All five palette names occur, giving 24120 named optima and 195 nonsquare partitions.

## originality

PASS

The full strong odd census, nonsquare excess, profiles and strong odd orbit classification are distinct from inspected prior results. The five-color minimum and the six square color partitions are already covered (the latter through the exact labelled one-factorization count for K6); neither is independent novelty.

## value

PASS

This determines how far parity-optimal coloring can depart from square coloring at the first odd complete subdivision after K3 where a root can have a triple of equally colored neighbors. The precise nonsquare count, profile split and symmetry spectrum give a canonical counterpoint to square rigidity and a reproducible enumeration benchmark; simply recovering five colors or the six known square partitions would not suffice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
