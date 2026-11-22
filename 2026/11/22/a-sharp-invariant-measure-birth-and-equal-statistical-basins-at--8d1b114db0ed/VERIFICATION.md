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

# Reproducibility

Run `python check.py` using Python 3 and its standard library. The checker validates exact identities with rational polynomial arithmetic and elements of \(\mathbb Q(\sqrt5)\), plus selected 85-digit Decimal orbit diagnostics. The exact analytic proof in `RESULT.md` is required for the statements applying to every real parameter and every initial state. No finite test is treated as proof of these universal assertions.

# Exact critical identities checked

The return is \(G_c(x)=16cx^2(1-x)^2\). The threshold is \(c_*=27/64\). The critical factorization is \(G_{c_*}(x)-x=x(3x-4)(3x-1)^2/4\). The saddle-node Taylor coefficients are \(H_c=64/81\) and \(H_{xx}/2=-9/4\) at \((x,c)=(1/3,c_*)\). The endpoint \(c=1/2\) has separator \(r=(3-\sqrt5)/4\), its right preimage \(s=(1+\sqrt5)/4\), and exact half-length ghost and physical basins.

# Limits of checks

Only the Proof supplies the global cycle classification, weak-limit and invariant-probability statements, square-root fold asymptotics, and doubly exponential convergence. The checker is reproducibility evidence rather than an independent audit.
