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

With simultaneous independent recipient-side updates on K_(a,2), seed in the 2-vertex side, freeze the other hub and assign iid Geom(1/2) clocks to large-side vertices. Conditional hub survival through t rounds is product_{s=0}^{t-1} W_s/a; an equality-pattern set partition yields the stated exact finite-a formula. LLN and dominated convergence give P(G>t)=2^{-t(t-1)/2}; uniform tail bound P(G_a>t)<=2^{-(t-1)} proves mean convergence. Once both hubs blue, all remaining large vertices fill next round with probability approaching 1, giving Tsmall=>1+G and E→3.64163256.... Opposite large-side start waits Geom(2/a-1/a²) for any hub, followed by O(log a) expected completion; hence Tlarge/a=>Exp(2), E/a→1/2 with stated sandwich bound. Independent exact transition checks for 70 finite-state steps and P(G_a>3)=(a+1)/(8a) corroborate, do not prove, limits.

## originality

PASS

Lichtenberg’s 2025 Rice thesis primary full PDF became accessible during this independent review: its Section 3.6 provides numerical K_(a,b) expectations and Conjecture 3.6.1 on seed preference, but not either exact distributional limit. The 2026 Geneson paper supplies broad O-bound and preference conjecture; a separate same-model Resultary published theorem proves the sharper all-finite-a mean preference and a/2+O(log a) gap, so neither mean preference nor its leading gap is original here. The surviving original contribution is the exact small-origin q-series law, Exp(2) large-origin law and finite-a set-partition survival identity.

## value

PASS

On a natural two-hub complete bipartite network this rigorously separates a constant-order nongeometric q-series completion law from a linearly growing Exp(2) law according to the seed side, providing the full distributions behind previously known mean-side preference. The exact finite-a set-partition first-activation law supplies useful detailed hitting-time data absent from mean recurrences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
