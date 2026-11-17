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

PASS: Prime steps strictly add k and every composite step maps to a prime; no fixed points, no adjacent composite states, and every cycle contains a composite. Period two has (p,pm) with k=p(m−1) and P⁺(m)≤p; period three has one composite and p,p+k,p+2k, forces p|2k and p=2 by the primality obstruction, so k=2^a−1 with 2^a+1 prime (Fermat exponent). Period four has two composites alternating or one composite after three primes. The former gives distinct p,q, CRT k=tpq−p−q and necessary/sufficient two smooth multipliers; latter forces p=3, k=3^u−1, primality of 3^u+2 and 2·3^u+1. Each converse proves least period four. Independent bounded trajectory calculations confirmed observed short cycles for tested k; they do not establish global completeness.

## originality

PASS

PASS qualified: Das introduced the exact shifted-largest-prime-factor system and proved global eventual periodicity and bounds, but inspected original discussion and published Resultary prime-locator bound do not classify all primitive cycles of length ≤4 at every shift. New exact smoothness/Fermat arithmetic types are a distinct full natural low-period classification. Unindexed special-period tables could exist.

## value

PASS

PASS: A necessary-and-sufficient classification of all shortest primitive orbits for a named natural prime iteration answers a specific source dynamical classification problem, revealing Fermat-prime and simultaneous power-of-three primality phenomena without asserting infinitude. All k≥1 quantified, no arbitrary cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
