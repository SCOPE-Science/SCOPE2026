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

For odd x the valuations of x−1 and x+1 have one equal to 1 (with an infinite valuation allowed at zero). This gives exactly x=±1 mod 2^(a−1) for involutions, and exactly x=±1+2^(a−2) mod 2^(a−1) for x^2=1+2^(a−1) mod 2^a. The full involution subgroup has four elements; for a>=4 one of the two representatives 2^(a−1)±1 is divisible by 3 and larger than 3. A noncyclic abelian 2-subgroup would contain the full involution subgroup, so is impossible. The other two involutions are not squares modulo 4, hence the four displayed square roots of 1+2^(a−1) exhaust order four and split into the two stated cyclic groups. The plus group is excluded: a even makes its involution composite, while a odd makes 2^(a−2)+1 composite. The surviving group has both order-four representatives congruent to −1 mod 8 when a>=5, so it cannot be inside an order-eight subgroup, whose order-four generators are odd squares. At a=4 ambient exponent is 4. This leaves exactly the claimed order-two primality tests and one conditional order-four group, with disjoint contributions to the count; direct inspection gives the a=1,2,3 lists and trial division confirms the two displayed examples. RESULT.md line 51 has the factor phrasing reversed: if a−1 has an odd factor u>1, 2^((a−1)/u)+1 is a proper divisor of 2^(a−1)+1, not the other way around. Line 55 should say order one, not order zero. These do not affect the finding or the independent proof. The deposited finite generator was inspected, not executed; its bounded corroboration is not necessary to the all-exponents argument.

## originality

PASS

Li already uses precisely the standard-positive-prime representative condition and explicitly gives the small modulus-eight examples. Credit those and the classical structure of dyadic units. The new claim is the all-subgroups cutoff and exact surviving order-four criterion uniformly for a>=4; neither the general interval restriction nor the results for complete and compact groups supply those conclusions. Polynomial analogues compare at the methodological level, not as equivalent arithmetic classifications.

## value

PASS

The dyadic family is a natural infinite class of noncyclic ambient unit groups in Li's framework. Reducing all subgroups to three involution tests and one sharp conditional order-four candidate is more informative than checking a few moduli or identifying complete groups. It shows arithmetic restrictions that the ambient decomposition cannot, without turning the exact criterion into a conjecture about the frequency of its prime triples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
