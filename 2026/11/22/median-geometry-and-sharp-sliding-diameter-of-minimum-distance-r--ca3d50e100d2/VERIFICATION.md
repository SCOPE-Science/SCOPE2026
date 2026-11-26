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

Each selected vertex covers at most 2r+1 vertices, so size is at least k. For any k positions, the gaps must be nonnegative and at most r at the two ends and 2r between successive positions; these conditions are necessary and sufficient on an integer path. The deficits from those capacities sum to d∈[0,2r], so interior bounds are automatic, and an admissible tuple exists by putting min(d,r) at the left end and the remainder at the right end. Reconstructing centers from gaps is unique. A right slide of token i transfers one deficit from slot i−1 to i; feasibility ensures the destination is in the path and not occupied. Sorted deficit lists allow no more than r zeros and r entries k, precisely the coordinate bounds L=(0^{min(d,r)},1^{(d−r)_+}) and R=((k−1)^{(d−r)_+},k^{min(d,r)}). On reversing rows these describe the ideals between I(L) and I(R) in the rectangular product poset; difference with I(L) identifies ideals in the induced difference poset. One legal transfer adds/deletes one box, and all one-box moves are realized. Deleting maximal extra boxes and adding minimal missing boxes realizes the symmetric-difference lower bound; majority of three ideals is an ideal and is the unique median for this Hamming metric. The number of available boxes is kd−2(d−r)_+, also the attained L–R distance, so the same value is both diameter and optimal isometric hypercube dimension. Subtracting the two disjoint endpoint violations from all weak compositions gives the stated binomial formula. These arguments include d=0, k=1, and n=1 (the last is a singleton even with d>0). Inspected the frozen checker without executing it. Replay: python3 -B /workspace/review_evidence/independent_checks.py 3; independently built legal slides for 135 path/radius cases, checked 547,440 ordered-pair distances against ordered-token matching, counts and diameters and 10,538 tested median memberships. The equality with the deficit metric can also be seen by counting unit crossings: for each cut i between slots, the number of ordered deficit matches crossing it is the absolute difference of the prefix deficit counts; these prefix differences equal the negatives of the corresponding token-position differences. Finite checks only corroborate the all-size proof.

## originality

PASS

The exact median interval and its state count, sharp diameter and dimension are the supported distinct content for the specified original-path slides at minimum cardinality. The exact transport-distance principle is already implied by the tree subtree-hitting framework, not a separate novelty ground.

## value

PASS

Minimum placements of fixed-radius service vertices along a path are a natural state space. Its full geometry, exact size and minimum binary representation are useful beyond the known shortest-route metric. The sharp reduction in diameter once d exceeds r distinguishes two actual endpoint-capacity regimes and gives the worst reconfiguration cost exactly, rather than fitting finite cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
