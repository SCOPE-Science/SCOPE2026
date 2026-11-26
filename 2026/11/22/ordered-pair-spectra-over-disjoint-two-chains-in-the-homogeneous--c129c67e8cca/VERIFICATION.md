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

Reconstructed the count independently of the attached program. Homogeneity identifies types with induced labelled extensions; old predecessors and successors of one new point are an ideal and a filter, and if both are nonempty they are exactly the bottom and top of one old block. This gives N. For x<y the ideals must nest in the forward direction and filters in the reverse direction. The globally predecessor-only or successor-only sectors contribute 2·6^m−1. Among the remaining cases with neither point mixed, x has only successors and y only predecessors, both nonempty, contributing (3^m−1)^2. With just one point mixed the other has two allowed signatures in the mixed block and three choices outside each block, giving 4m·3^(m−1) for the two directions combined; if both are mixed they must share a block, giving m. For x incomparable with y and neither mixed, the two same-sided sectors have 9 choices per block each, and the two opposite-sided sectors have 6 each by requiring disjoint ideal and filter. Removing repeats from empty sides gives 2·9^m+2·6^m−4·3^m+1. One mixed point contributes 2m(4·3^(m−1)−1); both mixed give m^2, since either ordered pair of block choices is allowed. These produce the exact C and I even at m=0, with mixed cases then empty. The stated gap 2C−I=2·6^m−m²+4m−1 is positive, and division by 2T gives the stated quarter coefficient and O((4/9)^m) error. Independently checked the row-annihilator mechanism: non-loop transitions activate a previously zero coordinate and thus each reachable path has at most two such transitions. At the initial state the loop weight is 1; in comparable one-active states it is 3, and in incomparable one-active states it is 1 or 3. With both active the loop weights are 1, 3, 6 or 9 from the printed masks. In the generating function for a row entry each path has one factor (1−weight·z)^−1 per visited state, so the two given polynomials supply sufficient root multiplicities and yield the claimed annihilations. The recorded bounded closure check is corroboration, not the basis for the universal implication.

## originality

PASS

The supported contribution is the exact pair spectrum over an unbounded number of individually named disjoint two-chains and its all-size sharp comparability law. Several exact small-base overlaps are real but do not give this family. No publication order is inferred from the same-day catalogue dates.

## value

PASS

Disjoint two-chains are a natural height-two test where old comparabilities exist but transitivity cannot supply cross-block ones. The all-size comparable and incomparable channels give usable exact invariants and determine the direction and rate of the half-comparability limit. This is not a frequency law for sampled elements of the infinite poset, nor just a comparison of a few small bases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
