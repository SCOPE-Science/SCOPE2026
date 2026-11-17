---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Kummer identifies V_t(n) as the number of carries adding fixed t to uniform p-adic n. Each finite carry count is a cylinder event with exact natural density. A digit d starts a carry with d/p; conditional continuation and termination give G_d(z)=(p-d)/p+d(p-1)z/(p²(1-z/p)). If fewer than g carries occur, chains cannot reach the next nonzero shift digit; disjoint digit blocks factor. At exactly g, only one chain can touch its immediately next active position, so the pairwise correction is d_i*d_(i+1)/p^(g+2) times all other zero-carry factors; this is strictly positive in the subtraction. Independently wrote a 2-state exact Fraction carry automaton, checking 192 odd-prime digit configurations for p=3,5,7, min gaps 1..4, 2-4 occupied positions and four amplitude patterns. All low coefficients and strict first corrections matched. The unbounded theorem is justified by the carry-block argument, not the finite computations.

## originality

PASS

Best-of-knowledge new odd-prime arbitrary-digit-amplitude sharp first-interaction coefficient; the known binary shielding result and classical Kummer/automata method are explicitly excluded from novelty.

## value

PASS

This is a natural sharp interaction onset: it quantitatively explains how separated nonzero base-p digits interact in p-adic binomial valuation densities and proves the first correction cannot vanish. Extending binary shielding to every odd p and arbitrary amplitudes is structural, not a mere parameter substitution, because the exact nonzero-digit thresholds and pair weights change.

The dated certificate retains the supplied scientific assessment, sources and limitations.
