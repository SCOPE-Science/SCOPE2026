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

The graph is unweighted, unnormalized K_{m,n}, with fixed d>1. No equilibrium coordinate is 1. A positive coordinate makes every neighbor positive at equilibrium; connectivity rules out mixed support, and identical input within each part then forces equal coordinates x or y. Dividing the two equations gives F_d(x)/F_d(y)=n/m with F_d(s)=s^{d+1}/(1-s), strictly increasing onto (0,infinity). The resulting increasing smooth y(x) defines L(x)=y/[m x^d(1-y)] with divergent endpoints (near zero y is asymptotic to (m/n)^{1/(d+1)}x). Log differentiation reduces its sign to 1-d^2(1-x)(1-y), whose derivative is strictly positive, and it changes from negative to positive exactly once. This proves the one nondegenerate minimum and the claimed equilibrium counts. The Jacobian restricted to the within-part zero-sum directions is strictly negative; on the part-constant subspace its diagonal is (-1/(1-x),-1/(1-y)), its off-diagonal product is d^2, and its trace is negative. The determinant changes from negative through zero to positive, proving one unstable eigenvalue, one simple zero, or all stable, as claimed. At the fold both left and right null vectors of the collective block can be positive. The left vector pairs strictly positively with the parameter derivative; twice differentiating the equilibrium curve at L'=0 pairs its quadratic field derivative with -L'' times that positive quantity, proving dynamical saddle-node nondegeneracy. At zero, the derivative is -I (one can use a continuously differentiable extension using positive parts), giving local exponential stability on the cube. On a star, x_c<=x_*=1-d^-2 bounds F_d(x_c), so F_d(y_c)=F_d(x_c)/n forces y_c to zero and the product equation gives x_c to x_*. Substituting y_c asymptotic to x_* d^{2/(d+1)} n^{-1/(d+1)} yields the stated constant, including 2^{8/3}/3 when d=2. Minimizing the scalar degree-averaged expression independently gives d^d/[(d-1)^{d-1} mean_degree]; mean degree tends to two and that scalar threshold tends to 2 at d=2. The methods were checked with a separate exact rational unequal biclique witness (m,n,d)=(375,32,2), (x,y,lambda)=(1/3,5/8,1/25), and direct fold-product parameterization for star examples. The tests are supplementary; they are not the proof for real d and all graph sizes. The frozen self-review's phrase 'finite-density adoption' is not used: the hub has a nonzero limiting fold coordinate, but the mean adoption at the fold tends to zero. No basin, stochastic or time-varying exponent claim follows.

## originality

PASS

Credit the exact motivating node-level equation, scalar mean-field fold, homogeneous behavior, symmetry reduction and bifurcation tools as prior or standard. The distinct supported content is the heterogeneous complete-bipartite full-network equilibrium and stability classification in the fixed-exponent model, and the exact star scaling. The closest structural catalogue theorem has a different incidence law, and the primary scalar model is not an exact heterogeneous reduction. Comparisons are bounded to the inspected mathematical statements and passages.

## value

PASS

Complete bipartite graphs are the canonical reduction retaining two genuinely different degrees, and their star limit sharply tests extrapolation of a narrow-degree approximation. The equilibrium table addresses all vertex patterns, the spectral calculation rules out additional within-part instabilities, and the sharp hub threshold explains why degree averaging can miss a qualitative onset change. The value is the exact deterministic threshold and stability, not an asserted nonvanishing global adoption fraction, a stochastic prediction, or a global basin characterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
