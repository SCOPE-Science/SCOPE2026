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

# Verification performed

The included `verify_minimal_bidirected.py` is a complete Python-standard-library certificate for graph-isomorphism enumeration, all multipath faces, both orientations of the acyclic face-poset Morse matching on the exceptional graph, exact unimodular integer pivot elimination, the witness's full raw \(2^{14}\) arc-subset enumeration, raw simplicial chain-condition checks and independent mod-two/mod-three boundary ranks.

Running `python3 verify_minimal_bidirected.py` exits successfully and prints `SHARP_MINIMAL_BIDIRECTED_MULTIPATH_TORSION_VERIFIED`. The exact executed output is stored in `CHECKER_OUTPUT.txt`. Its class totals are \((1,2,4,11,34)\), witness mask `127`, orbit size 10, 141 faces including empty, 350 Hasse incidences, and two Smith witnesses. In the first matching the degree-two matrix has size \(2\times9\), one unit pivot and a residual row with entries \((2,2,2)\). In the second matching it has size \(1\times8\) and nonzero entries \((2,-2)\).

An independent original-simplex integer Smith computation also gave thirteen unit factors for degree one, forty units and one factor two for degree two, and twelve units for degree three; the package verifier instead derives the claimed integral homology via its own elementary-integer Morse reduction and confirms raw field ranks. No verification of arbitrarily large or non-bidirected graphs is claimed. Independent audit has not been performed.
