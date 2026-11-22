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

Use Python 3 standard library. From the directory containing the included files, run `python3 verify_decks.py` and `python3 verify_structural.py`.

`verify_decks.py` generates all indexed binary words avoiding `001` at each length \(1\) through \(12\), explicitly computes their sets of *distinct* length-one-deletion descendants and counts all pairwise and triangular graph relations. It compares the counts with exact rational-series coefficient data.

`verify_structural.py` independently generates alternating difference intervals, admissible left and right contexts and all legal long-interval splices through length ten, compares actual edge/triangle sets with deletion-graph sets, and tests the rational-series and cumulative identities through length thirty-two.

Both were executed from the complete standalone script files with successful exits. Their finite test ranges are not proofs for all lengths; the full proof derives both rational functions from published edge and triangle normal forms and local avoidance conditions. The primary Type-A equivalence and the unrestricted three-edge normal form are scientific premises; the listed scripts do not reconstruct those published results for arbitrary alphabets.

No independent mathematical audit has been performed.
