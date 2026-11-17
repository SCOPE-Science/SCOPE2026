---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For normalized selected measurement v=a|00>+b|01>+c|10>+d|11>, the W3 branch is p I2/8+(1-p)|chi><chi|/3 with chi=(overline(b+c),overline a). Its success probability, capacity and ergotropy follow exactly from its two eigenvalues with H=epsilon sigma_z. Define N=|a|²+|b+c|², zeta=|b+c|² and concurrence Gamma=2|ad-bc|. In u=(b+c)/sqrt2,w=(b-c)/sqrt2 coordinates, triangle and weighted Cauchy–Schwarz yield 1-Gamma<=(|a|+|d|)²+2|w|² <=(3/2)(|a|²+2|d|²+2|w|²), and consequently N<=(4+2Gamma)/3. Separately zeta<=1+Gamma by triangle/AM-GM. Explicit normalized success witness (2sqrt(1-gamma)/3, sqrt((4+5gamma)/18),same,sqrt(1-gamma)/3) saturates N, and ergotropy witness (0,sqrt((1+sqrt(1-gamma²))/2),sqrt((1-sqrt(1-gamma²))/2),0) saturates zeta with |a|²=0. For 0<p<1 these are global P/C and E optima, mutually incompatible if gamma<1. Independently sampled 2000 normalized complex rays and found maximum inequality residuals N-bound=-0.02410782538 and zeta-bound=-0.02679172544, corroboration only.

## originality

PASS

Du–Zhou–Hu October 30, 2026 primary source already proves the exact conditional branch formulas and product (Gamma=0) versus unrestricted Bell (Gamma=1) endpoints. The complete W-state section and outcomes were inspected directly, including Eqs. (39)–(49), and full-text search found no quantitative concurrence-budget parameter or interior all-budget frontier. The new natural 0<=gamma<=1 interpolation yields separate linear maxima N=(4+2gamma)/3 and zeta=1+gamma, explicit different optimizer families and incompatibility for every gamma<1. Known endpoints and standard concurrence inequality are credited. Residual generic numerical-range theorem could imply the budget inequalities but no actual dominating statement was found.

## value

PASS

A quantitative entanglement constraint on the selected measurement outcome naturally interpolates between familiar local/product and Bell/global postselection regimes. Exact all-budget success/capacity and ergotropy frontiers answer separate operational questions, identify optimizers and prove a nontrivial tradeoff: for any submaximal gamma they cannot coincide. These precise benchmark bounds are reusable for this W-state battery model without pretending to quantify physical gate entanglement costs or net work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
