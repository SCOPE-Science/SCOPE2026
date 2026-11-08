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

# Reproduction and verification

Execute `python3 verify.py` in the directory containing the supplied certificate, `certificates.json`, using a standard Python 3 interpreter. The script enumerates all cyclic orders of nine labels in a canonical rotation-normalized representation and checks all three-query supports on the nine-label ground set. It independently constructs the complete six-label hypothesis class from permutations and binary solutions of every four-term equation. The resulting \(120\) hypotheses are compared as sets. It then checks all \(60460\) candidate supports through query size \(6\), rules out larger supports by the concept cardinality bound, reconstructs all facets and their ten label-permutation orbits, and validates sixty-four exact witness cycles.

Expected terminal line:

`CIRCULAR_TRIPLE_SHATTER_PASS 95284_three_query_supports 504_quadruple_obstructions 120_cyclic_orders 120_cocycles 60460_six_label_supports 6421_faces 2370_facets 10_orbits 64_witnesses`

The full nine-label three-coordinate statement follows from restriction-extension, not from statistical extrapolation. The program does not claim to decide all arbitrary-size supports for arbitrary \(n\), to establish priority against every historic manuscript, or to provide an independent audit. The output certificate is machine-checkable but finite in scope.
