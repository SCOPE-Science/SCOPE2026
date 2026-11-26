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

For m>=2 and full-support U on nonempty L, the displayed greedy factorization starts with two UaUb arches, then bUa and UbUa, followed by UbbUa and UbUa pairs as needed; the remainder UbbZ contains all non-a letters and no a. One letter per arch embeds every length-2m word. The 2m copies of a exclude a^(2m+1). Before the second a the prefix is UaUbU and the only missing pairs are aa,ba,bb. Before the jth a for j>=3 (or in the whole word at j=2m+1), there are j-1 complete arches followed by a piece containing all non-a symbols. Thus a missing length-j word must end in a, and matching at the last available a is equivalent to embedding its prefix before that a. Induction gives exactly the stated three words; only the specified fixed alphabet and tails in (L union {b})* are used. For d>=3 the ordinary ruler recursion until the first b gives W_(d-1)=UaUb and phi(U)0=UaU. The exceptional b image gives W_d=RRb and W_(d+1)=(RRb)^2 0bb. For R the only a cannot be paired with itself and the only b is terminal. For RRb all pairs embed, terminal b can follow any pair, final a gives the three missing initial pairs above, and before the last occurrence of each L-letter only bb fails among the pairs. This gives the two d+1 counts at lengths 2 and 3 and the stable three-word case at length 5. Independent direct enumeration on 82 bounded hosts agreed with the stable theorem; the all-parameter proof does not rely on this finite test. The supplied checker and recorded output were inspected, not executed. No claim for all subsequent morphic iterates is established.

## originality

PASS

Credit the exact substitution to Dvořáková–Mol–Pelantová and the general structural characterization of shortest absent subsequences to Kosche et al. The supported distinct result is the explicit stable three-word classification uniform in full-support U, m and the allowed tail, and its three-level transition for this particular morphism. Neither a new general SAS characterization nor historical priority is claimed. The strongest prior characterization indeed applies, but does not give the family-specific prefix and morphism identities that resolve all its constraints uniformly.

## value

PASS

Shortest forbidden scattered words directly measure where universality breaks, and the substitution is independently motivated by rich-word structure. The exact boundary and complete languages distinguish that family from other substitutions, without merely reporting three finite runs. The uniform extension explains why arbitrary internal multiplicity/order and a-free tails from the specified alphabet do not perturb the three obstructions; the length and count alone would miss this structural information. The claim remains limited to the three morphic levels and the stated block class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
