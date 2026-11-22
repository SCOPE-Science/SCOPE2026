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

# Reproduction of the exact quotient calculation

Run `python3 verify.py` with Python 3.10 or later. This checks the graph and forbidden triples on every mask, exactly enumerates the two fixed-vertex generators and all 120 graph automorphisms, checks the 55-generator simple-connectivity elimination of the original complex, constructs 9905 nonempty strict flags and 118 group-orbit cells, verifies both cellular boundary compositions, and performs integer-unimodular pivot reductions to 9, 26, and 23 unit factors with zero remainder.

`verification_output.txt` contains the deterministic recorded successful output, reproduced by execution of the included script. The algorithm uses Python's standard library, no floating-point arithmetic, no external datasets and no third-party software. The argument from these finite certificates to the homotopy type also uses Armstrong's orbit-space fundamental-group theorem and standard Hurewicz and Whitehead theorems; the code does not attempt to replace those infinite-theory results.

The package records one self-review. No external independent audit or certification has taken place. Unindexed prior work may remain relevant to originality.
