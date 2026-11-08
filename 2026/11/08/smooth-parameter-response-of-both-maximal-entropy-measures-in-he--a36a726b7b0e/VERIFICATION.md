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

The theorem is proved analytically by constructing a common symbolic coupling and uniformly summable derivative series of affine inverse/forward codings. The core bound for the \(q\)-th parameter derivative of the \(n\)-th increment is \(C_{q,K,M}(n+1)^q\rho_K^{n-q}\) with \(\rho_K<1\) on compact interior parameter ranges. Dominated differentiation gives the response formula, and a complex contraction neighborhood yields polynomial analyticity.

The included `check_affine_response.py` independently constructs finite affine compositions and first derivatives both by reverse-chain recursion and by a forward product series using exact fractions. It also verifies branch image, contraction and truncation bounds. Run with `python3 check_affine_response.py`. Successful output: `PASS: 105496 exact rational algebra/bound checks; finite words, M=2,3,4.`

These finite-word checks are not a proof for arbitrary infinite sequences or all derivative orders. Those steps rely on the displayed analytic estimates and the published parameter-independent almost-sure singleton coding, respectively. Independent mathematical audit has not been performed.
