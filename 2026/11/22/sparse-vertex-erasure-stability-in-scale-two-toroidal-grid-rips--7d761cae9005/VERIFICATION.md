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

Run `python3 verify_sparse_torus.py` with `link_certificate.json` in the same directory and compare stdout byte-for-byte with `expected_output.txt`. The Python 3 checker uses only the standard library. It reconstructs the vertex link directly from graph-metric inequalities and validates the complete 35-pair sequence without assuming its freeness. It tests the coned sequence on actual finite face sets and checks that the remainder equals the exact induced complex. It verifies the full face vector and 72 removed faces per site for four finite examples, including the dense 20-point periodic erasure in the ten-by-ten torus. It also independently computes the adjacent-pair neighbor-link Euler characteristic.

The infinite-family statement relies on the local isomorphism proof for all cyclic circumferences at least seven and the link-to-global lifting lemma; the finite checks alone do not establish the theorem. The base torus type is credited to prior publications, while this package certifies the direct simplicial collapse under prescribed removals. No independent mathematical validation is asserted.
