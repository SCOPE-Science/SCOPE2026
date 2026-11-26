---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For 0<p<1 and 0<x<y, substitute s exp(-kz) into the uniform-depth Steele mean. With t=exp(-h) the gain is e/h times D(t)-D(1), where D(t)=exp(-mt)J_p(dt)>0 for t>0. Multiplying D' by exp(xt) gives a constant plus two exponentials; the derivative of that expression has at most one zero. D'(0)=0, D''(0)=pqd²>0 and exp(xt)D'(t) tends to -px, so D' has exactly one root on (0,infinity) and changes from positive to negative. This proves all strict signs and the equality case at onset. The logarithmic secant gives the finite-depth threshold; J'_p(z)-qJ_p(z)=q(1-exp(-pz)) puts onset strictly above qd. For equal duty, J=2 sinh²(delta t/2); the secant grows from onset with slope delta²/[4 sinh²(delta/2)], giving the stated inverse expansion. In Proof §5 the sentence invoking uniqueness alone to force t_*→0 is insufficient, but the needed bound follows directly: dJ'_p(dt)/J_p(dt) is continuous on [epsilon,infinity) and tends to dq at infinity. At its root m=2/t_*+O(1). The crossing is on the increasing branch, hence ma_c is bounded and J_p(da_c) is comparable to a_c²; D(a_c)=D(1) gives a_c=O(exp(-m/2)), then the claimed prefactor and logarithmic constant. No finite replay is used as proof; the supplied diagnostic was inspected, not executed. Bounded asymptotic check: branches/92444bb8-1f76-416f-a40a-0e4deeb9ca55/ordinal-4-math-check.md.

## originality

PASS

The shared Steele response, integrated Beer kernel, time averages and equal-duty experiments are prior inputs. No inspected equivalent or stronger result supplies the two-point depth-dependent sign law, the arbitrary-duty necessary and sufficient onset test and the sharp high-mean cutoff. This is a best-of-knowledge finding, not a claim of exhaustive priority.

## value

PASS

This answers a natural model question at fixed weighted mean with a complete strict sign and equality classification, exact onset and finite-depth tests, and different near-onset and high-light scales. It can benchmark time-averaging approximations in the stated steady-response model. It establishes neither actual growth effects nor management thresholds: excluded are zero lower light, physiological memory, nonuniform biomass and alternative response laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
