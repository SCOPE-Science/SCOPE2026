---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Independent normalization check: in dimension d=m−1 a cubic harmonic is given by a trace-free symmetric 3-tensor. In the sixth probability-sphere moment against (z·x)^3 only the 3! pairings matching all three tensor indices with x survive, giving 6h(x)/(d(d+2)(d+4)); the linear term pairs two tensor indices and vanishes. The stated homogeneous harmonic kernel therefore reproduces h. The angles 0, ±1/2 and the diagonal give G=(k−2a)I+aB*B with k=(m−1)(m−2)(m+3)/6 and a=(m−1)(m+3)(m−11)/48. BB*=mI−J gives the two stated positive eigenvalues for every m≥4 and their ranks; at m=11 they coincide at 210, including all 55 representatives. Invertibility gives surjectivity and the minimum-norm formula by orthogonal projection off ker E; oddness supplies exactly the full-root data constraint. The eigenvalue ratio is the condition number of the Gram on edge data, or the square of the ratio of the nonzero singular values of E. The frozen checker and verification notes were inspected, not executed; no finite checker is needed for this algebraic proof.

## originality

FAIL

A distinct indexed record gives the same cubic spectrum, onto interpolation, and m=11 orthogonality, and extends the problem to degree five. The apparent difference in the cubic eigenvalues is exactly division by the kernel diagonal. The two sector projectors and the pseudoinverse formula do not supply a separate original theorem. This is evidence of equivalent coverage, not a priority or provenance judgment: the comparison path bears a later catalog date, and no dependence or earlier disclosure is inferred.

## value

FAIL

Conditioning on this canonical edge family and the exact all-dimension spectrum would be useful mathematical invariants in their own right. Given the indexed solution of the same problem, the distinct residue is a normalization conversion and standard minimum-energy inversion of the same Gram matrix; it adds no independently useful new invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
