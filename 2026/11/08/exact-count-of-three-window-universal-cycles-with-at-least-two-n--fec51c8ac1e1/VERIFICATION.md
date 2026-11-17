---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The allowed ordered triples with >=2 nonzero symbols give a balanced strongly connected overlap digraph on q^2-1 nonzero ordered pairs, edge count (q-1)^2(q+2). Its degree pattern is q-1 on pairs containing one zero and q on fully nonzero pairs. The quotient on v_a,u_a and row sums R_a has q(q-2) eigenvalues q, 2(q-2) eigenvalues q-1, and three-dimensional constant block with characteristic polynomial x[x^2-(2q-1)x+q^2-1]; directed matrix-tree gives tau=q^{q(q-2)}(q-1)^{2(q-2)}. BEST factorials yield the exact formula with one distinguished triple fixing rotation, even for loops. An independent exact-integer graph builder gave tree counts 1,108,5308416 at q=2,3,4, exactly the formula. Finite checks are corroboration, not infinite proof.

## originality

PASS

The 2021 full paper by Sawada–Williams constructs shorthand fixed-content cycles; its window set and count objective differ. The 2013 Sawada–Williams–Wong source concerns binary weight ranges and existence, not full q-ary weight-two/three exact counts in accessible material. The most relevant 2026 Mitchell–Wild work generalizes existence to multiple q-ary weights; only abstract and metadata were accessible, so a possible hidden exact enumeration remains a specific priority risk, not a fictitious noncoverage finding. Other Resultary three-letter exact enumerations concern one repeated symbol or noninjective triples, not the distinguished-zero >=2-nonzero language.

## value

PASS

A single formula counts every universal cycle of a natural q-ary two-layer Hamming-weight language (for every q), not just constructing one. The explicit Laplacian factorization and all-size product provide meaningful new exact enumeration for constrained universal-cycle design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
