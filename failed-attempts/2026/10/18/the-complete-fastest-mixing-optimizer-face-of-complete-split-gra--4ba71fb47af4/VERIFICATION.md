---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Write T for the sum of cross entries, counted once, and X for the clique-to-leaf block. Nonnegative clique rows imply T≤k. On leaf-zero-sum coordinates the trace of the compression is (1−1/m) times the sum m−T of the leaf diagonals, so the SLEM is at least 1−T/m. The contrast vector with levels 1/k and −1/m has Rayleigh quotient 1−(1/k+1/m)T, since only cross edges contribute to its Dirichlet energy. The maximum of the two bounds equals max(1−T/m,(1/k+1/m)T−1); its unique minimizer is the intersection at 2km/(m+2k) if m<2k, or T=k otherwise, including equality at m=2k. At saturation the positive-semidefinite μI−P on the full zero-sum space has zero quadratic form on all leaf-zero-sum vectors, so it kills them. Thus X kills leaf differences, making X constant along each row. In the first regime saturation at −μ on the contrast makes every clique cross-row sum equal, giving a=2/(m+2k). In the other regime T=k forces each such sum to be one and all core entries to vanish, hence a=1/m. For uniform cross entries the remaining unrestricted operator has core-zero-sum block cI−L_B, and the stationary, leaf and contrast modes have the stated eigenvalues. Nonnegativity gives d_i≤c, and the core SLEM band is just c−μ≤λ(L_B|1⊥)≤c+μ. Positive uniform b=c/k proves attainment and has slack in all inequalities when m<2k, proving nonuniqueness. At m=k the lower Laplacian bound is zero and B=0 becomes feasible; below it the positive lower bound forces connected positive support. At and above m=2k, −k/m has modulus ≤1−k/m, so the forced block kernel attains the bound. The one-core-edge example has restricted Laplacian eigenvalues 0 and 1/5 and is optimal but not invariant under all clique permutations. Reviewed RESULT.md lines 34–54 and verification.py; correctness rests on the unrestricted analytic proof, not finite samples or the symmetry-restricted LP.

## originality

FAIL

A distinct same-day record gives the exact unrestricted optimizer face, forced individual cross uniformity and the support/uniqueness phases on the same parameter domain, in block-matrix notation. Setting the core block A=cI−L_B proves mathematical equivalence and gives the connected-support consequence at once; that source even gives a sharp aggregate internal-weight interval. A second, later record explicitly gives the same Laplacian constraints. The optimal value and a canonical solution were already acknowledged, and no noncovered part of the stated finding remains. Same-day listing establishes neither direction of priority; the exact coverage, not a priority inference, is decisive.

## value

PASS

Beyond a known best rate, the full optimizer set answers which individual transitions may be reallocated or removed without sacrificing mixing. The connectedness, optional-edge and forced-deletion regimes describe genuine design freedom across an unbounded family, not a numerical repetition of the minimum. Equivalent coverage prevents a distinct contribution but does not erase the structural usefulness of that classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
