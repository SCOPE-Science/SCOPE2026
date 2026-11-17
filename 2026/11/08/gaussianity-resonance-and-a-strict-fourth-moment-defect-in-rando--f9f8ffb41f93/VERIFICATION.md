---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The random partition matrix is A=a I-kappa*h*c P_B, where P_B is a rank N-N/p orthoprojector and E[P_B]=(m/c)(I-J). Hence E[A^2]=a^2 J+rho(I-J) and rho=1-2(alpha+kappa m)h+D h^2; the mean-square boundary rho<1 gives exactly h<h_max and the covariance uJ+v(I-J). At h*=2/(2alpha+kappa c), b=-a, so every A is a scalar orthogonal reflection and the conditional stationary Gaussian covariance is deterministic uI. Away from h*, conditioning on the latest partition gives a random contrast variance with pair-cobatching probability (p-1)/(N-1) and Var(||Pw||^2)=4(p-1)(N-p)/(p^2(N-1)^2); conditional Gaussian-mixture Jensen yields the stated strictly positive lower bound. This is valid also if the fourth moment diverges (extended excess). The stationary perpetuity and finite-second-moment uniqueness follow from L2 contraction. Independently enumerated all exact rational equipartitions for (N,p)=(4,2),(6,2),(6,3),(8,2),(8,4), checking projector mean and contrast variance; finite checks do not establish unrestricted N,p.

## originality

PASS

Best-of-knowledge PASS: the inspected time-discrete random-batch error theorems prove strong/Wasserstein convergence and long-time approximation, not a sharp iff Gaussian invariant law or fourth cumulant. Related random-linear samplers and general conditional Gaussian mixtures share techniques but not the parameter-specific global resonance result for uniform repartitioned harmonic dynamics.

## value

PASS

The exact reflection step is an unexpected isolated distributional Gaussianity point within an entire mean-square-stable family of Gaussian-driven discretizations, and the contrast fourth-moment defect supplies a quantitative finite-batch diagnostic. This addresses genuine invariant-measure fidelity questions and is not merely a textbook covariance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
