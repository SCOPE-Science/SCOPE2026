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

The algebraic identity underlying the proof is the equality of the three computed Hasse--Witt entry-polynomials with \(A=5t(t+2)^4Q\), \(B=5t(t-2)^{12}Q\), and \(U=-t(t+2)^4(t-2)^{11}R\) over \(\mathbb F_{23}[t]\), at exactly twelve positions in the full \(10\)-dimensional cohomology basis. The polynomial Euclidean gcd is \(t(t+10)\). All smooth parameters at which the matrix is zero are precisely \(0,-10\).

Run `python3 verify_sextic_23.py` in the directory containing this file. The standalone checker uses only the Python 3 standard library. It checks the complete symbolic matrix and factorization, independently multiplies the six-term sextic \(22\) times at five parameter values, verifies the smooth rational-parameter rank census, and counts rational points on the two superspecial curves as a separate consistency test. Its output starts with `VERIFIED_P23_SUPERSPECIAL_2_RANK2_5_RANK6_8_GENERIC_RANK8`.

The numerical checks over \(\mathbb F_{23}\) do not establish the geometric classification on their own; the symbolic polynomial factorization, irreducibility of the three quadratics, and invariant-block argument are the proof of the infinite-field statement. Only the displayed family and prime characteristic are covered. Independent mathematical validation has not been carried out.
