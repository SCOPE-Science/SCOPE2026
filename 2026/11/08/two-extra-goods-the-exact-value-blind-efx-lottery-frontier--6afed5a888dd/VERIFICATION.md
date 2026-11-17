---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

C: Strict positivity forbids empty bundles in an EFX allocation with m=n+2, so only one triple or two double bundles are possible. Sorting four smallest goods a>=b>=c>=d, triple shape succeeds for the bottom triple if a>=b+c, and double shape with (a,d)|(b,c) succeeds if a<=b+c. Thus a uniform surjection always has at least n! successes among n![C(m,3)+3C(m,4)] allocations. Symmetrization of any value-independent lottery preserves/improves worst-case success; adversarial bottom values (10,4,3,1) and (6,4,3,1), all other values larger, force exclusively one triple or one double pairing, giving upper min(t/C(m,3),d0/[3C(m,4)])<=1/H. Independent exhaustive EFX allocation recomputation for n=2,m=4 reproduced exactly two winning labelled allocations in each adversarial case, one occupancy type each. Boundary n=2 and tie permissiveness follow from inequalities; infinite n uses the proof.

## originality

PASS

O: PASS best-of-knowledge. Neoh–Teh (2025) full available primary §3 Theorem 3.13 proves at least n! EFX allocations under identical valuation, but not the *value-blind minimax upper bound* or optimal mixed T/D lottery. Cohen–Teh–Wooldridge (2026) studies n+1 goods and more general value-aware/heterogeneous settings; its complete text was inaccessible, so implications remain a named risk, not a fabricated absence claim.

## value

PASS

V: PASS. A sharp probability frontier for valuation-independent online allocations at exactly two extra goods, including an implementable symmetric lottery and competing valuation regimes, is a motivated information-restriction boundary. Its exact 24/[(n+2)(n+1)n(3n+1)] law is not merely the previously known EFX existence/count lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
