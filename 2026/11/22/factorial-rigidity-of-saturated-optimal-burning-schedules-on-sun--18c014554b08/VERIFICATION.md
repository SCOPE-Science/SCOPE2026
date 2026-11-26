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

With r rounds of remaining spread, a core source reaches at most 2r-1 pendants for r≥1 and zero for r=0. A pendant source reaches its own pendant and other pendants only within cycle distance r-2, yielding at most max(1,2r-3) for r≥1 and exactly one for r=0. Thus k rounds cover at most (k-1)²+1 pendants and k-1 rounds cannot suffice. At equality each source attains its bound and the pendant footprints partition the cycle. Since the maximum arc length 2k-3 is less than n, there is no wraparound saturation ambiguity; each odd-length arc has a unique center. Rounds with r≥2 must use cores, the r=1 singleton permits either type and the final singleton must use its pendant. Conversely all such tilings cover every pendant and its core except possibly the final core; the latter has a neighboring nonsingleton block because there are only two singleton blocks and n≥5, and that block's core radius extends one further than its pendant radius. Disjoint cycle intervals of radii h_s,h_t have center distance at least h_s+h_t+1, which exceeds t-s for s<t≤k-1 with h_i=k-i-1. Pendant sources add a step for distinct indices; the last pendant lies outside every earlier footprint so its distance from any earlier core source exceeds k-s, and it is at least two steps from the penultimate source. Thus the constructed schedules satisfy even strict inequality in the stated ignition condition. A clockwise start of the first block gives n choices, arranging the other time labels gives (k-1)! choices, and the penultimate source gives the factor of two. Fixing every source but one fixes the complement footprint; its center and vertex type are forced except for the penultimate switch. This proves the matching. Every ordered schedule fixes at least three center indices if preserved, impossible for a nonidentity symmetry of the cycle, so the dihedral orbit count is (k-1)!. Inspected the supplied C++ enumeration and tiling checker without executing them. An independently written distance enumeration exhausted all 10³ triples on S₅, found 20 schedules and 10 exchange edges each of degree one at its endpoints, and found no two-round success. This corroborates only k=3.

## originality

PASS

The burning model, the scalar sunlet burning number credited to Jenifer–Shanthi, and saturation-based tiling and rigidity on undecorated cycles are prior groundwork. The supported distinct claim is the exhaustive saturated sunlet schedule classification with a two-type penultimate singleton, its exact labelled schedule and dihedral counts, and its matching of all one-round replacements. The closest sunlet proof was inaccessible in this review, so priority is qualified.

## value

PASS

The critical sizes are exactly those where the pendant capacity has no slack, making them a natural rigidity boundary. The known scalar minimum does not characterize the successful schedules. An exhaustive classification gives factorially many optima but the strongest possible fragmentation compatible with any variability: all optima have exactly one local move. This isolates the sole effect of the pendant choice on mobility and gives a baseline for testing what changes below saturation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
