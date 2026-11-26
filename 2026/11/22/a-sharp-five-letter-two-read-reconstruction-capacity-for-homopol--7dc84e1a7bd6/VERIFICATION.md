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

Edges mean two distinct common deletion outputs, not two positions or at least one common output. For two distinct words let i,j be the first and last differing indices. If deleted indices k<ℓ yield a common output then k≤i≤j≤ℓ and u_(t+1)=v_t across k≤t<ℓ. Agreement before i and after j gives constant endpoint segments permitting the deletions to be moved to i,j without changing the output. Reversing the order gives the other possible alignment; if i=j there is only one output. When i<j, two distinct outputs require both alignments, hence u_(t+2)=u_t and opposite alternating phases; the endpoint deletions conversely give two distinct strings. Legal flanks avoid both block symbols. Per symbol pair a flank has generating function C(z)=(1−z)/(1−(q−1)z); the unique interval gives the edge series binom(q,2) C(z)^2 z²/(1−z), including one edge per pair at n=2. Exact support is preserved because the union of the supports of two distinct one-deletion outputs equals the source support. Independent direct deletion-set construction verified all ten required support bases, their two-colorings/perfect matchings except for (n,s)=(5,3), and at n=5 the rows (vertices,edges,alpha)=(2,1,1),(42,57,19),(144,252,72),(120,240,60). For (5,3) the 19-word witness is independent, while the 12 edges and six 7-cycles cover each vertex by at least two doubled units with doubled cost 39. This yields the exact integral upper bound 19. There is exact coverage, since the doubled vertex incidence totals 84=2·42. Summing over supports gives half the ambient count for lengths 2–4 and a deficit of two per ternary support at length five. The directly checked induced 7-cycle extends by a legal common alternating prefix, preserving both distinct outputs per cycle edge; the binary graph always has just one edge. This gives the exact bipartiteness threshold without claiming capacity beyond length five. Replay: /workspace/review-evidence/5/independent_check.py, independent_small.log and independent_full.log; supplied scripts were read, not executed.

## originality

PASS

The unrestricted alternating-interval characterization and support separation are established, and the exact Kautz edge count follows directly from two closely related same-day proofs, not just from a differently named graph. The supported increment is the constrained length-five optimum with its exact defect per three-letter support, combined with the sharp first odd-cycle threshold. Neither the graph characterization/count nor the inspected unrestricted capacity certificates determine that optimum or threshold. The same-day records do not determine posting order.

## value

PASS

Every nonempty adjacent-unequal block of length at least two has a maximal initial alternating run. Opposite-phase replacement of that run is a fixed-point-free matching involution: if there is a following symbol it avoids both run letters. Thus half the ambient space is a natural upper bound, not a selected comparison. The theorem identifies exactly where it first fails for nonbinary alphabets, with a deficit supported entirely on ternary supports and certified by a genuine odd-cycle obstruction. This is an all-alphabet exact design benchmark at the first failure, not a claim about longer-length capacity or the minimum odd girth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
