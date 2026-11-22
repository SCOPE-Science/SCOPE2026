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

Every Condorcet-winner event is a disjoint codimension-(n-1) Boolean face. Inclusion-exclusion is exactly 1 minus the sum of the n face indicators, so nonzero Walsh sums vanish except on incident-edge stars; singleton frequencies cancel between the two endpoint faces. At each nonzero allowed frequency the magnitude is B=2^(E-n+1), while the zero multiplier is B*(2^(n-1)-n). For any projection to this character span, translation averaging preserves its range and cannot increase endpoint norm, and the unique translation-invariant projection is Fourier multiplication by 1_Omega, proving global (not just convolution) minimality. Fourier inversion gives kernel numerator 2^(n-1)H(G)+4e(G)-n²+1. Independent complete Walsh computations for orders 3,4,5 give rank 4,17,56 and exact norms 1,101/32,355/64. The n->infinity constant follows after separating the rare isolate contribution (uniformly O(n^3 2^-n)) and applying a binomial central limit theorem with uniform integrability to 4e(G)-n²+1.

## originality

PASS

Best-of-knowledge PASS for the exact all-order endpoint Fourier projection constant and evaluated asymptotic. Tournament voting methods study Condorcet selection mechanisms; score sequences and regular-tournament Walsh results involve different sets. Classical idempotent-averaging projection minimality is explicitly a known method, not the new assertion. No inspected source supplied the particular graph isolate/edge formula or the limiting constant, but specialized character sums may exist.

## value

PASS

The range-projection constant is a natural sharp stability/amplification invariant of a structured Boolean convolution, optimized over *all* projections and with a derived asymptotic constant. Its exact dependence on graph isolates and edges is a useful structural bridge from Fourier analysis to random graphs, not merely another count of winner-free tournaments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
