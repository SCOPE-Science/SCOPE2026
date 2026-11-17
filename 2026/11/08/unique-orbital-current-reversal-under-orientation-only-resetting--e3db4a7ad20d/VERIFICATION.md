---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The stationary angular generator closes m_n=E exp(in theta)=r/(r-in omega). Linear generator balances for E X,E Y, E[X exp(i theta)], E[Y exp(i theta)] and E[XY] express J=E[X dY-Y dX]/dt in a rational function of q=r/k,t=omega/k,a=kappa_x/k. Independent symbolic SymPy expansion of these generator moment formulas exactly matched the displayed quartic numerator P and all positive denominator factors, not just numeric cases. P(0)<0, leading coefficient 2a-3>0 for a>3/2, its linear term is negative, and cubic/quadratic signs yield exactly one Descartes sign variation, hence one positive root and strict reversal signs. For a=3/2 all remaining coefficients are negative. Independent x/y Brownian increments have zero cross-quadratic variation and do not enter mixed first moments; J independent of D_x,D_y. Code also derives generator-vs-age integral finite checks; these are corroboration, not proof of all-parameter uniqueness.

## originality

PASS

Best-of-knowledge: same-protocol orientation-only resetting is studied for free-space nonchiral Brownian motion by Baouche et al; chirality and anisotropic harmonic confinement without this reset rule occur in Caprini et al, while Shee studies position-and-heading resets. Those statements do not imply the displayed exact current polynomial, a=3/2 boundary or unique sign reversal. Relevant primary text/abstract comparisons identify genuinely different reset protocols rather than infer priority by titles alone.

## value

PASS

Exact reversal of mean signed orbital area production, despite a fixed-sign angular velocity between resets, is a substantive counterintuitive dynamical phenomenon. The universal uniqueness and sharp stiffness threshold a=3/2 for all angular speeds yield testable mathematical boundaries for angular-reset control; positional diffusion robustness extends model relevance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
