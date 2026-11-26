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

For the equilibrium renewal age A, the two independent arrays of Gaussian coordinates give (F_x,F_y)=sqrt(2DA)(M_x,M_y) in law jointly with A. Writing m and v for a standard Gaussian maximum's mean and variance, this gives rho=Delta m²/(Delta m²+EA v), with Delta=Var(sqrt(A))>0 even for deterministic resets observed at random phase. With b=Phi^{-1}(1-1/N), Mills' ratio gives b²~2 log N and b(M-b) converges to Gumbel, with second-moment convergence: the positive tail is at most exp(-z) by the normal hazard bound h(x)>=x, and the negative tail for 0<=z<=b² is at most exp(-exp(z/2)) by integrating the same bound between b-z/b and b. For z>=b² it is bounded by 2^{-N} exp[-N(z-b²)²/(2b²)], whose integrated second-moment tail tends to zero. Thus (log N)²v/m² tends to pi²/24. Integrating the equilibrium age tail gives (E sqrt A)²/EA=(8/9)(ES^{3/2})²/(ES ES²); Cauchy–Schwarz gives equality at the upper K endpoint only for constant S. The positive moment quotient cannot be zero but does approach zero for P(S=L)=L^{-7/4}, otherwise S=1, and varying the weight continuously attains every intermediate value. The Poisson coefficient and N=2 anchor follow by substitution. Canceling the common age factor in the ratio works at finite N; the normalized independent maxima differ by a standard logistic in the limit, with log N/b² tending to 1/2. Neither the age effect nor the finite-N variance is a property of independent reset clocks. Reviewed RESULT.md 5–102, VERIFICATION.md 19–23, and verify.py as text; deterministic quadrature and seeded sampling are corroboration only and were not executed. Replay is the exact tail/moment/renewal argument above.

## originality

PASS

The supported distinction is the orthogonal-max finite-size correlation together with the sharp arbitrary-renewal envelope for its logarithmic deficit. The scaling mechanism, clock moment quotient and Poisson coefficient in a different front problem already occur in prior or companion work. The clock cancellation and logistic ratio are elementary consequences of the Gaussian/Gumbel representation, not a new extreme-value law or the basis of the originality verdict.

## value

PASS

Orthogonal fronts can be measured in one configuration. The result separates common-clock size synchronization from clock-free relative shape and quantifies exactly how much clock choice can change the deficit, including which extreme is unattainable. The logarithmic rate alone or the standard logistic ratio alone would be much weaker.

The dated certificate retains the supplied scientific assessment, sources and limitations.
