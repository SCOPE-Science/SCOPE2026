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

# Verification of the mathematical statement

The included standalone `verify.py` uses SymPy identities and high-precision numerical tests. It verifies the exact relation
\[
\frac{d}{dt}\frac{(q-1)^2}{q}=2\frac{(q-1)^2}{q},
\]
the transverse radial exponent \(+1\) at \(q=1\), and the derivative expression proving the observable speed increases on the chosen quadrant \(q>1,z>0\). It also checks the two explicit logarithmic exit-time constants at three fixed thresholds and three initial offsets each, using independent root finding at high precision.

Actual execution result: `VERIFY_OK rational_field_identity=5 positive_monotone_speed=1 threshold_cases=9 bidirectional_logarithmic_delay=18`.

The two-dimensional all-flows exclusion follows from the one-dimensional Poincaré local return-map argument in RESULT.md. Finite examples or numerics cannot prove that universal assertion. The three-dimensional asymptotic expansions are proved analytically via the radial first integral; the numerical tests are auxiliary consistency checks. The result assumes autonomous, complete \(C^1\) vector fields and smooth observables, and does not classify higher-dimensional periodic orbits in general.
