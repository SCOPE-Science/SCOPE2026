---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For r<ell_min/3 each sampled interior point is within along-edge distance r of at most one endpoint. A ball of radius r cannot travel through a whole intervening edge. Away from endpoints it has length 2r; within distance t≤r of a degree-d endpoint its length is 2r+(d-2)(r-t), from the two directions on its own edge and the d-1 possible branches once it reaches the vertex. Integrating over the d edge ends at each vertex adds d(d-2)r²/2 to the unnormalized pair volume. This gives the displayed CDF after division by L², including r=0 by atomlessness. Right differentiation gives exactly the two inverse formulas. The handshake identity gives the Betti formula and degree-two subdivision changes neither degree sum expression nor L. In a tree, summing binom(d-1,2) over the vertices yields B+1, and degree at most three leaves just the degree-three count. The upper bound counts unordered incident edge pairs; if every pair meets, two edges meeting at v force all other edges to meet at v or form a triangle, impossible in a tree. Equality at the bottom is exactly the no-branch path case, including one edge. The proof establishes the finding on its stated class. Simplicity is a standing restriction here, not an independently established necessity; the proof does not need the limitations paragraph's stronger wording about essentiality.

## originality

FAIL

Mémoli–Needham arXiv:1810.09646v5 Lemma 4.18 explicitly gives the same global arclength distance distribution in a unit-total-length normalization at the wider radius r<r0/2. Its combinatorial coefficient is exactly 2B by the handshake identity. Rescaling and taking two derivatives gives the frozen inverse formulas, and the tree claims are elementary degree bookkeeping on the known coefficient. The earlier indexed edge-mixture law independently includes the frozen formula as the direct substitution p_e=ell_e/L. Renaming the coefficient does not make it a new statistic.

## value

FAIL

Extracting graph structure from an unlabeled distance observation is worthwhile, but this local coefficient is already the known q/2. Recovering it from local derivatives, expressing it with Betti and degree data, and obtaining the degree-three tree count and path/star bounds are routine consequences. The frozen record does not identify a distinct new inverse invariant or new recoverability regime that survives the coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
