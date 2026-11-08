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

The mathematical proof is given in `RESULT.md`, under the explicitly defined free Brownian partial-batch model. A standalone checker `CHECK.py` depends only on the Python standard library and can be run with `python3 CHECK.py`. It was executed successfully and printed: `PASS: 7499 checks (exact generator / Fourier recursions / cumulants / conditional clock simulations / tail product).`

The checker uses exact rational arithmetic for finite-population stationary second/fourth and pair-moment balance, the single/two-particle stationary Fourier recursion and the stated cumulant/variance normalization. Seeded conditional clock simulations compare a large finite batch gas with its geometric-age mixture, and numerical products check sharp-tail prefactor convergence. No finite simulation or product truncation certifies an infinite-population limit or infinite-tail asymptotic: the proof independently supplies concentration, uniform moment truncation, exponential-product convergence and a dominated-conditioning argument.

The count includes all scalar assertions performed by the checker. Checks require Python 3, standard library only, and no external datasets. No independent validation or formal proof certification has been performed.
