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

Stochastic Fubini gives X_p(s)=integral_0^s (s-u)^p/p! dW(u), also for p=0. Itô isometry gives V_p and covariance K_p(s,t) with W(t) by integrating the kernel from 0 to min(s,t); scalar Gaussian conditioning therefore gives the stated gain I_p/(t+eta). In I_p', use u=s-t on s>t: the integrand up to its factorial and factor of 2 is ((u+t)^(p+1)-u^(p+1))*u^p. Expansion and integration give the polynomial in y=t/(1-t). Differentiating, the coefficient of y^j in S_p for 1<=j<=p is binom(p+1,j)*[(p+1-j)/(2p+1-j)-1]=-p*binom(p+1,j)/(2p+1-j), with positive constant and leading coefficient -1. This includes p=0, with S_0=1-y. There is one inflection, and H_p'= -I_p*I_p''/(I_p')^2 so H_p first decreases then increases. At small t the polynomial gives I_p'=2t/[(p!)^2(2p+1)]+O(t^2) and hence H_p=-t/2+O(t^2). At t=1 the gain numerator is positive and I_p' vanishes. The sign of the derivative of I_p/(t+eta) on (0,1) is the sign of eta-H_p, yielding the unique interior solution increasing in eta. For z=1-t, expansion of the integral for I_p' gives 2z^(p+1)/[(p+1)!]^2 times (1+O_p(z)). Stationarity gives the claimed z and the integrated numerator loss is 2z^(p+2)/[(p+2)*((p+1)!)^2]+O_p(z^(p+3)). In the optimized gain over the endpoint, that loss subtracts 1/(p+2) of the leading denominator benefit I_p(1)*z/eta^2, which confirms the regret coefficient and sign. Independent checks used the exact p=0 polynomial I_0=t^2-2t^3/3 and bounded quadrature in u=z*v for the endpoint loss and derivative, solving stationarity in z by bisection. At p=1, eta=10^6 the distance and regret divided by the predicted leading terms are 1.000105 and 1.000077, respectively; at p=6, eta=10^21 they are 1.000077 and 1.000068.

## originality

PASS

Credit standard Gaussian risk reduction and the directly sampled Brownian case as background or framework-level overlap. The supported distinct result is the all-order base-process sensing law for integrated targets, including the strict finite-noise interior optimum, the order-dependent exponent and the sharp regret. The closest separately indexed placement theorem controls a different covariance and has terminal placement at high but finite noise. The dissertation's complete scope is unresolved.

## value

PASS

The theorem quantifies when placing a noisy sensor at the endpoint is strictly suboptimal and by how much, for an important distinction in trajectory design: measuring the base process while estimating a smoothed path. The all-order terminal scale and risk-regret distinguish a mathematically real but vanishing gain from an exact endpoint optimizer, while the monotone unique optimum gives a complete finite-noise location rule rather than only an asymptotic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
