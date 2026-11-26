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

Maximality is equivalent to incidence-freeness of the unmatched shores. With r unmatched on each shore the first two line-incidence moments are 5r and r(r+4); for r>0 Cauchy–Schwarz against the at most 21−r occupied lines gives r≤6. At r=6 equality forces the full six external lines and a six-point hyperoval. Each outside point lies on three secants that pair the six points; the 15 resulting pairings are distinct, giving the duad–syntheme graph. It is regular bipartite, so each fiber exists, and the symmetric differences of its perfect matchings are alternating cycles. Independently rebuilt PG(2,4) from two-vector spans, enumerated all 168 hyperovals and all 288 perfect matchings in each, and verified minimum within-fiber move size four and connectivity at that size. Distinct fibers have equal point and line intersections r≤3. All previously free vertices that become matched require 2(6−r) distinct newly inserted edges (no old free point is incident to an old free line), excluding r≤2 through threshold seven. For every one of the 3,360 remaining fiber pairs, the full 288×288 overlap census had maximum eight common edges with exactly 216 pairs attaining it. The actual quotient is 40-regular with diameter two, so the full graph first connects at seven. Internal degrees 37 and 41 each appeared 24,192 times, and all cross-degrees were 30; reproduced 943,488 internal, 725,760 cross and 1,669,248 total edges. The component conclusions for thresholds ≤6 follow from these exclusions and the four-move connectivity in each fiber.

## originality

PASS

Pass for the first exchange threshold on the whole optimum-matching space and the bridge and degree census. The static size 15, point-only quotient parameters, 288 perfect matchings in one fiber, and the four-edge single-fiber flip structure are credited, not adjudicated as novel. The closest inspected prior statements concern a projection to hyperovals, a fixed fiber, or another graph, not the lifting of every adjacent pair to exactly 216 whole-matching bridges.

## value

PASS

The first connectivity threshold tests when genuinely distinct optimum fibers can communicate under the natural batch distance. It is not merely a new count of already-known states or an arbitrary parameter slice: it distinguishes the four-edge scale of motions inside a perfect-matching fiber from the seven-edge scale where these fibers first communicate. Uniform bridge multiplicity and cross-degree make the geometry of these first lifts precise and would matter in any subsequent study of these dynamics, without claiming a mixing result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
