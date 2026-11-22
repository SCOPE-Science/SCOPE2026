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

# Scientific reproducibility

The proof is analytical: direct generator action, Bloch-block determinant, discriminant factorization, Jordan rank/minimal-polynomial checks, and an exact matrix exponential. The accompanying `verify.py` is an executable supplementary check, not an independent audit or a formal proof of all parameter values.

From a directory containing these files, install `sympy` and `numpy` and execute `python verify.py`. The tested script reports:

`THREE_BATH_GLAUBER_CHECKS_PASSED symbolic=10 exact_generator=5016 finite_spectra=15`

The 10 symbolic assertions include the characteristic polynomial, factorization and exceptional-point identities. The 5,016 rational checks directly evaluate each spin-flip generator on every configuration and every single-spin coordinate on rings of three, six, and nine sites. The 15 full-matrix comparisons test ring lengths six, nine and twelve and five nonexceptional numerical bath combinations. The finite spectra tests do not probe the Jordan order reliably because diagonalizing nearly defective matrices is numerically ill-conditioned; that assertion is established by symbolic algebra.

Limitations: strict parameter assumptions \(0<g,h<1\) and lengths \(3m\) with \(m\ge2\); the third-order modes require \(4\mid m\). Statements concern only the invariant linear magnetization sector, not all generator eigenmodes. Historical priority is not independently certified.
