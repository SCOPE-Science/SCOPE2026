---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The uniform homotopy classification is proved by the explicit graph decomposition, a forced-matching parity argument, a two-cone recurrence for open-ladder perfect matching complexes, an exact identification of the exceptional simplex's attaching subcomplex with a path-independence complex, and the standard classification of those independence complexes. This is a structural proof for all \(n\ge2\), not a deduction from finite enumeration.

The accompanying `VERIFY.py` is standalone Python 3 with no third-party dependencies. It exhaustively generates the perfect-matchings of the deleted graph for widths \(2\le n\le13\), verifies the parity rule for the exceptional cross-edge, and for odd widths through \(13\) checks each of the \(2^{n-1}\) subsets of the exceptional horizontal matching against the claimed path-independent-set criterion. For \(2\le n\le12\) it constructs all simplicial faces and reduces them by an acyclic lexicographic face-poset matching; it checks the critical-cell degree and count against the theorem. The exact text of a completed run is in `verification_output.txt`.

The finite computations do not prove an infinite-family statement or establish literature originality. They independently check essential combinatorial premises of the symbolic proof. All homotopy types are ordinary, nonequivariant, and integral. Independent mathematical auditing remains outstanding.
