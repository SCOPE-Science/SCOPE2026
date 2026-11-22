---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Write C=J−2B and expand by nonattacking negative-board rook placements: per C=Σ_j(-2)^j (n−j)!m_j(B). The cyclic row-and-column rotation of order 2^k acts freely on cells; any size-j placement stabilizer has power-of-two order h dividing j, so 2^(k−ν2(j)) divides m_j(B). Legendre ν2((n−j)!)=n−j−s2(n−j), together with s2(n−j)≤k−ν2(j), forces all j=1,...,n−1 terms divisible by 2^n, and j=n has 2^n already. ν2(n!)=n−1. Fourier diagonalization of displacement parity identifies multipliers with these permanents; a balanced unrestricted first-row sign yields a zero by cancellation.

## originality

PASS

Minc 1972 full text gives sparse structured circulant permanents but not arbitrary full-density sign circulants; Tao–Vu random Bernoulli nonvanishing is probabilistic rather than uniform over all signed circulants. The 2017 Sburlati paper specifically discusses congruences of circulants and is a material priority risk; OA/preprint searches failed, authorized Oxford download returned vpn_disconnected. Its inaccessible full text alone is not proof of coverage or automatic originality failure. In accessible evidence no stronger exact universal signed dyadic 2-adic valuation theorem was found.

## value

PASS

The permanent’s exact 2-adic valuation for all 2^n sign patterns at every dyadic order is a natural structural invariant, not an arbitrary finite slice. Orbit-stabilizer divisibility gives an infinite combinatorial explanation and a genuinely new contrast between cyclic-displacement and unrestricted matching Fourier operators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
