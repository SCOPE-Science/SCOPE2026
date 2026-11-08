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

# Verification and evidence limits

The mathematical result is proved in `RESULT.md` by reflection-principle survival, an exact renewal derivative, a scaled complementary-error-function kernel, two endpoint asymptotics, an induction by scale separation and implicit differentiation of an everywhere strictly increasing absorption CDF.

Run `python3 verify.py` with the Python standard library. The deterministic program evaluates an independent renewal convolution by composite Simpson quadrature; compares the Laplace-domain sensitivity formula to numerical integration of the time-domain kernel; checks endpoint asymptotics; checks ordered alternating sign samples for three starting-distance classes; and stress-tests the same construction with two, three and four classes. The recorded execution produced 81 passing checks, with sample rank fractions approximately 0.052433, 0.205692, 0.382005, 0.537695, 0.715301, and 0.871015 at the alternating-sign sample times.

Floating-point quadrature, asymptotic spot checks, and finite test configurations are not certificates for all numbers of classes. The universal statement rests on the full analytic proof. No external independent validation is asserted. Primary-literature access for the directly motivating recent preprint was incomplete, so priority relative to its nonabstracted contents remains unverified.
