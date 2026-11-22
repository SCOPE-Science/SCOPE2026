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

Run `python3 verify.py` using only the Python 3 standard library. The program computes all entries of the five-dimensional unrooted Cartier matrix in two exact ways, verifies its decisive minors, implements \(\mathbb F_{11^5}=\mathbb F_{11}[\tau]/(\tau^5-2)\), and checks the ranks \(4,3,2,2,2,2,2,2,2,2\) of the successive unrooted semilinear products. The final ten-factor matrix has rank two and is idempotent. The calculation includes an exact proof-oriented check of base-field fifth-power residues and their degree-five splitting consequences.

The symbolic program checks the nonstandard arithmetic steps; the accompanying mathematical text proves regularity of the differential basis, the cyclic cubic genus calculation, the nonexceptional stable ranks, and the exact scope of the coefficients. A finite computation is not itself a general theorem for other characteristics or other families. An independent mathematical audit has not been performed.
