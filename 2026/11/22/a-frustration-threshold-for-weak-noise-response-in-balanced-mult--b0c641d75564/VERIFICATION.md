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

The fair-refresh clock yields actual spin flips at a/2, so its contribution to the linear spin drift is -a, not -2a. At positive a the finite chain is irreducible and reversal symmetry centers M. An independent spectral reconstruction uses the symmetric neighbor matrix P and J=(1+a)I+P. The spin drift is -J; for the stationary correlation matrix C the off-diagonal entries of JC+CJ are zero because no jump changes two sites. Transitivity makes the diagonal scalar, so positivity of J and C_ii=1 give C=J^(-1)/d, where d=tr(J^(-1))/(rn). The eigenvalues of P are 1, -1/(r-1), 0 with multiplicities 1, r-1, r(n-1); the weights of M form an eigenvector at the second eigenvalue and have squared norm 2/n. This gives Var(M)=2/(n*d*lambda), with lambda=a+(r-2)/(r-1); reducing this expression gives the frozen rational formula. The semigroup on M alone has decay exp(-lambda*t), proving both covariance and integration without any statement about the full chain gap. At a=c/n the denominator is 1+2c+c²/n for r=2 and 2(r-2)n+O(1) otherwise, and lambda is c/n versus a positive constant. These yield the two time scales and all four limiting amplitudes. An exact independent rational occupancy-chain check (not the supplied spin-level script) confirmed the variance and generator equation in three finite examples, including r=4. Susceptibility here is defined as integrated stationary covariance, not a general response-to-field identity.

## originality

PASS

The balanced-versus-frustrated distinction as a qualitative signed-graph fact, the bipartite equivalence to a faithful voter model, and standard moment closures are prior ingredients. There is definite prior overlap with the bipartite exponential rate and approximate/asymptotic noisy-voter variance formulas, and with general equal-time order theory. The reviewed claim is the joint exact finite contrast law and quantified susceptibility separation across two versus at least three parts. The inspected sources do not dominate that combined statement; this is not a priority claim for either noise-induced ordering or the use of an eigenfunction for a time covariance.

## value

PASS

An opposed shore magnetization is natural for the unfrustrated anti-voter dynamics, and adding a third shore is the canonical first frustrated complete multipartite case. At identical per-shore size and refresh parameter, the corresponding integrated fluctuation scales differ by order n². The explicit amplitudes and lag limits quantify the distinction without annealed-network approximations, and the exact positive-refresh contrast law is a useful finite-graph benchmark. The value is the quantitative frustrated comparison, not the elementary exponential integration in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
