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

A selected-edge subgraph contains no triangle or three-edge path, since the remaining/middle edge would witness a conflict. An extra edge between endpoints of chosen edges would itself witness a conflict, so the endpoint-induced graph is exactly the selected star forest. One distinct leaf per edge is independent. Its size is at most n, with equality only for the two alternating independent transversals in even prisms. At equality every center is in the complementary bipartition and has all three neighbors among the chosen leaves, so inducedness forces every center to carry all three edges. Cover of each leaf exactly once gives x_(i−1)+x_i+x_(i+1)=1, hence a period-three center pattern, one phase per residue modulo three. Either leaf orientation and any phase constructs a distinct optimum when 6 divides n. The listed small cyclic masks realize the lower bounds. For n≥5 any two conflicting anchor columns lie within two steps, and the conflict test on triples is uniform because the anchored edge endpoints span at most four consecutive columns, with no seam adjacency outside that span. Thus gluing at the common pair (0,2) preserves admissibility and adds sizes, giving all n via n=6q+r and the base cases 3–5. The uploaded verifier was inspected, not run. Independently, /workspace/branches/bf01f41f-0746-4f64-b04e-6562024330db/independent_replay.py used direct enumeration for n=3–6 and a cyclic conflict transfer for n=7–48; replay_small.txt and replay_11_48.txt report matching values and six induced-star configurations at n=6. Those bounded checks corroborate but do not prove the infinite theorem.

## originality

FAIL

Concrete equivalent coverage was found. The 2026-10-13 Resultary record proves the same invariant for all n≥3 and exactly the same six labelled edge sets in the divisible case. The distinct same-date record also gives the n≥7 formula and a broader count; its date is not used to infer priority. This is a coverage decision, not a conclusion of false mathematics or an inference from missing evidence.

## value

FAIL

Exact prism optima and equality structure would be useful were they unknown, but both are already established on precisely this graph family. The frozen proof offers another elementary verification and bounded corroboration; it does not identify a materially new structural consequence, scope, or reusable method beyond those known conclusions. No genuine distinct remainder of the submitted finding warrants a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
