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

Deleting one entry from a decreasing layer decrements its length or drops a singleton, without merging other layers. Terminal-one encoding sends a decrement to deletion of a zero, and a singleton removal to deletion of a 1 from the initial run or from a run of length at least two; deleting any equivalent 1 in that run yields the same output. Independently reconstructed the ordinary binary lemma: if L,R are first/last differences, any common output using deletions at i≤j in the two words can be represented by deletions at L,R, since the positions from i to L in the first and from R to j in the second lie in constant runs by the intervening shift equality. The opposite alignment gives the only other possible output; if L=R there is just one. For L<R two distinct outputs occur precisely when both shift equalities hold through the differing interval, forcing opposite alternating phases over a binary alphabet. The resulting endpoint-zero deletions are always allowed. The other output uses the first and last endpoint ones; the first is deletable only at the beginning or just after a common 1, and the last only just before a common 1 (with equivalent deletion elsewhere in its run allowed). The final 1 lies in the common suffix. Reading the two parities, including the shared following 1, gives exactly the two moves with t≥1 and unique boundaries. Counting marked blocks yields ((1−z)/(1−2z))² z³/(1−z). Heavy parts and gap weights and two-presence are preserved; swaps let two 1s flank a 2, then 121→22 reduces their count to the parity normal form, proving sufficiency and the Fibonacci size product. The gap series for components and isolated vertices are respectively (1+z²)/(1−z) and 1/(1−z)+z², separated by heavy parts of series z³/(1−z), giving both stated rational functions and the n=0 convention. Independent reverse-deck indexing and union-find in /workspace/reviews/evidence/layered_replay.py exhaust n=1 through 11: all edges match their proposed moves uniquely, no pair shares more than two outputs, and all component signatures, sizes and counts agree, including (1280,396,288) at n=11. This is corroboration, not the all-n proof. Frozen scripts were inspected rather than executed.

## originality

PASS

The ordinary alternating-interval criterion, composition deletion channel, and edge-number sequence are prior and must remain credited. The claim that survives comparison is the restricted graph's admissibility-filtered moves, which yield new exact ambiguity-component signatures, Fibonacci product sizes, and enumerators for this adjacency. Same-day results on similar graphs or on the same source under different adjacency do not supply this classification.

## value

PASS

The layered source comes from an established reconstruction problem. A local ambiguity rule propagates into a global classification over an exponentially large source, with exact decomposition and independently useful enumeration of component sizes and singleton behavior. This is more than another interpretation of a known edge sequence. It tells a coding researcher which families of vertices must be considered together, without assuming that a component's code capacity is determined by its size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
