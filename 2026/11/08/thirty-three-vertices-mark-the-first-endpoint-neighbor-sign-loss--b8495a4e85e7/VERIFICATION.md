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

For the graph-Neumann unweighted path P_n, n>=2, write s=(1-1/sqrt(2))h and R=(I+sL)^(-1); the L-stable TR-BDF2 end step satisfies T=(1+sqrt2)R^2-sqrt2 R. The endpoint-neighbor entry has sign rho_n(s)-(2-sqrt2), rho=(R^2)_{01}/R_{01}. The tridiagonal hyperbolic Green kernel and s*dtheta/ds=-tanh(theta/2) yield rho_n=1/2+tanh(theta/2)[n coth(n theta)-(n-3/2)tanh((n-3/2)theta)]. The A(x)<B(y) derivative argument makes rho strictly decreasing with path n>=3, so the sharp all-h safe boundary reduces to n=32. Reconstructed degree-125 rational Bernstein polynomial 50000 A32-8579 B32 had strictly positive exact Bernstein coefficients on [0,1/2], [1/2,3/4], [3/4,7/8], [7/8,1]; independently computed positive minima approximately 124263,89947.21,24330.08,1154.04. At n=33,r=10/11 (s=110) the rational witness 50000 A33-8578 B33 is negative (approximately -2373.96). Rational sqrt(2) bounds separate threshold; n=2 direct calculation is positive. Hence iff 2<=n<=32 positive for all h>0; every n>=33 negative at stated h yet positive near endpoints. This proves only entry (0,1), not whole-matrix positivity or the exact number of negative h-bands.

## originality

PASS

Classical TR-BDF2 stability/absolute-monotonicity theory and positivity counterexamples in general positive systems do not fix the endpoint-neighbor matrix entry on graph-Neumann paths. Resultary TR-BDF2 complete-multipartite result concerns diagonal entries of a different graph family. The exact sharp 32/33 cutoff survives available comparison. The plausible Carroll 1993 one-dimensional composite integration paper remained inaccessible: lawful OA/arXiv attempts failed and authorized institutional access returned VPN disconnected; source priority remains qualified, not auto-failed.

## value

PASS

The quantity is a motivated positivity check on the nearest-neighbor heat transfer of a widely used L-stable discretization. A sharp 32/33 graph-size frontier for all positive timesteps, derived by monotonic Green-kernel analysis and a nontrivial rational Bernstein certificate, is a meaningful exact boundary despite only testing one entry; it is not a tiny-instance test or numerical experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
