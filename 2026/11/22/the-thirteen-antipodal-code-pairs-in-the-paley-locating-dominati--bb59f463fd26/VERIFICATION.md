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

Enumerated every subset of sizes 0–4 using open traces only at nonmembers, giving accepted counts (0,0,0,0,247). Closed traces at all thirteen vertices pick out 26 of the 247. Constructing both replacement graphs by pairwise symmetric difference and doing breadth-first search from every state gives connected jump and slide graphs, unordered distance histograms (1599,7995,15483,5304) and (858,3432,9087,13403,3588,13). The jump eccentricities are all four, and the slide eccentricities are five for 221 states and six for 26 states. The six affine orbit profiles agree with the frozen table. The endpoints of distance-six pairs are exactly the 26 identifying optima, each occurs once, and the unordered pairs are exactly the thirteen simultaneous translations of the displayed A,B, each intersecting in one point. This is exhaustive only for the labelled Paley graph of order thirteen, restricted to minimum locating-dominating sets.

## originality

PASS

Best-of-knowledge pass for the exact minimum-code exchange geometry, especially the identifying-code/antipode equivalence. The closest distinct indexed computation concerns a different predicate and move regime. The inspected general sources do not establish this profile or equivalence. No priority claim is based on the failed primary-literature lookup.

## value

PASS

This canonical small strongly regular host is a natural test for the impact of locality of moves on optimal sensor placements. The useful structure is not just the size of a finite list: requiring adjacent moves raises the diameter and singles out precisely the optima that solve the stronger vertex-identification problem. The translated antipodal matching gives an exact bottleneck and a reusable benchmark for locating-code reconfiguration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
