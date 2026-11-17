---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: Full proof checks fixed-point constraints of the stable sorting permutation at content (m,m,1), eliminating starts in 0, final 2 and 1 between last non-1 letters. Removing the unique 2 leaves a binary word with at most one equal pair, forcing exactly A_m=(10)^(m-1)120 or B_m=(10)^(m-2)10201. Direct agreement counts yield A_m distance m+1 only for even m, B_m never sharp. Under conjugation by i↦i+1, the A_m sorting permutation is multiplication by a=(m+1)=2^(-1) mod p with a single splice through zero; one cycle iff p=2m+1 is prime and 2 primitive. The prime-root condition does not assume infinitely many such primes. Independent complete enumeration m=2..8 reproduces exactly two fixed-point-free candidates and sharp counts (m=2,6 only); finite checks are not the all-m proof.

## originality

PASS

PASS: Survives statement-level primary-literature and published-finding comparisons, subject to recorded residual risks. Previously established sufficiency does not imply this all-m necessity or uniqueness. The nonstandard candidate enumeration and cycle-splicing reverse implication survive. Historical terminology risk persists because the closest original 2026 paper could not be read fully in this execution.

## value

PASS

PASS: A natural fixed-Parikh-vector slice of an explicitly posed BWT sharp-run problem receives a complete infinite-family 0/1 existence, nonexistence and uniqueness criterion. The all-m fixed-point-free two-word rigidity and necessary arithmetic obstruction go beyond a previously known sufficient word or a finite length census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
