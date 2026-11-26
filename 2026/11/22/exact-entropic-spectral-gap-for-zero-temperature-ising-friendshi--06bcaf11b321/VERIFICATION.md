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

Each triangle minimizes at one equal bond; conditional on the hub there are three peripheral states forming a unit-rate three-vertex path. The two product sectors are connected by the rate-one hub matching of mixed states, so the full chain is connected and symmetric. Global-flip-even functions orthogonal to constants and functions odd under any leaf swap have zero conditional sector means; the product path Poincaré inequality bounds their eigenvalues below by one. In the remaining global-odd, swap-even block, the lumped bits have rates 2 and 1 and hub reversal contributes a rank-one positive diagonal term of strength 2 at the all-mixed point. The normalized point mass has weights Bin(n,1/3) at 3k by tensoring constant and centered eigenvectors. The secular function increases from minus to plus infinity between 0 and 3; the constant-vector Rayleigh quotient is 2(2/3)^n, strictly greater than the bottom because the constant is not an eigenvector, and <1 for n>=2. The inverse-binomial moment is 1/n+O(n^-2): outside an exponentially small lower tail, expand the inverse around n/3 with quadratic remainder bounded using Var(K)=2n/9. The resolvent shift changes that moment by O(lambda_n). Both asymptotic expansions follow. Independently constructed full Laplacians for n=2–5, confirmed the next eigenvalue is at least one to numerical tolerance, and obtained gaps 0.627718676731, 0.413850444148, 0.278476903921, 0.189144882974, with secular-root discrepancies below 7e-15. Replay: OPENBLAS_NUM_THREADS=1 python3 /workspace/branches/independent_reproduction.py 3 (NumPy).

## originality

PASS

The distinct contribution is the explicit friendship-graph ground-state Markov spectral gap and sharp first correction, not the count of configurations, existence of an entropic bottleneck, or the rank-one formula as a general method. No inspected comparison establishes the same spectrum or implies it without the model-specific decomposition.

## value

PASS

The frustration forces a genuine rare transition between two rapidly relaxing sectors; the exact gap and relative 1/n correction give a normalization-sensitive benchmark for entropic slow relaxation. A conductance estimate or the known ground-state count would not supply this precision. The small symmetry block gives a usable all-size calculation, not an isolated instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
