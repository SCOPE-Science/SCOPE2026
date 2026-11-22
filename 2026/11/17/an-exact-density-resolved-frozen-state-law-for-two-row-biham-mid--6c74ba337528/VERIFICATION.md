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

PASS. Frozen claim covers exactly the labelled 2×n periodic east-then-north Biham–Middleton–Levine rule for n≥3. If an east car moves, no subsequent north update can restore its former east occupancy; hence full-update fixedness forces no east move and, next, no north move. Two-row north obstruction excludes exactly (N,0),(0,N) from the nine vertical pairs, leaving seven columns. The edge constraint forbids an empty successor row after E; the weighted 7×7 transfer trace counts each cyclic labelled configuration once, with weight u per east car and v per north car. Independently constructed the seven-by-seven SymPy matrix from this predicate, computed det(I-zT), and verified exact symbolic identity with (1-uz)[1-(1+u+u²+2uv+v²)z+(u+u²+u³+2uv−uv²)z²−u³z³]. Independent traces yield physical n=3..7 totals 148,777,4097,21620,114107. The unweighted characteristic polynomial x³(x−1)(x³−6x²+4x−1) gives isolated λ in (5.278039,5.278040); smaller other-root moduli prove dominant growth. Inclusion–exclusion of east-only (4), north-only (2^n), and fully occupied (4^n), with three singleton intersections, proves mixed-vacancy J_n−4^n−2^n−1. Analytic perturbation of the dominant simple root at u=v=e^s gives occupied fraction and variance O(n), hence vacancy concentration at approximately 0.152713299756. Direct original verify/transfer.py and verify/brute.cpp source were read; the independent algebra, not only captured logs, checks the certificate. n=1,2 coefficients are formal transfer, and uniform sampling among fixed states is not a random-initial-condition dynamical statement.

## originality

PASS

PASS at best-of-knowledge priority only. Classical BML papers concern phase transitions, jamming and large square/nonslim strips; this exact two-row all-circumference joint fixed-point polynomial, cubic entropy and vacancy law are not directly implied. A published three-row counterpart uses 18 columns and a product of quartics rather than a general width theorem subsuming two rows. The two-row computation and density resolved fixed ensemble are genuine distinct statements; an unindexed specialized strip table remains a priority risk. No historical uniqueness certificate is claimed.

## value

PASS

PASS. A width-two fully periodic exclusion automaton has a natural nontrivial exact fixed-state population by two conserved species, not a renamed textbook recurrence. The seven-state transfer produces an interpretable entropy and an exact vacancy fraction in the stationary ensemble, distinguishing jammed configuration counts from attraction probabilities. The exact bivariate polynomial is a reusable baseline for finite-width traffic and obstruction models; classification is exhaustive for the stated natural width and all n≥3. Scope does not include wider tori or global phase transitions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
