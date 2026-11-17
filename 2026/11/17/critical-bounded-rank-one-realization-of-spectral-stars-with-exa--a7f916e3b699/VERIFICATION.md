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
# Verification of the stated spectral realization

The proof is self-contained apart from standard spectral-radius, Stirling, rank-one resolvent, and approximation-number identities. Exact checks are the forced Taylor coefficients, their critical \(\ell^2\) membership, the resolvent secular equation, the poles' simplicity, integer-lattice counting, and rank-one singular-value inequalities. Those deductions establish the assertions for all integers \(m\ge2\) and all specified parameters.

`check_spectral_ladders.py` executed successfully, reporting 26 parameter cases, including \(m=2,3,4\), both interior and critical coefficient values, and complex couplings. These finite tests do **not** establish the infinite-dimensional theorem; they check numerical consistency only. The exceptional coupling and endpoint series are proved analytically.

Scope limits: the sharp boundary applies to the particular \(e_1\)-range perturbations with secular function \(e^{az^m}-1\); the count as \(r\downarrow0\) fixes \(m,a,lpha\). No independent mathematical audit has occurred.
