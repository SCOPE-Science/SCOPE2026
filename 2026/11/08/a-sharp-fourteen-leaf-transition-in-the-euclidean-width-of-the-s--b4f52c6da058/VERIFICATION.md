---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For each coordinate-ordered cone, decompose centered normal u into nonnegative nested centered indicator rays with adjacent gaps. Each simplex width is linear in those gaps. Strict Euclidean triangle inequality, since distinct step rays are not positive collinear, excludes non-step minimizers. A b-leaf cut meets exactly 2^m-2^(m-b) hub tubes, and squared normalized width is [(2^m-2^(m-b))^2(m+1)]/[b(m+1-b)]. Reflect b>n/2 to smaller b; prove consecutive f_n(b) decreasing for b>=2 from the exact A_b,T_b inequalities. Comparing b=1 to balanced b=floor(n/2) yields unique 1-leaf minimizer m<=13, unique balanced minimizer m>=14. Exact rational checks independently verified all minimizing sizes through m=100, including n=14/15; finite confirmation supplements all-m proof.

## originality

PASS

The exact Euclidean width and all minimizing normals of the fixed unit tube-simplex stellohedron are distinct from its Ehrhart polynomials, inball/circumball, asymmetry, principal-axis covariance and random-direction width distribution, despite identical underlying star graph. The sharp m=14 transition is not an algebraic consequence of those different extremal statistics. A more general min-width theorem phrased for generalized permutohedra remains an unexcluded bibliographic risk.

## value

PASS

Intrinsic Euclidean minimum width is a canonical invariant of a natural graph-associahedron realization. The exact switch at fourteen leaves from singleton to balanced cuts and complete equality classification are mathematically non-obvious and resolve the invariant in all dimensions; the result is more than a small numerical lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
