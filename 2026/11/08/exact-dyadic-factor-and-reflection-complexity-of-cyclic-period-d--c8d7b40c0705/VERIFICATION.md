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

The window of 2^k positive indices contains exactly one multiple of 2^k, yielding templates T_{j,c} for all j,c; powers 2^e realize each c. For different center indices with v2(distance)<=k-2, a residue-class witness changes valuations t versus t+1 modulo m>=2. Only centers separated by 2^(k-1) collide, precisely for both labels c=k-1 mod m. There are m2^k-2^(k-1) factors. Reflection through a larger power of two proves reversal-closure at all lengths. Every length-2^k palindrome for k>=2 would force both offset parity classes to be zero, contradicted by a valuation-1 position; at length2 exactly 00. Independent all-template comparisons for m=2..6,k=1..7 agreed, not an infinite proof.

## originality

PASS

The new result is exact all-m>=3 dyadic collision classification, not the binary m=2 reflection formula or palindromic factors. Allouche et al. show binary evaluation/general automatic complexity regularity, which cannot immediately imply the precise template collisions for arbitrary modulus; Bognini/Ammar analyze kernel factors and gaps. The structural explicit formula is not a title substitution, but an unindexed broader generalized-complexity result remains possible.

## value

PASS

Factor complexity and reversal orbits are basic structural invariants of morphic/automatic words; the all-alphabet dyadic exact factor enumeration with a classified exceptional collision mechanism gives a potentially reusable sharp description, beyond known binary special cases. It is naturally motivated rather than an arbitrary finite sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
