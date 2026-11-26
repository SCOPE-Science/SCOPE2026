---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

A vertex of color a observes c_a−1 in its own bin and c_b in every other bin. One global maximizer attracts all vertices in one step (vertices of that color keep it, possibly at a tie); two maximizers swap their nonempty classes and leave smaller classes untouched; three or more maximizers leave every vertex with a tied local mode. The swap preserves the global occupancies, has primitive period two immediately, and attracts no transient. Choosing its unordered pair of named colors, their size m and their two labelled vertex sets leaves the remaining exponential multinomial coefficient with cap m−1; this gives B(n,q), including q=2, and B/2 cycles. For fixed j,r, under q≫n direct multinomial counting gives E[(X_j)_r] ∼ (n^j q^(1−j)/j!)^r. In a fixed k window this gives X_k⇒Poisson(λ_k), divergence and relative-variance concentration of X_{k−1} (also for k=2), and P(M≥k+1)≤binom(n,k+1)/q^k=o(1). The events J=2 and X_k=2 differ only if M>k or X_{k−1}≤2, proving the limit. Between critical exponents the analogous higher-load bound and diverging concentrated X_k imply vanishing oscillation probability; above 2 even a repeated color disappears with high probability. Differentiation gives the unique maximum at λ_k=2 and the stated c. Replay: frozen RESULT.md Proof (1)–(5). The bundled checker and finite output were inspected without execution and are not relied on for asymptotic conclusions. The result is for fixed k and uniform independent initialization, not growing k or α≤1.

## originality

PASS

The supported distinction is the exact dynamical identification and finite orbit census joined to the full sequence of sharp fixed-k windows for this specific deterministic incumbent-retaining clique rule. The occupancy factorial moments are standard and are not credited as a separate new probability theorem. The closest checked indexed result is a different graph with a different update reduction, and the closest clique protocol inspected uses random samples and random ties.

## value

PASS

An exact criterion and census for the persistence of disagreement give a useful benchmark for deterministic many-color dynamics: a whole sequence of critical power-law scales with the same optimized nonconsensus oscillation probability, separated by scales with vanishing oscillations. The work is useful as a combined classification and probabilistic limit, not as a general occupancy advance or a uniform-in-k phase diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
