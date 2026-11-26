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

Rotate the marked chord to endpoints 0,t. The crossing event has probability q=2t(1-t); given a crossing, one endpoint of the other chord is uniform on (0,t) and the other on (t,1), independently. Their positive difference has mean 1/2 and variance [t^2+(1-t)^2]/12, so the mean crossing propensity of that chord is 1/3+q/6. The resulting cross-projection is q^2/6. The global first projection h=q-1/3 has variance 1/45. The remaining degenerate order-two sum has variance O(n^2), because terms with at most one common index are uncorrelated, and the marked crossings change the n^(3/2)-scaled global statistic by O(n^(-1/2)). A bounded i.i.d. two-dimensional CLT for each first chord, then bounded convergence of the conditional characteristic functions jointly with T and the vanishing remainder, proves the stated mixed limit, including the point-mass deletion variance at degenerate endpoints. Z has a constant conditional law while the positive cross-covariance averages to 1/45; the mixing of nonconstant deletion variances gives positive fourth cumulant, hence a non-Gaussian W. The finite moment sums the n-1 local variances and the (n-1)(n-2) shared-index covariances, giving (n-1)/5+(n-1)(n-2)/45, also valid at n=2.

## originality

PASS

Pass is for the geometry-conditioned joint weak law of the global crossing statistic and the conditionally centered marked deletion noise, not for the covariance formula alone. The strongest prior rank-conditional covariance implies both the geometry-conditioned cross-covariance coefficient and, with the binomial marked-degree variance, the finite mixed moment. This is substantive prior coverage of the second moments and should be credited as such. The compared moment identities and separate marginal or two-global-statistic limit theorems do not determine the conditional mixed-normal law or show independence from the geometry together with dependence on the centered deletion fluctuation.

## value

PASS

The natural intervention of deleting one independently marked chord separates geometry-scale effects from √n local noise. A marginal global CLT, a degree regression, and even exact finite mixed moments do not give the conditional joint law needed to distinguish independence from the geometry from dependence on deletion noise. This structural distinction and the explicit conditional normal mixture are useful on their own, without crediting the known second moments or the standard CLT method as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
