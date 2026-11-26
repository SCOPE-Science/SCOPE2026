---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Deleting ordinary large-shore vertices leaves an incidence forest with a+k vertices, c components and a+k-c edges, hence sum(degree-1)=a-c. At k=a-1 all special vertices must have degree two and their suppressed edges form a tree. The choices of this tree, the assignment of distinct B labels, and the a+1 independent ordinary states biject to the event, giving its exact uniform conditional law and count. For k=a-2 the degree sum permits only a two-component forest of pairs, or one triple and otherwise pairs in a connected incidence tree. In the triple case contracting its three endpoints leaves a tree on a-2 vertices with endpoint multiplicity 3 for each edge incident to the contracted vertex; labelled Prüfer weights give 3a^{a-4}, with the one-vertex case interpreted separately at a=3. For a=2 only the two-component case occurs. No lower class can contribute beyond O_a(b^{a-3}(a+1)^b); the remainder is empty when a=2. Total variation from conditioning is exactly the excluded mass. The second-to-first count ratio is κ_a/(b-a+2), yielding the claimed TV law. The conditional isolated count is binomial and the conditional largest size is a+b minus that count, so the binomial LLN and CLT transfer by TV; the O_a(1) centering difference vanishes on the sqrt(b) scale. All this holds only for fixed a. Correction to the comparison prose at line 114: b/(b+3) is hub connection on K_{2,b}; 3/(b+3) is disconnection, also the exact TV error. The theorem already gives the correct error. Read VERIFICATION.md and verify.py without running them; the checker uses int.bit_count(), available in Python 3.10+, despite the proof document's Python 3.9 compatibility wording.

## originality

PASS

Exact biclique-forest enumeration and connector-rank bounds are already available, including formulas that determine every count in the frozen theorem implicitly. The surviving content is the general fixed-shore conditional product representation on the labelled forest space and its explicit arbitrary-a sharp TV error via the two classified top core types. Neither the known exact-count algorithms nor the closest indexed connector formula states this law, and obtaining it requires identifying and evaluating the extremal classes, not just reading a table or reindexing the count. No chronological priority is inferred between the same-date records.

## value

PASS

The approximation replaces a uniform law on acyclic labelled edge sets by a uniformly subdivided Cayley tree and independent choices at the remaining large-shore vertices. The explicit TV rate controls all labelled events and yields a transparent binomial/normal component approximation; the two error sources separate disconnected pair cores from the first larger hyperedge. This is more than a new table of forest counts and does not claim uniformity in growing small-shore size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
