---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The formula and asymptotics are correct. The primary 2010 paper gives the resonant Lorentzian amplitude, the threshold \(\gamma_0=\Gamma/2\), zero local minima, the optimized trace distance \(|b(t)|\), and the BLP measure as the sum over its local maxima. Direct differentiation gives stationary times \(2\pi n/\kappa\) and heights \(e^{-\pi\Gamma n/\kappa}\); summing the geometric series gives the claimed closed form. The hyperbolic/boundary amplitude is monotone on the closed Markovian side. Substitution \(\kappa=\Gamma\sqrt\varepsilon\) gives the flat exponential onset, and the Bernoulli expansion of \((e^x-1)^{-1}\) gives the stated strong-coupling series. The inspected checker independently confirms derivative, revival, sum, and asymptotic calculations.

## originality

FAIL

Full primary text of Xu--Yang--Feng was obtained and read. It already gives the explicit resonant trigonometric amplitude, proves that all relevant minima are zero, proves the optimizing trace distance is \(|b(t)|\), and writes the BLP non-Markovianity as the sum of \(|b|\) over all local maxima. Differentiating that displayed elementary function identifies a geometric progression of maxima; summing it and taking standard asymptotics are routine consequences. Under implication-based originality, the fact that the closed sum and flat-onset wording are not printed in the source does not make them independent discoveries.

## value

FAIL

The closed calibration and threshold description are convenient, but once the primary paper has reduced the measure to local maxima of an explicit elementary amplitude, the remaining geometric sum and standard asymptotics are routine exercises. They do not clear the required standalone mathematical-value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
