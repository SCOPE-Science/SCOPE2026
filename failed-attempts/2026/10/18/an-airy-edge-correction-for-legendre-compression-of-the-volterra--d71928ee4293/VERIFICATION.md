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

Integrating the normalized shifted Legendre basis yields the coefficients c_k in the Finding's proof. Subtracting P_nJP_n removes the internal edges and the constant diagonal, but not the edge from n to n+1, so for n≥1 the nonzero block starts at index n. Diagonal phases identify the residual norm with the norm of the compact symmetric Jacobi tail A_n with off-diagonals c_k, k≥n; bipartite symmetry permits taking its top eigenvalue. Independently checked this eigenvalue using the spherical Bessel recurrence: u_k=√(2k+1) j_k^{sph}(z) satisfies the eigenvalue equation at 1/(2z), is square summable by the fixed-argument Bessel series, and satisfies the left boundary exactly when J_(n−1/2)(z)=0. Conversely at any positive eigenvalue set z to its reciprocal divided by two; the discrete Wronskian of the corresponding Bessel solution and the eigenvector is constant in the interior and tends to zero, so the solutions are proportional and the boundary forces the zero. Thus the norm is 1/(2 j_(n−1/2,1)). The fixed-first-zero expansion j_(ν,1)=ν+2^(−1/3)|a_1|ν^(1/3)+O(ν^(−1/3)) gives the claimed constant after inversion; the order shift by −1/2 is lower order at n^(−5/3). The frozen quadratic form is also consistent: v_(n,0)>1 forces the limiting trace to vanish under h=n^(−1/3), and v_(n,m)≳min(m/n,1) yields tight mass and a limiting potential 2x. For the rank comparison, the reversed-time kernel min(x,y) has the Dirichlet–Neumann boundary problem with s_j(J)=1/[π(j−1/2)], so the index n+2 and ratio π/2 are correct.

## originality

FAIL

Demonstrable earlier stronger coverage: Clark's arXiv:2608.12588v1, 12 August 2026, Proposition 1 and Eq. (19), give the exact recurrence coefficients and support of a two-parameter Lommel measure. The prescribed compression residual is, after the textbook Legendre antiderivative and phases, precisely its Jacobi operator for (ν,β)=(n−1/2,1/2). This gives the full spectral support, in particular the exact norm at every positive integer n, not just a similar Airy limit for another operator. DLMF's classical expansion of the first positive Bessel zero then yields the frozen conclusion by elementary inversion.

## value

FAIL

The prescribed operator-norm error is a natural question, but the frozen contribution is a specific asymptotic coefficient already mechanically implied by an earlier exact spectral measure plus the classical zero expansion. No new parameter regime, edge estimate, or general limit principle survives in the stated finding. The specialized quadratic-form proof may have expository use, but is not asserted as a new general tool and does not supply an independently valuable new exact invariant here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
