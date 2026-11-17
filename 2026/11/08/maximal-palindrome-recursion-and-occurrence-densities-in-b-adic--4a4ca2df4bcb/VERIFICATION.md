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

For integer b>=2 including composite b, y_b(bu)=1-y_b(u) and y_b(t)=0 when b does not divide t. Longest zero run has 2b-1 symbols and gives unique terminal maximal zero palindrome 0^(2b-2), with two starts per valuation-even center. Every palindrome containing a 1 has a reflection axis on the b-lattice, and language-maximality forces external multiple-of-b positions; it uniquely descends via the complemented 0^(b-1)-padded inflation map F_b. Conversely the lift preserves nonextendibility and shifts all starts by a factor b. Induction yields lengths (2b-1)b^k-1, exact position formula and density 2/[b^(k+1)(b+1)] via valuation parity frequencies. Independent factor and occurrence prefix checks passed for bases 2..7, n up to 80.

## originality

PASS

The b-adic valuation-parity binary fixed point of 0->0^(b-1)1,1->0^b is not the q-letter two-uniform generalized period-doubling word or the complementary Mephisto substitution; language-maximal nonextendibility is not palindromic prefix factorization or maximality of an individual occurrence. Schaeffer-Shallit Theorem 3(d) proves exactly the b=2 maximal-palindrome length set 3*2^k-1; this special case is already known and is explicitly not credited as new. Class-P palindromic morphism theory accounts for the existence of a general padded palindrome lift, but not the all-b maximal factor list and valuation-based exact start densities. A proof of base-two allowed lengths cannot imply the all-integer-base two-start valuation formula, especially for composite b. General palindrome-preserving substitution counts do not by themselves prove complete language-level nonextendibility and occurrence classification. Best-of-knowledge originality with disclosed residual risks; no search failure alone is treated as novelty proof.

## value

PASS

A full language-level classification of nonextendible palindromic factors, with explicit integer starting positions and asymptotic densities for every positional base, is a natural exact invariant of a well-studied automatic word family. The all-base occurrence distribution is stronger than the known binary length spectrum and may be reused in automatic-sequence palindrome statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
