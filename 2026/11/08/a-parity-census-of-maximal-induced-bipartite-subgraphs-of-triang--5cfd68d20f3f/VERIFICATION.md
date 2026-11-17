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

The line-graph equivalence converts a selected triangular-graph vertex set to edges H subset K_n. L(H) is bipartite precisely when H has maximum degree <=2 and only even cycles, i.e. its components are paths, isolated vertices and even cycles of length at least four. One can join endpoints of two paths, so maximality leaves at most one path; an even path of size >=4 can close to an allowed even cycle, whereas one path of odd size or size two cannot. Conversely all other omitted edges create forbidden degree three or odd cycle. The labeled exponential formula counts even cycles with EGF e^{-z²x²/4}(1-z²x²)^(-1/4); multiplying by an arbitrary path SET or the one permissible path gives the two displayed EGFs. Logarithmic differentiation produces c0=1,c1=0,4jc_j=sum_{i<=j-2}c_i and exact even/odd polynomials; singular coefficient ratio c_{m-1}/c_m ->1 gives 2/3. Independent direct adjacency enumeration for n=3,4,5 verified maximality and coefficients and an inspected exact finite component recurrence through 30 (not treated as unrestricted proof).

## originality

PASS

The known optimization and algorithms for maximal bipartite induced subgraphs do not supply the labeled triangular-graph size polynomial. Similar Resultary triangular-graph results address dissociation sets, cluster graphs, and induced matchings: different hereditary predicates, so they do not imply the bipartite-path/even-cycle enumerator. The exact even-cycle exponential form and parity of maximal cardinalities were not found in matching prior published comparisons; residual risk remains for an unindexed bicovered/odd-cycle-transversal table.

## value

PASS

Enumerates a natural NP-hard-type hereditary induced-subgraph property on a symmetric graph family, including all maximal sizes and the exact minimum odd-cycle transversal polynomial. Distinguishing inclusion-maximal from maximum is mathematically consequential; the two-thirds asymptotic identifies the relative frequency of global maxima among all local maximal configurations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
