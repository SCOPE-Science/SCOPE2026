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

# Verification notes

The file `verify.py` is a standalone Python/SymPy computation. Executed on the supplied source, it checked both closed-form adjacent-ratio differences by symbolic simplification, reconstructed the first seven unnormalized mass coefficients using rising factorials, verified the exact rational separating witness \((\nu,q,r)=(1/2,1/2,1/10)\), checked threshold ordering at that witness, and ran rational index tests over several interior parameter values. It completed with an explicit `PASS` message.

The proof of universal index monotonicity is not based on the finite tests: positivity of the displayed polynomial \(S_k\), algebraic positivity of the exact first-step quadratic, and the convergent reciprocal-hazard identity establish the statements for every integer index. The exact rational calculation identifies a DFR yet non-log-convex law without numerical rounding.

No observational data were fitted, no external expert audit was performed, and literature priority is provisional. The public theorem is restricted to \(0<p,q<1\), \(\nu>0\) and the specified discrete hazard convention.
