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
# Verification

Run `python3 verify.py` using Python 3.8 or newer. The exact program enumerates the marked Rosenhain locus for eleven prime fields and computes the quadratic-extension genus-two and associated elliptic point counts for seven tuples and two nonzero twists per tuple; it also verifies the full nonsplit marked population and its point count over the characteristic-three field of nine elements. A successful execution prints `VERIFY_ROSENHAIN_NONSPLIT_OK 11_prime_parameter_censuses 14_quadratic_field_curve_checks 24_F9_odd_trace_checks`.

The tests verify the displayed formulas in these finite cases using integer modular arithmetic only. They do not establish the parameter formula for every odd prime power or all extension-degree assertions; those follow from the elementary character count and Galois-cohomological proof in `RESULT.md`. Self-review has been performed; independent audit remains unperformed.
