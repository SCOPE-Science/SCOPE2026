---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The rank-preserving action fixes simplices pointwise when it stabilizes them, and the quotient cells are simplex orbits, not just sets of vertex orbits. Keeping the edge orbits distinct and orienting by increasing rank yields the written triangle boundary after a tree collapse. A cell whose word uses a chosen generator once can be collapsed with that edge after pushing the other attaching loops along the resulting deformation onto the remaining graph; cyclic changes of basepoint are harmless. Once one degree-five cell is attached to the surviving circle, every other degree ±5 loop is null there, so each remaining cell gives an S² summand. Independent replay `python /tmp/opencode/singer_review.py` enumerated XOR-closed subsets of sizes 2,4,8, converted nonzero vectors to cyclic exponents, enumerated strict chains and canonically rotated their exponent sets. With a different tree (reverse edge scan) and shortest-word substitutions, for d=1,3,5,15 it got orbit cell counts (65,315,315), (25,105,105), (13,63,63), (5,21,21); elimination counts 251,81,50,16; and terminal degree multisets 64 zeros, 24 zeros, {-5×4,0×8,+5}, {-5×4,+5}. The different numbers of zero or signed degree-five attachments are presentation-dependent and give exactly the same four spaces. The frozen script was inspected, not executed; it asserts all nonzero degrees have modulus five and checks the final sphere counts, not the precise signed frequencies as separate postconditions. Structurally the only nontrivial stabilizers occur at the five F4-lines under C3, and χ is respectively 65,25,13,5. The finding is correct for the stated ordinary geometric quotients.

## originality

FAIL

The claimed new homotopy types are implied by the earlier same-action π₁ and Euler-characteristic results and the existing homotopy classification of finite two-complexes with finite cyclic fundamental group. The frozen rationale correctly notes that π₁ and homology need not classify arbitrary two-complexes, but the cyclic case here has cancellation. The explicit elementary moves produce a self-contained alternate proof, not a new homotopy invariant of these quotients.

## value

FAIL

The free versus nonfree contrast is well motivated and the verification is pedagogically useful. But the advertised new exact invariant is mechanically implied once the already computed groups and ranks are put into the existing cyclic two-complex classification. The finite presentation operations add an alternate certificate and choice-dependent terminal word counts, not a separate invariant or a general algorithmic theorem. That does not meet the novelty/value bar for this narrow exact finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
