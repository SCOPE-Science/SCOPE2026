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

From conditioning on the uniformly selected currently feasible edge derive P_G(z)=z/|E(G)| sum_{uv} P_{G-{u,v}}(z), with P_edgeless=1. Independently implemented subset-memoized exact Fraction recursion and enumerated every NetworkX nonisomorphic_tree at each n=1..13 (2288 total, including 1301 at 13). After removing zero factors all coefficient support widths were <=3; exact quadratic/cubic discriminants give zero nonreal types through 12 and exactly six at 13, matching six graph6 encodings. The symmetric 13-vertex triple-fork witness has law z^3(180+1852z+5149z²+4339z³)/11520 and discriminant -12323232144. This verifies a truly exhaustive FINITE cutoff, not any claim for >13 vertices. The pinned verify_greedy_matching_roots.py was separately read and its 12! edge-order DP reasoned through; it provides a different representation of the same feasible-edge process.

## originality

PASS

Heilmann–Lieb ordinary matching-polynomial real-rootedness and uniform maximal-matching enumerators are different measures. Semantic Resultary search finds no earlier exact 13-vertex terminal feasible-edge greedy distribution root census. Original Dyer–Frieze 1991 studies the identical algorithm and trees; its complete primary text remained inaccessible after arXiv/OA search and authorized institutional request reported VPN disconnected, so a residual priority risk remains rather than a spurious NOT_COVERING claim. Best-of-knowledge PASS.

## value

PASS

The sharp first loss of real-rootedness of a natural stochastic matching size law distinguishes random greedy output distributions from the classical matching enumerator. Six complete minimal tree types and an exact rational witness provide a meaningful structural finite obstruction despite strict log-concavity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
