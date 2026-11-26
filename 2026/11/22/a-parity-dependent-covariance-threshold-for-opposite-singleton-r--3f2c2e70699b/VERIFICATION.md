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

Under a fair stationary start and symmetric flip probability p, the edge-flip indicators F_i are iid Bernoulli(p). An independent sign check uses A_i=I_i+J_i=F_i F_{i+1} and D_i=I_i-J_i=(-1)^(X_i) A_i, where I_i,J_i indicate the two trigrams. Then Cov(U,V)=(Var(sum A_i)-Var(sum D_i))/4. A_i has variance p²-p⁴ and off-diagonal covariance p³-p⁴ at lag one, zero at larger lags. D_i has mean zero and second moment p²; the lag-one product expectation is -p³ since the common first flip reverses sign. At lag h>=2 it is p⁴(1-2p)^(h-2), since the two forced flips at the beginning cancel in the sign and the h-2 intermediate flips supply the correlation. Lag two in this computation correctly accounts for the shared endpoint. With N=n-2 positions, weight each positive lag by 2(N-h). For N>=2 the tail sum is [(N-2)-(N-1)rho+rho^(N-1)]/(1-rho)², rho=1-2p, including the empty sum when N=2. Substitution gives p²H_(n-3)(p)/8; for n=3 the two trigrams are incompatible, giving -p⁴/4. The step-two increment of H is (1-rho²)(3+rho^K)>0; H_1=8p(1-p) and H_2=2p(8-9p). For even K>=2, positivity when p<=1/2 follows from H_2 and monotonicity in K. On q=1-p in [0,1/2] the derivative of H_K(1-q) is at least 2, the term 2K(1-2q)^(K-1) being nonnegative, and H_K(1)=-2. Thus there is exactly one crossing, increasing in p with n by the step-two comparison, with p_5=8/9. With p=1-z/K and K even, H_K converges to 6z-1-exp(-2z); its uniquely simple positive root brackets the scaled finite roots from both sides. For fixed interior p the other H terms stay bounded and the linear term yields Cov/n→3p³(1-p)/4. Independent exact coefficientwise enumeration of all 1016 words at lengths 3–9 confirmed the means and covariance, e.g. n=5 gives 2p³-9p⁴/4. Decimal bisection gives c=0.26480563675075367228677..., rounding to the stated number. The aggregate counts and replay method are in /workspace/reviews/evidence/3-markov-replay.md. This replay is finite; the sign classification and moving-root limit follow from the inequalities above. Frozen checker inspected, not executed.

## originality

PASS

General Markov word-count machinery covers computing covariances, so the formula alone is not credited as new general methodology. The bounded comparison supports the complete finite opposite-colour parity/sign classification, monotone unique odd thresholds and sharp near-alternation scale as the distinct contribution. Some older run-covariance text could not be independently inspected; no claim of absolute priority is made.

## value

PASS

Opposite-colour enclosed singleton counts measure the two orientations of local alternation. The transition from strict positivity at every even length to an exactly delimited negative interval at odd lengths is a structural finite-sample conclusion obscured by the positive fixed-p asymptotic. The threshold and its sharp 1/n scale quantify precisely where substituting a limiting covariance would give the wrong sign. This is not an arbitrary table or a claim about all binary patterns.

The dated certificate retains the supplied scientific assessment, sources and limitations.
