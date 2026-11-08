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

# Verification record

The complete mathematical proof is in `RESULT.md`. No independently performed external audit is asserted.

Run `python3 verify_biclique_efx.py` using a standard Python 3 interpreter. The script constructs actual recipient bundles, tests all ordered EFX0 comparisons after deletion of every edge in a recipient bundle, separately tests the graph-theoretic source criterion, and checks the exact count. Its run passed \(22\) exhaustive labeled-orientation instances totaling \(142602\) orientations, plus \(9801\) integer symmetry/bounds tests.

The enumerated instances have \(1\le a,b\le5\) and \(ab\le16\). They are not claimed to exhaust all parameters. The universal count follows from the source-neighbor characterization and disjoint zero-row/all-one-column events, and the sharp threshold follows by an explicit uniform remainder bound.

Model limitations: every edge is a distinct unit-valued good assigned to an endpoint; EFX checks removal of zero-valued goods; no arbitrary weights, multi-edges, excluded-zero EFX, or wasteful allocations are covered. No human mathematical certification has been performed.
