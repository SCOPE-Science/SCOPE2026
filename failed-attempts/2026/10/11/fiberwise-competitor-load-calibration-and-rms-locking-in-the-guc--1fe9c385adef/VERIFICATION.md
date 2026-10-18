---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For compact invariant μ with no mass on coordinate planes, cutoff logarithmic generator H_eps′(x)=phi(x²)x/(x²+eps) yields E[r_i|X_i]=0 by dominated convergence, without falsely requiring support bounded away from planes. The circulant matrix with rows (a,b,c),(c,a,b),(b,c,a) has determinant (a+b+c)[a²+b²+c²-ab-bc-ca] >0 when coefficients not all equal; hence E[X_i]=mu/(a+b+c). Writing Q_i=mu-aX_i-r_i gives exact variance and covariance by conditional orthogonality, and summing rates gives r1+r2+r3=3mu-(a+b+c)S, yielding aggregate variance defect. Exact symbolic determinant identity and classical parameter mu=1,a=1,b=11/20,c=3/2 check reproduce 20/61 and 60/61.

## originality

FAIL

The main equal-RMS conclusion is directly covered as a special case of the published generalized Lotka–Volterra equilibrium-is-time-average result (Stefano Allesina, §2.4.4, actual full original HTML inspected), and the classical stationary zero-per-capita-growth balance: in variables X_i=x_i², X_i′=2X_i(mu−sum_j Aij Xj), so any fully active stationary measure gives A E[X]=mu*1. The invertible circulant matrix yields the published-style coexistence equilibrium mean, and the advertised covariance/speed defects are the universal conditional expectation Pythagorean identity after the standard one-dimensional stationary generator E[r_i|X_i]=0. Neither cyclic symmetry nor any new dynamical lemma is needed; this specializes a stronger general LV stationarity principle to a textbook 3×3 circulant system. The primary GH literature concerns heteroclinic networks on invariant coordinate planes, which the claim excludes.

## value

FAIL

The equal-RMS law is biologically interpretable but not a new property of recurrent heteroclinic dynamics: it is a direct generalized Lotka–Volterra time-average computation at the coexistence equilibrium. The added fiberwise covariance and variance-speed formulas are generic L² orthogonality upon rewriting the known per-capita drift, with no new sharp nontrivial dynamical boundary. The central GH heteroclinic network is excluded from the theorem by the no-coordinate-plane-mass hypothesis, and no non-equilibrium interior stationary state is constructed or independently characterized. This package is mathematically correct but its proposed invariant is a routine substitution rather than a motivated independent advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
