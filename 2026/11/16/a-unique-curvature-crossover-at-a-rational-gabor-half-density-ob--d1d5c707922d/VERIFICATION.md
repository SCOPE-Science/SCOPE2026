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

The window has cubic decay and its first Zak derivatives converge absolutely; oddness pairs integer and half-integer samples to force the common zero. Real spatial and imaginary frequency derivatives make the cross Hessian vanish. The four derivative coefficients are evaluated through Fourier sine and Mittag–Leffler sums, with a0>0, a1<0 and b0,b1>0; their squares yield positive A,B. Setting u=tanh²(piβ), the claimed B/A=64β² H(u) was independently checked numerically and H prime independently differentiated symbolically in SymPy; P(u)>0 by grouping 284u^7−51u^8+17u^9>=233u^7 and 188u^3−50u^4>=138u^3 on (0,1), so H and β² increase. Leading hyperbolic expansions yield the claimed opposite small/large β anisotropy and local ellipse measure. Independent ratio values at β=.1,.3,.300316196879881,.6,1 corroborate a unique crossing only; the algebra establishes all β.

## originality

PASS

The exact Hessian ratio and full scale monotonicity for this very rational window is an additional local quantitative statement beyond known parity nonframe and two-coset perturbation results; no directly covering mathematical result was identified from the actual full-text comparisons. Ghosh full article unavailable, so retain priority risk rather than treating the access obstacle as a failure.

## value

PASS

Quantifies the local two-dimensional geometry of a natural symmetry-forced Gabor nonframe obstruction, including which direction is soft, the one isotropy scale, and how sublevel area depends on β. Neither the existence of the obstruction nor the known half-coset frame collapse computes these β-dependent local invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
