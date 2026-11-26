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

The closed sum at root edge uv is d(u)+d(v)-f(uv), so completeness of K_n forbids two root degrees below 2. A weight at most n-1 then forces the sole low degree to be zero and the others 2, violating the lower bound on an incident edge. At weight n, a zero degree forces the other n-1 degrees to be at least 3, impossible for n>=5. A degree of one forces exactly one degree-three vertex, which must be the endpoint of the sole incident unit edge. Its edges to all n-2 remaining degree-two vertices must be positive to avoid closed sum 5 on a zero edge, but only two units remain. Conversely all degrees 2 give sums 4 and 3 at labels 0 and 1, and a spanning simple cycle realizes weight n. The associated loopless 2-regular multigraph has uniquely determined doubled edges and simple cycles. On j>=3 chosen vertices there are (j-1)!/2 undirected cycles, and a chosen pair gives one doubled edge, so the component series is ux^2/2+sum_{j>=3}x^j/(2j). Exponentiation gives both stated series; logarithmic differentiation gives the recurrence and the analytic factor at x=1 yields the stated e^(-1/4) asymptotic. Independently enumerating low-weight edge multisets and testing closed sums reproduces weights/counts {5:22}, {6:130}, {7:822} among 2893, 52224, and 1141536 assignments respectively, and separate component counts reproduce all listed values through n=12.

## originality

PASS

The strongest verified analogue has the same rule on a different root graph. The verified same-family statements have different neighborhood constraints and matching, not degree-two, optima. The supported distinction is rigidity for the stated perfect double Italian rule on the complete root graph and the resulting optimizer census, not the labeled exponential formula itself. Best-of-knowledge assessment, not historical priority certification.

## value

PASS

This determines the complete minimum space of a local domination invariant on the canonical clique line-graph family, not only its scalar minimum. It supplies a direct construction of every optimum and its refined enumeration by doubled edges, including factorial-scale growth. Odd cycles and the optimizer family are not captured by the bipartite rook analogue.

The dated certificate retains the supplied scientific assessment, sources and limitations.
