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

The weighted anti-triangular indicator factors as an upper-triangular ones matrix times reversal. Inverting the ones factor gives a first difference; squaring the symmetric inverse yields Jacobi diagonal (2,6,...,6,4) and off-diagonal (-2,-2sqrt(2),...,-2sqrt(2)). The leading-minor recurrence is det(J-tI); positivity follows from the invertible inverse square and simplicity from the nonzero couplings. The positive vector h=(sqrt(2)s,1+s,...,N+s), s=3+2sqrt(2), has zero edge-shifted residual except for a positive residual at N, giving strict positivity above 6-4sqrt(2) by a sum of squares. The constant-coefficient principal submatrix gives theta <= pi/N. Eliminating u_0 gives the effective left ghost ratio a=sqrt(2)/(2-lambda); the right ghost ratio is b=1/sqrt(2). At small theta, both phases lie in (0,pi/2); the positive least eigenvector and the step size theta<pi keep its last phase below pi, so the right boundary forces (N-1)theta+phi+eta=pi, not a higher multiple. The linear phase corrections sum to 1/(1-a(0))+1/(1-b)-1=5+3sqrt(2), with cubic phase error. Consequently theta=pi/(N+c)+O(N^-4); cosine and inverse-square-root expansions give the specified norm deficit and absolute O(N^-4). Independent diagonalizations of the dense compression and Jacobi matrix agreed at six sizes including N=2 and N=250.

## originality

PASS

The supported contribution is finite spectral quantification for the already-known compression: the explicit boundary-modified Jacobi recurrence and the sharp deficit coefficient and phase shift. The compression, use of sinusoidal vectors and limiting constant are not credited as new.

## value

PASS

This canonical Walsh compression was already a motivated spectral object, and its prior approximate eigenvector analysis left the quantitative rate open on the available evidence. The exact recurrence allows finite-index evaluation without the full Walsh matrix; the proven edge law distinguishes boundary effects from the limiting constant and settles a specific previously numerical scale. It need not establish optimality among all truncations to be useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
