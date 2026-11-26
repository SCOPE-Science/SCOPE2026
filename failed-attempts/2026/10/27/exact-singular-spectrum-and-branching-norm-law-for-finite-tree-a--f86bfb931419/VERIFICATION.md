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

For the root-inclusive ancestor inverse B, the edge-difference energy has the extra term |g(root)|^2, so B*B is positive definite and is the ordinary Laplacian plus unit root grounding. On normalized levels and on each child contrast the edge coefficient is -sqrt(b); the sum-zero condition cancels parent coupling. At each level these spaces have the full dimension, giving the stated multiplicities, including the terminal 1x1 block. The determinant recurrence has final diagonal 1-lambda, giving exactly the stated Chebyshev subtraction. II* counts common ancestors and is strictly positive; its simple positive top mode is radial. Its leaf equation and backward difference recurrence give strictly increasing integrated values and hence a positive input. Independently, the lower-triangular radial integration matrix is the lower part of the rank-one array b^((i-j)/2): the omitted upper part has squared Frobenius norm at most (h+1)/(b-1), while the full rank-one norm is sqrt((sum b^i)(sum b^-j)). This gives the stated asymptotic. The path equation has g(-1)=0 and g(h+1)=g(h), giving the stated sine norm. Fresh replay at /workspace/review_replay.py (python3 /workspace/review_replay.py tree) used direct SVD of ancestor-incidence matrices, not the frozen inverse-check code: tested (b,h)=(1,5),(2,2),(2,4),(3,3),(5,2), with absolute full-spectrum discrepancies below 9e-14; also computed independent exact-sum enclosures of the scaled sharp norm. The numerical checks do not certify arbitrary depth. The depth asymptotic is for fixed b.

## originality

FAIL

The earlier finite-tree Cesàro result is on the very same rooted tree and counting space. Its proof gives the orthogonal block decomposition and the actual block matrices, not just an asymptotic list of singular values. Removing the specified depth divisor yields the frozen blocks by a bidiagonal inverse. Its proved Hilbert–Schmidt convergence also yields the frozen sharp norm constant by bounded row multipliers converging strongly to identity. Thus the principal joint claim is mathematically covered by a routine reduction, despite different operators and different stated norm scalings. The standard boundary recurrences do not leave a distinct material claim. This decision does not require a conclusion about inaccessible Rojo–Robbiano full text or the unresolved normalized-ancestor hit.

## value

FAIL

The exact finite spectrum and norm constant would be useful for tree Hardy inequalities, but the frozen result adds only explicit deaveraging, an elementary tridiagonal determinant, and an alternative proof in this regime to previously available block and convergence information. No new regime, stability phenomenon or nonroutine bound is established beyond that implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
