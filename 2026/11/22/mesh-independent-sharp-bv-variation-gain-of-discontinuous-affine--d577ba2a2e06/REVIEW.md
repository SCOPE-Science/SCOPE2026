# Scientific assessment

## Correctness — PASS

The theorem is for each finite nondegenerate one-dimensional mesh and every real \(BV\) input. Exact local normal equations give the two traces \(A(t)=(1-t)(1-3t)\) and \(B(t)=(1-t)(1+3t)\). The full distributional variation of a projected jump includes each local affine slope and each interior interface mismatch. The edge and interior profiles have explicit piecewise quadratic maxima \(16/9\) and \(2\); the single-cell maximum is \(3/2\). Integration against the signed distributional derivative of an arbitrary \(BV\) function gives the universal bound. Single-jump witnesses attain all constants. The packaged exact-rational checker independently recomputes normal equations, witnesses, one-jump profiles and nonuniform multijump inequalities; finite tests are not used to prove the all-input statement.

## Originality — PASS, with historical-priority risk

Wang (arXiv:1107.3903v1, §4, 2011) defines the same discontinuous degree-one finite-element trial space, jump traces, and a coupled DG formulation for TV-regularized inpainting, but the inspected paper does not give the sharp norm of the separate \(L^2\) projector. Nochetto–Salgado (arXiv:1211.1069v1, §3, 2012) proves TV diminution for a **continuous interpolant**, not broken \(L^2\) least squares. Herrmann et al. (arXiv:1804.07477, §§2–4, 2018) define total and discrete variation for DG functions but not this projection norm. Bartels (2012) treats continuous-affine and piecewise-constant TV minimization rather than the present operator. Published-result and semantic searches for exact sharp projection gains, equivalent formulations and degree-one DG norms found no implication of the claimed three-value law. Historical priority remains qualified because an equivalent identity could occur in unindexed numerical-analysis literature.

## Value — PASS

The result answers a natural quantitative question for the local \(L^2\) projector onto discontinuous linear finite elements: how much can projection amplify the **full** total variation of a discontinuous signal? Mesh-independent exactness, the nontrivial \(3/2\to16/9\to2\) cell-count transition, and explicit step extremizers give a usable stability calibration for discontinuous Galerkin and TV-sensitive reconstruction. The interface contributions are essential rather than a cosmetic normalization change; this projector is not TV-diminishing, unlike deliberately constructed TVD interpolation maps. No multidimensional or high-degree bound is asserted.

## Remaining limits

No claim of uniqueness in the full historical literature, no independent external audit, and no transfer to continuous spline projection or DG elliptic solvers. The finite checker supplements the analytic proof.

Self-review: passed. Independent audit: not yet performed.
