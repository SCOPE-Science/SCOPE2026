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

# Verification of the directional rank-predictability formulas

Run `python check_directional.py` with SymPy and SciPy available. It performs exact symbolic integration of the squared piecewise conditional CDFs, algebraic simplification of both directional formulas and of the gap, and symbolic differentiation of the sharpness polynomial. It then integrates the original conditional CDF squares via separate adaptive quadratures with domain breaks at the switching curve for parameters \(\theta=0.125,\,0.4396926207859084,\,1,\,2.5,\,10\). The numerical comparisons use absolute error tolerance \(5\times10^{-8}\).

The proof in RESULT.md, not this finite numerical set, establishes validity for every \(\theta>0\), the limiting endpoint values, and unique attainment of the maximum. A one-dimensional root solver supplements the exact proof that the strictly increasing polynomial \(8\theta^3+12\theta^2-3\) has one positive root. The exact published copula and its conditional laws are accepted as prior definitions; the new rank-statistic evaluations are fully derived here. No independent mathematical audit, external certification, or estimator-performance validation is claimed.
