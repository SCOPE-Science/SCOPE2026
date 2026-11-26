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

At fixed j the bounded reset-free Laplace transform solves (r+2)h_j=h_(j-1)+h_(j+1), h_0=1, so h_j=y^(-j). A cycle succeeds with probability h_j and has mean length (1-h_j)/r; renewal gives (y^j-1)/r. Tonelli after conditioning gives M=yA(y)/(y-1) even when infinite. The unit jump rates and the positive-rate change of variable r=(y-1)^2/y agree with this normalization. On 1<y<R, differentiating gives M'=N/(y-1)^2 and N'=(y-1)(2A'+yA'')>0 unless J=1 almost surely. Also N(1)=-E[J]<0 for R>1. Divergence of M at an excluded finite convergence edge, or at infinity for R=infinity and mass beyond 1, forces an interior crossing; a divergent endpoint derivative at finite A similarly forces a crossing. With A(R),A'(R) finite, their left limits give N(R), and N(R)<=0 (including equality) gives the attained boundary minimum, otherwise the strict interior minimum. R=1 leaves no finite positive rate; J=1 gives the unattained infimum 1. For the edge example the term at j=2 in N(2)/C is -1/256. Bounding the positive terms j=3,4 exactly and j>=5 by the decreasing j^(-5) tail gives 75859933/49766400000 < 1/256. For the rare-distance mixture N=-1+epsilon*P(y), with leading coefficient (K-1)q_K at degree K. The root diverges, r/y tends to 1, and the only leading terms of M-1 are 1/y and epsilon*q_K*y^(K-1), yielding both constants and the stated K=2 root. Independent replay /workspace/replay/03.py checked the rational edge sign and 40 finite-volume mean times via direct backward equations for the mean; finite-volume checks do not prove the infinite-support classification. Frozen checker inspected but not executed.

## originality

PASS

The fixed-site mean and point-mass optimizer are prior, averaging that mean is immediate, and a fixed random target is an equivalent quenched-distance protocol in homogeneous translation-invariant geometry. The exact all-law lattice optimizer criterion, a mean-optimal convergence endpoint, and the sharp finite-support contamination asymptotics survive the strongest comparisons. In particular the prior Brownian exponential-target example has an interior mean optimum at a variance threshold, not at the boundary of mean finiteness. Credit the continuum antecedent and distinguish the moments; no absolute historical priority is inferred.

## value

PASS

A common reset rate for a population with fixed but heterogeneous starting distances requires optimizing the averaged objective, not selecting each site's conditional optimum. The sharp finite-domain alternative shows when the optimal rate is forced against a boundary beyond which all population means diverge, and the exact rare-class exponent quantifies how a vanishingly small farthest class controls the optimal rate. These are independently useful finite-versus-infinite and sensitivity statements, not a restatement of a fixed-site mean.

The dated certificate retains the supplied scientific assessment, sources and limitations.
