---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For z above the free band, the decaying branch solution h satisfies (q-1)h^2-zh+1=0, and the path Green kernel is g h^distance with g=1/(z-qh). The restriction to the string is g(z) C_p(h(z)^d), with finite limit c C_p(r) at the edge. Differentiation of the resolvent gives a strictly negative form on the impurity subspace, so the ordered eigenvalues decrease continuously and strictly to zero. They cross 1/kappa exactly once when the limit at the edge is strictly greater than 1/kappa, and never above the edge at equality. The inverse of C_p(s) for 0<s<1 is irreducible tridiagonal (p>1), so it gives simplicity for the entire z-dependent family, not merely at the edge. The sine recurrence with end conditions v_0=r v_1 and v_{p+1}=r v_p gives the frozen phase equation; its strictly increasing phase runs from 0 to (p+1)pi. At p=1 theta=arccos(r) gives 1/c. Extreme principal-block interlacing is strict: equality would make a padded vector with last component zero an extremizing eigenvector of the bigger matrix, impossible by the last row of its tridiagonal inverse and then recurrence. Expansion of the first and last phase equations gives theta_1 and pi-theta_p equal to pi/p+O(p^-2), yielding the displayed shifts and strict finite endpoints. Also |p theta_j-j pi| is uniformly bounded, so angle counting gives the stated fraction. An independent two-by-two even/odd reflection calculation gives the first two cubic-tree p=4 thresholds 0.257100534504 and 0.953022342560 and the limiting fraction 0.135573653451 at kappa=0.3, confirming the example. The supplied checker was inspected, not run: its finite counts compare two calculations on the edge matrix, while its Dirichlet-ball checks are approximate and away from the edge.

## originality

FAIL

The physically instantiated result is correct, but its spectrum-dependent assertions are covered by direct composition of existing results. The geometric specialization inserts r=(q-1)^(-d/2) and c into the known Kac–Murdock–Szegő eigensystem; the standard monotone finite-impurity reduction translates the same eigenvalues to threshold reciprocals. I did not find a source printing the exact physical statement, but the equivalence and implication are mathematical and do not depend on a verbatim match.

## value

FAIL

Mode counts and the finite-string cooperative window are naturally motivated, and this is a useful worked example. However the precise output is the known finite geometric Toeplitz spectral data in inverse-coupling variables plus standard finite-rank crossing, endpoint expansion and counting. The frozen result has no separate unknown invariant, nonmechanical geometric phenomenon, or stronger conclusion beyond this specialization. The worked example does not meet the threshold for a distinct standalone finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
