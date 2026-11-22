---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For n>=3, L=2(n-1), path P_n embedded in cycle C_L is graph-distance isometric. Harmonic completion on the complementary chain is a linear interpolation of the two endpoint values; for any Parseval host analysis W, T*=E*W*, so T*T=E*E. Computing the two-by-two endpoint Gram gives eigenvalues n/2 and n(n+1)/(6(n-1)), plus n-2 ones, hence sharp frame bounds 1 and n/2 while R W*T=I gives exact recovery. The grounded interior Laplacian is tridiagonal (2,-1,-1), sine diagonalizable with j=1..n-2 eigenvalues 2-2cos(jpi/(n-1)); exact condition cot^2(pi/(2(n-1))) and full Krylov degree n-2 for endpoint impulses. In Cartesian power d, fixed occupancy epsilon=(n/(2n-2))^d>=2^-d and full-cycle Poincare plus a Dirichlet sub-box eigenvector bound lambda_min=Theta_d(n^-2), while lambda_max=Theta(d), so condition Theta_d(n^2). Independent constructed E and grounded Laplacians checked all eigenvalues for n=3..15; analytic proof is uniform in n and fixed d. Assessed against actual frozen tree, RESULT.md and verification/check.py, no reliance on log-only success. The precise wording of the cited conjecture could not be independently read, so claim of refuting its exact published formulation remains a conditional citation risk, not a flaw in these unconditional spectral identities.

## originality

PASS

The literature establishes Parseval analysis on the *host* and harmonic extension as a Dirichlet minimizer, but that does not imply the path-data analysis stays tight or yield its full two-endpoint singular spectrum, sharp n/2 frame distortion, or grounded Krylov lower bound. Standard sine eigenvalues and Rayleigh/Poincare tools are known inputs; their combination gives an explicit concrete obstruction in a natural embedding architecture. The most relevant 2026 primary full text was inaccessible because the authorized connection returned vpn_disconnected; this sole access limitation is recorded as a residual risk, not an automatic originality failure. The exact purported conjecture wording was not independently validated.

## value

PASS

The exact input-data frame distortion matters in graph-wavelet analysis because perfect reconstruction by restriction can disguise non-tightness, and the n/2 sharp ratio quantifies that discrepancy. The grounded solve shows quadratic condition growth for isometric, constant-occupancy host embeddings, a motivated counterfamily regardless of whether a particular conjecture was worded exactly as described. These are natural structural boundary facts, not an arbitrary numerical slice or a trivial normalization sanity check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
