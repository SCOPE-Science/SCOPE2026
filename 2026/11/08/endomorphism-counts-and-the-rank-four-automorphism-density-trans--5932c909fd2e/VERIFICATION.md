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

# Verification record
The standalone `verify.py` uses explicit square-free basis multiplication modulo small primes and independent Gaussian elimination on multiplication matrices. Its actual recorded output is `verification_output.txt`; it terminates with `VERIFY_OK`.

It exhaustively enumerated the radical square-zero elements of \(A_3(\mathbb F_3)\) and \(A_3(\mathbb F_5)\) and computed annihilator-rank profiles \((1,2,78,162)\) and \((1,4,620,1500)\) in multiplication ranks \((0,1,2,4)\). Annihilator weighting reconstructs \(S_4(3)=80919\), \(S_4(5)=11328125\). It directly checked \(2^{15}\) radical elements in \(A_4(\mathbb F_2)\), plus rank-one/two counts for small primes and \(72\) invertible substitutions of the two-generator algebra over \(\mathbb F_3\).

No finite enumeration proves the formulas for all finite fields; the algebraic direct-sum and monomial-linear arguments in the proof do. No independent audit has been conducted.
