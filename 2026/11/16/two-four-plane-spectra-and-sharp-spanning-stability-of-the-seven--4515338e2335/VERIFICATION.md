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

# Exact finite verification

Run `python3 exact_four_plane.py` with Python 3. The program constructs the matrices in a faithful twelve-dimensional integral cyclotomic basis and uses exact matrix multiplication and Newton identities to obtain their characteristic polynomials. It evaluates all \(\binom74=35\) distinct four-plane choices and checks that exactly 21 belong to type A and 14 to type B.

Expected last output line:

`PASS: all 35 exact integer-cyclotomic matrices have the declared characteristic polynomials`

For type A the descending integer characteristic coefficients of \(42A_S\) are `(1, -336, 45864, -3259872, 128357460, -2744515872, 28715767920, -106731172800)`. For type B they are `(1, -336, 45864, -3259872, 128357460, -2744515872, 28795180995, -113401871100)`.

The computation exactly proves the finite matrix identities, conditional on the mathematically documented implementation of the cyclotomic quotient ring; the companion proof derives its entries and factors the resulting polynomials. Numeric diagonalization is not used to establish equality. The calculation does not extend to arbitrary field sizes. Independent mathematical audit has not been performed.
