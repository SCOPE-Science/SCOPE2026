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

# Verification and limits

`verify.py` runs with the Python 3 standard library. Execute `python3 verify.py` from the directory containing this document. Its output is recorded exactly in `verification_output.txt`.

The verifier enumerates the quotient cell type associated with every support tuple of positive sorted-row difference coordinates, and chooses one or two sheets according to whether the original column stabilizer contains an odd permutation. It then generates the signed incidence differential from the product-simplex facets, tracking the parity of the released column when an interval's terminal coordinate is deleted. All consecutive integer boundary products are zero in the verified cases. Homology ranks are computed independently modulo 2, 3 and 5, and agree with the claimed single top homology rank. A selected square submatrix of the two-term integer difference differential is checked to be triangular with unit diagonal, as predicted in the proof.

The tested cases are every pair \(2\le m\le5\), \(m+1\le n\le\min(m+4,8)\), fifteen pairs. The zero-dimensional case \(m=n\) is handled directly by bijective coloring orbits and does not require a finite homology computation. Computer checks of fifteen pairs are not exhaustive proofs for unbounded parameters; the general proof uses the explicit orbit model, the uniform integer triangular-matrix argument, and classical homotopy results. No independent mathematical audit has been performed.
