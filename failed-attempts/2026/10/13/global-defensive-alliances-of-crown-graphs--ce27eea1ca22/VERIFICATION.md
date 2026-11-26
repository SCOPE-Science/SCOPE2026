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

With the closed-neighborhood convention the threshold for a selected vertex in the (n−1)-regular crown is ceil((n−2)/2)=q. For a selected vertex the only missing potential selected opposite neighbor is its matched mate, so a doubled index forces both shore sizes at least q+1; otherwise both must be at least q. Because q>=1, nonempty alliances meet both shores. At n>=5, at least two chosen vertices per shore guarantee domination, at most one being nonadjacent to any given outside vertex. For c=0 the induced subgraph is complete bipartite; for c>0 both sizes are at least three, so any two selected vertices on one shore have a common selected neighbor, and every selected vertex has a neighbor. For n=3,4, a singleton selected shore in the disjoint case leaves the opposite matched vertex undominated, so global alliances are exactly sets with at least two selected vertices on each shore. Expanding (sum_{j=2}^n binom(n,j)x^j)^2 gives both claimed boundary polynomials. The four-state multinomial formula has correct weights, and equality at the minimum 2q for n>=5 requires disjoint q-element shore selections, with exactly the stated multiplicity. The comparison with K_{n,n} uses the closed-neighborhood inequality in both graphs.

## originality

FAIL

The exact all-set defensive feasibility criterion under the same convention already has equivalent indexed coverage. For n>=5 the asserted globality, connectivity, enumerator, minimum and count follow directly from that criterion and the fixed deleted matching; odd-order enumerators are explicitly covered via an equivalent strong-alliance invariant in this regime. The boundary counts add no distinct nonroutine claim. These are statements about available equivalent coverage and implication, not priority inferences from same-day or later displayed dates.

## value

FAIL

The exact structural characterization of a natural graph family would be valuable from scratch. Once the equivalent all-set classification and the odd-order exact polynomial are credited, the remaining counts are the direct multinomial weight sum over known feasible profiles (and the elementary two-shore square at n=3,4). Automatic domination and connectivity follow directly from the known per-shore sizes and a single missing neighbor. No distinct motivated exact result beyond that mechanical specialization survives; the two small expansions or the subtraction from the known complete-bipartite minimum do not rescue it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
