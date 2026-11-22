---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The exact one-sided quadratures use inverse R_s(u)=U_s^{-1}(u): T_s=sqrt(2) int_0^h R_s'(u)(h-u)^(-1/2)du and A_s=2sqrt(2) int_0^h R_s'(u)(h-u)^(1/2)du. Analytic inversion gives R_s'(u)=alpha A u^(alpha-1)[1-2alpha b A u^alpha+O(u^(2alpha))] with uniform differentiated remainder, alpha=1/k, A=a^-alpha. After u=hq, beta-normalized densities converge in weighted L1; normalization yields the centered first correction -c h^alpha(q^alpha-E_beta Q^alpha) and sharp TV rate if b!=0. Beta recurrence B(alpha,3/2)/B(alpha,1/2)=k/(k+2), combined with rare-side power h^(1/n-1/m), cancels stiffness coefficients to m(n+2)/(n(m+2)). Monomial potentials give exact laws. Independently checked time/area beta moments and period-as-action-derivative in thirteen cases; convergence proof is symbolic.

## originality

PASS

Bakhshalizadeh–Liu–Rezende arxiv:2311.10020 Theorem B and Sec 3 supply piecewise-center nonisochronicity and period quadratures; these are credited. They do not, in inspected material, state distinct conditioned *fixed-energy* time and Euclidean-area probability laws and their centered analytic corrections. Elementary monomial beta distributions are also prior common knowledge. The new joint local result assembles sampling distinction, TV control and universal amplification; other Resultary nearby beta-residence studies address high energies/different potentials.

## value

PASS

Comparing physically distinct sampling measures on asymmetric switching-center orbits yields an interpretable universal less-flat-side bias and a sharp perturbative local law. The fact connects period and action asymptotics to a probability-observable difference, not just a renaming of one Euler beta integral.

The dated certificate retains the supplied scientific assessment, sources and limitations.
