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

# Reproduction

Run `python3 verify.py` with the Python standard library. No network access, private data or external manuscript is required. The code independently sums bilateral-Laplace jump tails and the mixed \(\mathbb E[JT]\) moment, then compares with the closed analytical formula, reflection parity, the symmetric-lattice formula and small-/large-rate regimes.

The recorded execution passed 262 deterministic assertions. Examples: \(D_{\mathrm{eff}}/D\approx1.934807543062\) at \(\delta=1/4,\ell=8\), and \(\approx1.167428083835\) at \(\delta=1/2,\ell=3\).

## Verification limitations

Floating-point checks sample parameter values and cannot prove uniqueness, global asymptotics or a continuum theorem. Those assertions are established by the exact geometric-tail, renewal-reward, hyperbolic monotonicity and asymptotic arguments in RESULT.md. The verifier neither establishes publication priority nor constitutes independent mathematical certification.
