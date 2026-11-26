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

Cumulative flow after subtracting the sample mean gives B=H^T H and the discrete bridge covariance K(j,l)=min(j,l)-jl/n. In the trace-square sum, grouping by the larger index l gives (n-l)^2 l(2l^2+1)/(3n^2); summing and subtracting the squared diagonals in the off-diagonal Rademacher variance identity recovers the stated variance and factor 4/5. For k plus signs, double-centered distances give a strictly convex function of the ordered locations, so only the endpoint-block vertices of the location polytope can maximize. Relative to the all-prefix vertex, shifting q plus signs past the r=n-k minus signs increases the row-mean contribution to a^T B a by k p q r/n and increases the subtracted pair-distance sum by p q r. Thus the deficit in Z is 4pqr^2/n. The one-switch energy is 2k(n-k)(2k(n-k)+1)/(3n); maximizing its product yields both parity formulas and exactly the listed patterns. Zero means each centered flow is zero. For the interpolated bridge, the integral of its square differs from the discrete normalized energy by at most 2/(3n), since successive scaled increments have magnitude at most 2/sqrt(n). Donsker and the continuous mapping theorem give the limit; the stated KL eigenvalues are those of the Dirichlet Green operator. Independent exact integer enumeration counted 2044 vectors for n=2 through 10 and also verified the pseudoinverse equation. Independent averaging divides the variance by m.

## originality

PASS

The distinct supported contribution is the exact finite sign-probe risk coupled with the parity-dependent worst-case energy and complete equality cases on the unpinned path. Mean from Kirchhoff index, generic Hutchinson variance, Green identities and bridge convergence are standard ingredients rather than independent novelty claims.

## value

PASS

The unweighted path is a natural benchmark for stochastic Laplacian inverse traces: its exact relative noise remains order one for a single probe. The rigid sharp range identifies the atypical sign geometry that saturates worst-case bounds, while the normalized non-Gaussian limit distinguishes typical fluctuation from that worst case. Neither a generic concentration bound nor an average alone supplies both benchmarks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
