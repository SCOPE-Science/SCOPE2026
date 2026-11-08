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
# Reproducible verification

The standalone `desargues_verify.py` checks the exact graph definition and facet formula, exhaustive face enumeration using two independent predicates, two opposite-order acyclic vertex-toggle Morse matchings (314 pairs), all 2,640 directed face incidences, exact integer Morse attaching maps, an explicit primitive integral three-cycle, independent mod-two boundary ranks, and all 120 permutation actions.

Its recorded output in `desargues_verification_output.txt` has `status` equal to `PASS`. The embedded script uses Python 3 standard library only. To reproduce, place the script and output in one directory and execute `python3 desargues_verify.py`; compare its JSON output with the recorded output, allowing for insignificant JSON whitespace. No external calculation or inaccessible data file is required.

The discrete-Morse matching is established computationally by a complete finite Hasse traversal. It proves a non-equivariant sphere-wedge homotopy type; rational character equality proves the rational representation isomorphism. This does not establish an equivariant wedge equivalence or an integral lattice decomposition. No independent external audit has been performed.
