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

# Reproducibility and limits

Run `python3 verify_nauru.py` in this directory (Python standard library only) and compare its JSON output with `verification_output.json`. Both enumerations of all 7,627 augmented faces agree. The 3,768 explicitly constructed Morse pairs and every one of the 28,836 directed cover incidences are checked; topological sorting certifies acyclicity. The only unpaired cells are 91 simplices of dimension three. All 144 adjacency-preserving graph automorphisms and their edge actions are checked via both explicit symmetric-group actions and an independent exhaustive adjacency backtracking. Signed fixed-face Lefschetz calculations verify the five-by-three character matrix and the nine listed rational irreducible multiplicities; averaging the values gives four invariant classes.

The finite computation is exhaustive for the specific 24-vertex graph. It does not imply any infinite-family classification. The integral homotopy inference uses the standard discrete-Morse theorem, whereas the character computation uses rational Euler–Poincaré trace. No external independent audit has been performed.
