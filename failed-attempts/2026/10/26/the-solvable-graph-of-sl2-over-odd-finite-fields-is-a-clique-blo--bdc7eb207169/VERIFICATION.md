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

The graph and all formulas are correct in odd characteristic. A nonscalar traceless matrix has full matrix centralizer spanned by I and x, hence traceless centralizer F_q x. A two-dimensional subalgebra is nonabelian; choosing a nonzero derived generator z with [h,z]=lambda z, trace cyclicity gives tr(z^2)=0. Odd characteristic and Cayley–Hamilton make z nilpotent, and its kernel is a rational invariant line for the subalgebra. All such subalgebras are the rational-line stabilizers. A nonzero nilpotent projective matrix line gives one singleton label, split semisimple lines give one label per unordered pair, and the remaining q(q-1)/2 lines give isolated K_m fibers. For the middle graph, the unsigned incidence block satisfies BB^T=(n-2)I+J; singular sectors give 0,n+1, the two stated quadratic roots, and 2n on ker B. Fiber constants scale these by m and fiber-zero-sum vectors give m(d+1). The matrix-tree divisor is mn(n+1)/2, giving the prefactor 2/n. The pendant matching, edge factorization of even K_n, and intersecting-label distance argument give the remaining invariants. Independently checked every matrix pair by det(x,y,[x,y]) versus projective invariant-line incidence for q=3,5,9 (325, 7626, 264628 pairs); q=9 used F_3[u]/(u^2+1). For q=3 the actual large-component Laplacian characteristic polynomial matched and a cofactor was 1034851547969748992. Analytic replay: the invariant-line argument and incidence and fiber blocks in RESULT.md; finite replay: enumerate trace-zero triples and projective lines as above. Frozen verify.py was inspected rather than executed, and finite checks do not replace the field-uniform argument.

## originality

FAIL

The result is mathematically sound but mechanically implied by prior statements in combination. The decisive overlap is stronger than agreement of degree sequences: Towers et al. explicitly give all neighbor rules in terms of the 0/1/2 two-dimensional subalgebras containing a vertex. Dimension and the given class counts recover the complete middle-graph quotient without any additional classification theorem. The claimed middle-graph spectrum is already covered under the alias Q(K_n) by a general published regular-graph spectrum formula. The other outputs are routine blow-up or standard graph operations. This is a demonstrated implication, not a claim that one prior source prints the whole package verbatim.

## value

FAIL

The Lie graph is a natural object and the presentation is convenient, but the exact classification and invariants here are mechanically recoverable from published neighbor data and the known Q-graph Laplacian formula. Repackaging them and verifying small fields does not supply a separate unknown exact fact, nontrivial new structural lemma, or motivated unresolved boundary. This is a value judgment about the frozen contribution, not a claim that the formulas are false or useless as a worked example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
