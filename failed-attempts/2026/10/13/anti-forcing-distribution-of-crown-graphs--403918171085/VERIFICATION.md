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

Relative to a fixed matching, a second matching exists in the retained graph exactly when there is an alternating cycle: a difference of matchings decomposes into such cycles, and toggling any one produces a second matching. Under contraction the allowed arc i->j is equivalent to i!=j and pi(j)!=i, so precisely the derangement inverse cycle cover is absent from the loopless complete bidirected graph. In a linear order exactly one candidate arc per unordered pair is forward. Each missing directed cycle forces at least one missing forward arc, attained by reversing its cyclic vertex order and concatenating the blocks. The remaining max acyclic size is binom(n,2)-c(pi), yielding the stated minimum feedback arc set. Insertion into a cycle of length at least two or addition of a transposition proves the recurrence; labelled cycles of lengths >=2 give the EGF. A cycle of size n-2(k-1) plus k-1 transpositions realizes the full spectrum, and standard cycle-type counts give both extremal multiplicities, including n=3. An independent bounded subset DP through n=7 (append j last, adding the existing arcs i->j for i in the previous subset) agreed; at n=7 the counts at 15,16,17 were 720,924,210. This checks the contraction count only on that range; the universal proof is analytic. Frozen code was inspected, not executed.

## originality

FAIL

A distinct published Resultary record, 2026/11/22/SCOPE-anti-forcing-numbers-of-crown-graph-matchings-are-determined-by--90543620c469, explicitly covers the per-matching formula, polynomial, recurrence, spectrum, and extrema under the same hypotheses with the same cycle-cover argument. It additionally describes optimum deletions via orders. This is an equivalent-coverage decision, not a determination of priority; its later catalogue date neither proves who first derived the formula nor makes the records scientifically distinct. No distinct surviving result is exposed by the frozen package.

## value

PASS

The mathematical content is a natural complete classification, tying the edge-deletion cost of each matching to its cycle structure and exposing the exact spectrum and frequencies rather than one extremum. That scientific utility does not create a distinct contribution beyond the demonstrated catalogue overlap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
