---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For every p>=3 with N=2p, full Gaussian window variance 1/(2p), even modulations and translations 0,1, character orthogonality decomposes S=GG* into p two-dimensional blocks. The p=0 seam swaps the two Gaussian half-coordinates; with V_a=sqrt(2p)*(g_a,g_{a+p}) and independent standard complex Gaussians, B_a=0.5(V_a V_a*+W_a W_a*), det B_a=|det[V_a,W_a]|^2/4. Thus H=-p log 4+2 sum log R_a+sum log D_a with R_a~Gamma(shape2,scale1), D_a~Uniform(0,1). Adjacent angular D logs are uncorrelated by conditioning on the shared Haar direction (not jointly independent around the cycle), all radii are independent, hence E H=p(1-2 EulerGamma-log4), Var H=p(2 pi^2/3-3). Nonseam logdet terms form a stationary one-dependent sequence with finite moments; the single seam contributes o_P(sqrt(p)), proving the CLT, and Chebyshev yields the geometric-mean law. Independent full-matrix/block determinant reconstruction checked 75 random instances p=3,4,6; finite tests are only corroboration.

## originality

PASS

Published Asipchuk–De Carli–Rodriguez give subgroup block equivalence but no Gaussian exact logdet moments or growing-p CLT in the inspected relevant text. A same-geometry Gaussian paper gives a Poisson law for the *least eigenvalue*, not log volume; its shared block factorization is credited. A phase-only window theorem has a logdet CLT but uses constant-amplitude independent phases and different exact constants. Its distributional law does not imply the Gaussian amplitude/radius covariance contribution. Best-of-knowledge surviving novelty is these precise Gaussian moments and one-dependent CLT.

## value

PASS

Log-volume is a natural independent conditioning/entropy statistic of a critical random Gabor basis, distinct from extremal frame bounds. The proof correctly accounts for coordinate reuse, finds exact finite-size mean and variance for all p, and identifies a nontrivial 1-dependent Gaussian limit. The seam twist and radial covariance make it more than simply treating blocks as independent Wishart matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
