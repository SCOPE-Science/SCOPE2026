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

Given the middle Bernoulli X_j, the two path segments are independent. Conditional means are affine in X_j with slopes Cov(X_i,X_j)/Var(X_j) and Cov(X_j,X_k)/Var(X_j); their product times the third central moment of X_j yields the stated factorization. Forward transition means are a_t(1-X_t), 0<a_t<1, so the two covariances are nonzero and alternate with distance. Splitting at j gives the odds equation, and the path recurrence gives the displayed closed form under z=x/(1-x)^2. For odd n, j and b=n+1-j have the same parity: two even factors give odds below one, while two odd factors give positive derivative and limits zero and infinity. For even n reflect to odd j and even b. The numerator of odds minus one is -(1-x)(1+x^(n+2))+2(x^(j+1)-x^(b+1)); it is negative for b<=j. For b>j, pair the powers in the sum after factoring 1-x. Writing x=exp(-u), each ratio cosh(alpha u)/cosh(beta u) for 0<=alpha<beta has strictly negative derivative in u, because alpha*tanh(alpha u)<beta*tanh(beta u). This checks the derivative needed for transversality, not only strict monotonicity. The critical ratio goes from zero to b-j, crossing one at a unique simple root exactly when b-j>1, equivalent to 2j<n, and reflection gives 2j>n+2. Counting triples through j gives (j-1)(n-j). P3 and P4 have no exceptional internal sites; at j=3 on P5 the polynomial z(1+z)^2-(1+2z)^2 is the stated cubic, negative at 3 and positive at 4. My exact checks agree on 840 triples and independently confirm the odds algebra through length 60.

## originality

PASS

The shared middle-site factorization and standard partition polynomial are not distinct contributions. A same-day Resultary tree theorem uses the same factor and includes paths through length 12, but gives only an at-most-once assertion there, not an all-length criterion for when a reversal exists or the exact crossing equation and sharp path onset. The same-day cycle and five-site covariance records are on different geometries or observables. No inspected stronger result supplies the exact all-length open-path parity and position classification.

## value

PASS

The connected three-point function is a natural nonlinear equilibrium observable. Unlike the standard fixed parity of pair signs, its complete finite-size sign diagram separates genuinely reversing triples from the rest and identifies their sharp onset and boundary dependence. The marked-site odds criterion is useful independently as a classification of which internal occupations can cross half density. No macroscopic phase transition is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
