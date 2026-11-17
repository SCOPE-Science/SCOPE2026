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

PASS: Prime-adic quotient excess equals ∑_{1≤r≤h_p}1[n mod p^r < k mod p^r]. All terms nonnegative, so equality iff lower base-p digits dominate. CRT gives the product density; changing the highest constrained nonzero digit establishes sharp local period p^e_p, hence least global period. Prime number theorem gives density upper bound. Independent exact lcm-vs-binomial checks covered 3726 integer pairs. Farhi’s complete primary Theorem3 speaks to quotient, not support indicator.

## originality

PASS

PASS best of knowledge: precise all-prime truncated digit criterion and sharp least period of the equality indicator answer Farhi’s explicitly posed equality-locus problem; earlier quotient periods are different functions.

## value

PASS

PASS: Answers Farhi’s natural integer equality-locus classification and determines the sharp least Boolean-support period and exact density for each column; the latter is not synonymous with the known full quotient’s periodicity. A natural arithmetic invariant with a global exact test and quantified rarity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
