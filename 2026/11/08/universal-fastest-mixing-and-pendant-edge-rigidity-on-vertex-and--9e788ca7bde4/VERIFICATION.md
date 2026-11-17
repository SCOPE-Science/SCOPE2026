---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For the Fiedler eigenspace E of the core, vertex transitivity makes its projector diagonal constant and edge transitivity makes the averaged squared core-edge displacement 2k*lambda_2/(nd). Lifting each normalized Fiedler eigenvector to leaves with factor 1+t, t=sqrt(lambda_2/d), gives an averaged positive Laplacian Rayleigh quotient equal to (a/(nD))(2 sum_core_edges w+sum_pendants q) <= a/D=alpha by core stochastic budgets; min-max forces spectral SLEM >=1-alpha even without invariant weights. The explicit p*=(1+r(1+t))/(dD), q*=t(1+t)/D satisfies dp*+rq*=1. The 2x2 Laplacian mode blocks over all base Laplacian eigenvalues attain smallest positive alpha; trace and rho_max<=2d bound the largest Laplacian eigenvalue by 2-alpha, controlling the negative Markov eigenvalues. Equality saturates every core budget and makes every lifted Fiedler vector an alpha-eigenvector; positive Fiedler-projector diagonal forces each individual leaf q to q* even for non-invariant optima. Direct independent full-matrix eigenvalue checks on C4,C5,K4,Petersen for r=1,2,3 agreed numerically. Finite spectra corroborate rather than prove global optimum.

## originality

PASS

Older general fastest-mixing SDP and symmetry reduction are appropriately credited, but do not state this universal closed-form leaf-corona optimum or force every unrestricted pendant edge equal. Published one-leaf four-fifths barriers address only a sharp bound and equality class for noncomplete cores; published clique-corona formulas are a special H=K_m case. Neither supplies the full H,r formula with non-invariant leaf rigidity. Best-of-knowledge O, with specialist star-mesh literature a residual risk.

## value

PASS

An exact fastest-mixing spectral constant for an infinite natural family of leaf-corona graphs, valid against all non-invariant symmetric stochastic kernels, is a meaningful optimization theorem. The new local uniqueness of pendant transitions among all global optima identifies structurally forced conductances; the result extends and sharpens previously known special cores, not just the standard SDP formulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
