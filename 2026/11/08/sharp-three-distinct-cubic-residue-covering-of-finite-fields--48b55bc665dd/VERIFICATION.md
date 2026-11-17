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

For q ≡1 mod3, the nonzero cubic subgroup H has size h=(q-1)/3. By order-three multiplicative-character decomposition each nontrivial additive Fourier coefficient has magnitude at most B=(1+2sqrt(q))/3; additive orthogonality bounds unrestricted ordered T_b below by (h³-(q-1)B³)/q. Three collision events each contain at most h triples, hence R_b≥T_b-3h. The resulting numerator factor t(t³-8t²-41t-6), t=sqrt(q), is positive for t≥13: cubic at13 is306 and its derivative is increasing and positive. This proves every target for all q≥169. For all 24 smaller eligible prime powers the inspected verifier explicitly constructs finite fields, checks nonzero inverses and enumerates all unordered distinct triples (131116 total). An independent implementation reproduced q37 and q43 contrast plus coverage at primes 49? (49 is extension): separately checked F25, F49, F64, F121 with explicit extension fields; verified q37 full, q43 missing zero, and all sampled eligible prime fields through163 covered. Finite exhaustiveness comes from inspected source code enumeration, not extrapolation.

## originality

PASS

Zhu–Wan (2011) studies arbitrary k-element subgroup subset sums asymptotically. Available abstract establishes a broader topic but does not imply the exact index-three k=3 all-target boundary; its complete arXiv manuscript was inaccessible and institutional retrieval reported disconnected VPN, so this remains a material priority risk. Ge–Li–Wang (2022) computes cubic diagonal equation solution counts for prime fields, plausibly covering zero-target subcases, but that alone does not cover distinct-summand all-target prime powers or the 37/43 cutoff. Separate Resultary searches found cubic-graph and consecutive-residue problems, not this subgroup restricted sumset. Originality is best-of-knowledge with exact source limitations stated.

## value

PASS

A natural restricted Waring/subset-sum question for the index-three multiplicative subgroup has a surprising exceptional full-cover field q=37, obstruction at q=43, and sharp eventual threshold 49 uniformly over prime powers. Distinct-element and every-target quantifiers make the exact cutoff a useful finite-field additive-combinatorics fact, rather than a routine Gauss bound alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
