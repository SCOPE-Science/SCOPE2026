---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The beta integral gives the stated negative-pool probability, and conditional independence gives the two-specimen correlation Var(Theta)/[p(1-p)]=1/(tau+1). Subtracting adjacent costs and using Q_(k+1)/Q_k=(tau-a+k)/(tau+k) gives the sign of R_k-1 and the stated rational ratio. Its excess over one is positive in the prescribed range, and at fixed a the gamma ratio gives R_k asymptotic to a positive constant times k^(1-a). The crossing therefore gives exactly one minimum or two adjacent minima, including a possible boundary at k=2. For a tending to zero at fixed tau, the sum of squared reciprocal denominators is bounded independently of k, so log Q_k=-a[psi(tau+k)-psi(tau)]+O_tau(a^2) uniformly. Thus R_floor(c/a) tends to c for every c>0, and strict monotonicity brackets every minimizing index to yield a k_* tending to 1. At such indices the exponent has magnitude O(a log(1/a)); its square is o(a), giving 1-Q=a[log(1/a)-psi(tau)]+o(a). Adding 1/k_*=a+o(a) proves the cost formula. The cost tends to zero. For independent statuses, the trial size p^(-1/2) has cost asymptotic to 2 sqrt(p); an optimizer must have k=Theta(p^(-1/2)) from 1/k and 1-exp(-pk) and the cost bound, and its scaled cost tends to the minimum of x+1/x. The three frozen tau=1 examples were also checked separately by integer comparisons: for a=1/d, use the sign of k product_(i=1)^k(di-1)-d product_(i=1)^k(di). Consecutive signs (-,+) bracket the advertised unique minima at k=25,106,1008 for d=20,100,1000.

## originality

FAIL

A distinct published Resultary finding, 3ec6a71f09f8, gives the same threshold, inverse-prevalence limit, and complete digamma constant at fixed correlation, in the same beta-mixture model. Its parameter kappa is the frozen tau and its alpha is a, so the overlap is exact, not a loose scaling analogy. It further incorporates singletons and proves savings throughout alpha<1. A second record, dbb2786143e3, independently overlaps with and extends the exact adjacent-sign classification. The frozen asymptotic, threshold, and examples leave no substantive uncovered remainder. This is an existing-coverage decision, not a claim that the publication path dates establish priority.

## value

PASS

As mathematical content, the fixed-correlation law is useful: it gives both a change of scaling regime from independence and sharp optimizer and cost asymptotics, with an exact finite-size rule. This is more than the observation that correlation helps. That intrinsic value does not make this already covered finding a distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
