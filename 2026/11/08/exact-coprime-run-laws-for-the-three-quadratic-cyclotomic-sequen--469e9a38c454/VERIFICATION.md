---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Polynomial resultants for Phi3 at separations 1..4 restrict common primes to 7 at h=2, 3 at h=3 and 19 at h=4; exact modular roots determine all five-window edges. Phi4 separations 1,2 yield primes 5,2 and Phi6(x)=Phi3(x−1). Every six Phi3 indices contain two ≡1 mod3 and every four Phi4 indices two odd, giving strict universal cutoffs. CRT count of allowable maximal windows and graph-edge generating polynomials gives the claimed 399- and 10-period histograms; proper nonempty residue classes at every prime factor force least periods. Independently enumerated every starting residue of periods 399 and 10, all gcd edges and run lengths, including Phi6 n=1 boundary; matches exactly. Finite checks corroborate the resultant/CRT proof, not substitute for it.

## originality

PASS

An October 18 prior theorem provides a complete single-shift pair-gcd formula for Phi3 at every shift, and therefore covers the individual Phi3 edge congruences. The submitted Phi3 399-period run and multi-edge distribution can be obtained by combining that prior pair formula over shifts 1..4 and applying CRT; this is substantial logically antecedent coverage and is not represented as a new local-gcd mechanism. However the earlier theorem only covers same-step gcds and individual distributions for Phi3, not the stated joint window/run classification of the complete three degree-two cyclotomic family; Phi4 has separate parity-and-mod5 behavior and Phi6 translates Phi3. The significance is the unified exact full-family run/graph invariant rather than its elementary prime checks. Risk: a reader may view the run histograms as routine corollaries of the earlier general formula, weakening novelty.

## value

PASS

The family of all monic quadratic cyclotomic sequences is a natural, exhaustively defined arithmetic class. Exact maximal pairwise-coprime blocks, least periods and full common-divisor graph distribution give global sequence invariants rather than isolated gcd counts; completeness across Phi3,4,6 and sharp cutoffs are mathematically useful. Nevertheless the combinatorial CRT evaluation is short and some Phi3 content mechanically follows the earlier all-shift gcd theorem; assessed as a modest, motivated classification rather than a broad new gcd theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
