---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The lower bound is rigorous: any long accepting run yields a shortest repeated-state interval which is a simple directed cycle, hence its pump length is a multiple of p, and its bipartite length even. The bound lcm(p,2) follows; the directed even cycle attains it, also at p=1,m=2. Unrestricted p-cycle and pump lower bound give p. Independently checked explicit periodic cycle construction for p=1..20; universal proof is analytical.

## originality

PASS

No exact prior formula located in searched Resultary or accessible primary abstracts. However this is an elementary corollary of the standard pumping argument plus even-cycle parity; a future discovery of that lower bound under a different term is a genuine risk.

## value

FAIL

Although the exact singleton-residue boundary of the recent bipartite-cactus representation theorem is natural, its entire proof and construction are an immediate textbook one-cycle pumping/parity exercise; the cactus restriction contributes no additional mathematical obstacle. It supplies no new structural lemma beyond routine cycle divisibility. Under the substantive-value test, a repackaged elementary baseline alone is insufficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
