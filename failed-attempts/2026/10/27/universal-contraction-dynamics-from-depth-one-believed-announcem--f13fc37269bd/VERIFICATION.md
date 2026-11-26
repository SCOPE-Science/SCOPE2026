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

Target restriction leaves R'=T×(S∩truth(φ)), so the family is closed and each support (also the empty one) is reachable by a factual selector of its types. With τ_t the type minterm, ◇τ_u tests u∈S uniformly at all worlds. Exact support tests and τ_t therefore realize every truth bit (t,S) with t∈S by one depth-at-most-one formula; all other bits are discarded by the update. There are m·2^(m−1) such bits. In the positive fragment, adding accessible types can only increase truth at fixed t, and each monotone survivor function on the other m−1 types is written using its minimal true supports and positive diamonds. This gives independent Dedekind factors, including constants. Factual announcements give intersections with a fixed subset and are idempotent. The explicit positive witness retains a type iff some strictly lower type is present, dropping precisely the least surviving type each time until empty, including for m=2. Thus both strict inclusions, the numerical examples, and the m-step bound and attainment hold under the arrow restriction semantics, not ordinary world deletion. I inspected the finite checker without running it; the symbolic argument supplies the full quantifiers.

## originality

FAIL

The closest height-two free-algebra result covers more than the coincident count. Its exact depth-one pointed types are the same pairs (t,S) with t∈S, and its Step 3 proves that every Boolean truth table on those pairs is realizable. Those are exactly the bits an announcement can retain, so the unrestricted representation and its count are a direct translation. The positive formula/count are the standard monotone-DNF restriction and independent product on those same coordinates, not a separate nonmechanical representation. The sharp positive iteration has separate exact corpus coverage. The verdict concerns mathematical coverage and routine implications, not author or disclosure priority.

## value

PASS

As a classification, the result is useful: it describes exactly which dynamics a single announcement can encode across simultaneously reachable states, separates the monotone syntactic fragment, and gives a tight positive-fragment lifetime. This judgment credits the content of a natural classification, not a new contribution from rephrasing the already characterized type tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
