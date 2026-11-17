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

Independence forbids two vertices in one column, forces opposite rows for adjacent selected columns. Three consecutive occupied columns necessarily alternate and give the vertex opposite their middle a forbidden third selected neighbor; conversely forbidding cyclic 111 prevents any vertex having three selected neighbors. Every occupied run length 1 or 2 has exactly two row choices. For k selected columns and r runs, count length-two runs binom(r,k−r), positive empty-column gaps binom(n−k−1,r−1), starting positions n/r and row assignments 2^r. Summing cyclic 3-window inequalities gives 3k≤2n and construction attains floor(2n/3); substitution yields all extremal counts. Fresh direct labelled-graph enumeration for n=3..10 checked coefficients independently, including seams and n=3.

## originality

PASS

Best-of-knowledge original component after comparison of exact mathematical implications and source scope. Known constituent techniques and narrower special cases are credited. Full inaccessible relevant texts remain expressly flagged rather than declared not covering.

## value

PASS

The 2-frugal condition is a motivated cubic-graph invariant. This determines the whole cardinality polynomial and all extremal multiplicities for the natural infinite prism family, strictly refining previously known general maximum bounds. It is neither a single isolated number nor a restatement of a coloring count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
