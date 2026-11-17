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

# Verification and scope

A standalone Python file `CHECK.py` (dependencies declared in `requirements.txt`) uses SymPy to differentiate the exact first integral, verify the turning-gap velocity ODE, and verify its zero initial value; it uses SciPy quadrature on the original physical-time integral to test the leading constant at multiple amplitudes, positive values of \(h\), and coefficients \(k\) ranging from zero to 100. It also compares the cumulative distribution for the squared turning gap to the analytically predicted one-sided arcsine transform. The test run finished with the exact marker `CUBIC_CENTER_UNIFORM_ENDPOINT_LAYER_CHECK_OK`.

The complete proof of all-amplitude monotonicity, uniform \(O_h(A^{-2})\) period error, and total-variation bound for every real \(k\ge0\) is analytic in RESULT.md, not a conclusion from the finite checker. No proof assistant or external certification is claimed. Independent audit has not been performed.
