---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

At a positive equilibrium, eliminating the recovered fractions gives the reciprocal system with rows (1,-g/a) and (-h/b,1) and positive right-hand sides 1+g/delta and 1+h/delta. At ab=gh these rows are negatively proportional and inconsistent; below it the reciprocal solutions are negative. Above it both reciprocals are positive and the balance equations give positive susceptible fractions, so the unique solution is in the physical simplex. The prevalence difference is delta(ab-gh)(A delta+B)/(D1 D2) with both denominators positive; each prevalence has form C delta/(D delta+E) with positive C,D,E. This verifies all zero-slope/intercept cases, the strict crossing iff AB<0, simultaneous increase, and the no-reversal obstructions under either homogeneity. For the local stability claim, write c=a y2*, d=b y1*. Eliminating the recovered perturbations for a putative eigenvalue s with Re s>=0 gives diagonal factors s+g+c+cg/(s+delta) and s+h+d+dh/(s+delta), of moduli strictly greater than g and h respectively. The product of the two off-diagonal infection derivatives is gh by the endemic balances, so the determinant cannot vanish. This also independently checks the cited local conclusion. Read the frozen proof, verification notes and CHECK.py; did not execute the frozen code. An independent exact check substituted the three reported rational pairs at delta=1,4,10 into both infection balances, using x_i=1-(1+gamma_i/delta)y_i; all residuals were zero and the ordering was +,0,-. This is an equilibrium theorem, not a proof of global convergence or an empirical prediction.

## originality

PASS

Credit the general network equilibrium theory and the direction of the individual prevalence response to prior work. The supported distinct claim is the exact affine relative-ranking boundary for cross-only two-node dynamics with a shared waning rate, including a strict reversal and its necessary and sufficient conditions. It is obtained by an additional inverse-equilibrium reduction, not by the previously stated componentwise monotonicity or stability theorems. Priority is bounded by the inspected evidence.

## value

PASS

Monotone responses of both coordinates do not resolve which group is higher. The result gives a full boundary for when their ordering can reverse, proves that both kinds of heterogeneity are needed in this model, and provides an exact witness that rules out any general preservation of ranking in this class. This is useful as a diagnostic for relative versus absolute equilibrium comparisons in minimal network models, not as an intervention, transmission forecast, or claim about real groups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
