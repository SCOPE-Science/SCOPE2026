---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Odd DNA length forbids self reverse-complementary words; 640 eligible words split into 320 orbits; discarding internally conflicting strands leaves 260 orbit vertices. Independent reconstruction yields 4,948 conflicting pair edges. Four exhaustive binary branch leaves have 147 rational clique duals, nonnegative weights, coverage >=1 at every remaining vertex, and strict bounds 36880/1623, 436/19, 47255/2068, 597/26 (<23); the fully verified 22-pair example covers 166 distinct four-base deletions without collision. Exact BigInt rational verification reconstructed all 147 cliques, all remaining sets and the matching witness rather than relying on a verifier exit string.

## originality

PASS

D’yachkov 2014 and Bennenni–Guenda–Gulliver 2015 study reverse-complement and GC-constrained edit/DNA codes, but no located result proves this same two-layer GC, reversal-closed, one-deletion-only n=5 optimum. Jing Sun 2009 thesis explicitly claims short-parameter code tables and remains a real unresolved historical risk; full correct thesis source could not be fetched (public PDF redirects returned unrelated theses), and authorized Oxford returned vpn_disconnected. Best-of-knowledge PASS is qualified, not a statement that the thesis has been fully excluded.

## value

PASS

A complete exact finite capacity is a meaningful natural coding benchmark at the smallest odd length with close-to-half GC and full strand-pair closure; the exact numerical optimum is not a generic sphere-bound substitution. This remains valuable despite being finite and despite lack of a general family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
