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

Relabeling triples takes any chosen vertex to the lexicographically first one. Deletion removes only that triple, while link removes it and its four disjoint neighbors. Independent include/exclude recursion on available triples enumerated 277,713 and 1,000,971 nonempty faces, respectively. Applying each prescribed pivot to the active set by deleting the intersection with its bit-flipped translate gave critical dimensions {0:1,5:6,8:4} and {0:1,6:23,9:3}. The matching is acyclic without relying on the recorded DFS: in any directed cycle up-arrows are isolated because matching pairs are disjoint, so equal numbers of up/down arrows force alternation. Take the earliest pivot used by its up-arrows. A down-arrow must remove that pivot to restore membership around the cycle; its two incident faces were both free in the earliest pivot pass since each is in a cycle match at that pass or later. They would have been matched then, a contradiction. The Morse CW complexes have no adjacent critical dimensions and one zero-cell, so the integral differentials vanish and the stated reduced groups are exact. Mayer–Vietoris for deletion union the cone on the link gives the two stated short exact sequences of abelian groups; both split because the link groups in degrees 5 and 8 are free. No assertion about higher attaching maps is required.

## originality

PASS

The established contributions here are the two vertex-local integral homology profiles and their consequence for inclusion. Whole-complex rational ranks, integral torsion-free ranks, even the prior ambient homotopy splitting, and an analogous puncture theorem on a different graph do not supply the two local profiles. The exact indexed local match is the frozen item itself.

## value

PASS

Deleting one triple is intrinsic up to symmetry, not an arbitrary restriction. The two local integral profiles isolate exactly how much of each ambient lattice survives without the triple and how much comes from its link, while excluding hidden local torsion. This gives useful data for vertex-filtration and attaching questions in the first mixed-degree triple-Kneser case even without a family extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
