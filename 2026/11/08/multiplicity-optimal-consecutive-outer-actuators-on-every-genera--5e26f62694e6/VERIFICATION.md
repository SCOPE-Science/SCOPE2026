---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

Reconstructed unweighted GP(n,k) Fourier block diagonalization for every n>=5 and 2<=k<n/2. Each real-symmetric two-by-two block M_j has simple eigenvalues; its outer component is nonzero. At a common eigenvalue the outer components of the indexed Fourier eigenvectors form a Vandermonde matrix on the first m outer coordinates (m=|J_lambda|), so the first r=max eigenvalue multiplicity outer coordinates pass the complexified PBH criterion simultaneously; eigenspace dimension proves the matching lower bound. Chebyshev F_lambda(t) has degree k+1 with leading coefficient 2^(k+1), giving r<=min(n,2k+2), and mirror frequencies give r>=2. Independently rederived the GP(11,2) tenth-degree resultant from its five-degree cyclotomic trace polynomial; mod-2 squarefreeness plus exclusion of lambda=0,2 establishes r=2, with Z(GP(11,2))=6 from Rashidi et al. Independently constructed integral Laplacians and modular Kalman matrices for seven (n,k) cases, obtaining full rank at the exact r and deficient rank at r-1. These finite computations corroborate examples, not the universal proof; deficient modular rank alone is not generally a real upper-rank certificate, which here comes from spectral PBH.

## originality

PASS

The all-n,k, fixed-Laplacian dedicated-coordinate placement at maximum eigenspace multiplicity is not established by the primary cited works or relevant published SCOPE theorems inspected. The earlier GP Fourier spectrum and 2k+2 zero-forcing prefix are fully credited. The Resultary identical mirror is the same submitted finding and is not a separate predecessor. Originality is a best-of-knowledge conclusion, conditional on residual risk in unindexed specialist control literature.

## value

PASS

For an infinite two-parameter family of canonical cubic networks, a natural fixed-matrix control-design invariant (minimum number of independently actuated coordinates) equals a clear algebraic lower bound, with an explicit sharp attaining placement. This is not automatic for arbitrary graphs or for predetermined coordinate-restricted inputs. GP(11,2) demonstrates a motivated strict distinction from the established six-vertex zero-forcing requirement: two sufficient fixed-Laplacian actuators. The theorem is appropriately bounded to unweighted Laplacians, not robust independent perturbation models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
