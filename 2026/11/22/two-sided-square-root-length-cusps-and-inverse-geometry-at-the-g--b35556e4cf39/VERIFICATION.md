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

# Verification evidence

The proof uses a direct \(t\)-parametrization of the sphere-cylinder intersection and proves both one-sided length-cusp coefficients by a rescaled local limit. The second coefficient explicitly subtracts the excluded central interval; neither finite-precision calculations nor literature absence are used as proof of the limits.

The portable `checker.py` runs with Python 3, NumPy and SciPy. It cross-checks direct integral lengths against independent three-dimensional polygonal sampling and tests predicted limits at multiple offsets in four different radius pairs. It returned `PASS: 79 deterministic checks` in its recorded execution. These checks do not certify asymptotic estimates for infinitely small offsets and do not constitute independent validation.

Classical geometry, loop topology, and the special Viviani length are acknowledged as prior work. Historical priority remains a risk, especially for inaccessible older specialized treatments.
