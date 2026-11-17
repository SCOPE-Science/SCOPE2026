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

# Reproducible exact checks

Run `python3 verify_fifth_power.py` from the directory containing `verify_fifth_power.py` and `shelling_orders.json`, using Python 3.10 or later with assertions enabled. The program relies solely on the Python standard library and exact integer and binary arithmetic. Its output must match `verification_output.txt`.

The full finite proof data are in `shelling_orders.json`: for each integer \(21\le n\le26\), it stores every facet exactly once as an index into the lexicographically enumerated disconnected triples. The program independently checks each permutation, reconstructs all previous-facet ridges, tests the defining pure shelling intersection axiom for every current facet against every earlier facet, and counts the spanning facets. The counts are \(1,12,24,37,51,66\) for ascending \(n\).

For every integer \(13\le n\le20\), the verifier independently reconstructs the Alexander dual of the three-cut complex by forbidding all disconnected triples, enumerates every dual face, determines exact reduced boundary ranks over \(\mathbb F_2\), checks Euler–Poincaré and extracts nonzero reduced homology. Alexander duality transfers the eight lower-dimensional obstructions to the original pure complex. The verifier also tests that there are no disconnected triples for \(3\le n\le12\).

The all-size positive range \(n\ge27\) is **not** established by finite enumeration: it invokes the external theorem of Chauhan and Shukla, arXiv:2603.23155, Theorem 1.4, which covers every \(p\ge2\) and \(n\ge6p-3\). Neither an independent audit nor an independent mathematical validation is claimed.
