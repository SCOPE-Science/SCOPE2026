---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Subtract the time-zero derivative row from each of the other two rows of the Poisson mean Jacobian. Its determinant is, up to sign, (theta/lambda)(1-e^-q)e^-z h(z). Squaring and dividing by the three means gives the stated Fisher determinant, with variable part e^-2z h(z)^2/(e^-z+rho). The strictly concave h vanishes at 0 and q, is positive between them, and has strictly signed endpoint slopes. The log determinant is strictly concave and goes to minus infinity at both ends, proving one interior maximum at fixed nominal parameters. With G=2h'/h-2+1/(1+rho e^z), both G_z and G_rho are strictly negative, so dz*/drho=-G_rho/G_z<0 at fixed q. The limiting scores at zero and infinite rho bracket the score strictly and converge uniformly on compact interior intervals; their unique roots give the two strict bounds. For the short horizon, put z=qv and factor h(qv)=q^2 v(1-v)[1+q(2v-1)/6+O(q^2)]/2, analytically in a neighborhood of v=1/2. The derivative in v of the leading log score is -16 at 1/2. Its first-order score perturbation is q(2/3-2+1/(1+rho)), which gives the claimed coefficient. The local branch is the global maximizer by uniqueness. At large q the limiting score is strictly decreasing, with opposite signs at 1 and 2; convergence on compact subsets brackets the finite-q root at the limiting root. A separately written diagnostic reproduced t*=1.043396317665198 and the determinant ratio 2.013109816346372, and independently compared the analytic determinant to the direct Jacobian computation.

## originality

PASS

Best-of-knowledge pass for the uniquely optimal pinned-endpoint middle snapshot in the instantaneous single-exponential Poisson-plus-constant model, its strict background-ratio sensitivity, and its explicit temporal limits. The Fisher information construction and exponential-plus-constant Jacobian are not novelty claims.

## value

PASS

With only one free snapshot in a saturated joint design, the result gives a usable rule for scheduling under background uncertainty: increasing the background moves that date strictly earlier rather than leaving it at the Gaussian optimum or the midpoint. The limits quantify when the scale is T and when it is 1/lambda, and the numerical example shows a substantial determinant gap within the declared design space. The contribution is the strict analytic comparison and calibration, not use of Poisson Fisher information by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
