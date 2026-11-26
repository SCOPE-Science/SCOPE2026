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

Every element of S² annihilates S on either side since S³={0}; conversely any table on A×A with entries in B extends associatively by zero. The requirement S²=B is exactly occurrence of each nonzero label in the table; zero is already produced by products involving B. The size bound gives positive covered mass. With t available labels the diagonals contribute t^r, and equality and inequality pairs contribute t and t(t-1), respectively; inclusion–exclusion gives both displayed counts, including t=1. The unconditioned equality events concern disjoint pairs of entries, giving independent Bernoulli(1/b) variables. The distance to conditioning on coverage is its failure probability, bounded by the union bound; passing to graphs cannot increase distance. Products with B commute, so central generators are exactly the universal vertices. The union bound r b^(-(r-1)) applies before conditioning, with the stated extra TV error. For b=floor(r/(log r+c)), r/b=log r+c+O((log r)^2/r), and both errors vanish. The h-th factorial moment of isolated vertices uses precisely h(r-h)+h(h-1)/2 absent edges and tends to exp(-hc). Components with size k≤r/(log r)^2 have summed tree-and-cross-edge bound O(p) because (1-p)^(r-k)≤C/r; for larger k≤r/2 the cross-edge event alone has bound r^(-k/3). This proves the transfer to the ordinary noncentral graph. Adjoining B preserves closure and commutativity, giving the maximal clique correspondence. Independent small-table enumeration checked six parameter pairs, including the coverage boundary (2,5), the actual multiplication center, and direct commutative subsemigroup enumeration for the two-generator cases.

## originality

PASS

Credit the standard nilpotent table representation, commuting-graph definition, classical connectivity limit for independent edges, and an indexed special case of the conditional graph count. The surviving claim specifies the graph distribution for arbitrary admissible b and transfers the connectivity window to the noncentral graph in the growing-b semigroup ensemble. The strongest same-day match only treats b=2 without universal vertices. No inspected source contains or determines the general conditioned law and sparse transfer as stated.

## value

PASS

Uniform labeled three-nilpotent multiplication is a natural finite algebraic ensemble in which conditioning can distort commutation. The exact graph-frequency invariant quantifies that distortion and handles regimes in which it is not small. The distance estimate then identifies an actual sparse connectivity window for the ordinary noncentral graph, not merely an analogy to independent edges; the clique correspondence connects the law to maximal commutative subsemigroups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
