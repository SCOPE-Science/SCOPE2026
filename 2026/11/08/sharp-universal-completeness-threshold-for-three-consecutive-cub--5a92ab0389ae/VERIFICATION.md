---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For each target color and nonzero argument the root-of-unity filter is exactly 3 or 0, and at zero it is 1. Removing starts 0,−1,−2 from the field sum subtracts at most 27 before division by 27. The 27-term expansion has constant term p; the six one-support terms vanish by character orthogonality; the twelve two-support and eight three-support terms are bounded by √p and 2√p respectively. In the last two cases the polynomial is not a cube because its distinct linear factors have exponents 1 or 2, so the distinct-root version of the Weil bound applies. The error phases all have modulus one, giving 27N≥p−28√p−27. For √p≥29 the lower bound is (√p−29)(√p+1)+2>0. Independently reran the entire finite interval by an Eratosthenes sieve and direct Euler-character values x^((p−1)/3), identifying the first nontrivial value with color 1. This reproduced the 70 eligible primes through 840, all 42 successes between 307 and 840, the full list of thirteen failing primes, and the last failure 283 with just (0,0,0) missing. It also confirmed (2,0,2) is absent at 151 and 163 while (0,0,0) occurs. The next eligible prime is 307. The proof is for eligible prime fields and ordinary starts 1,…,p−3, not a least integer lower bound or a claim for proper extensions. Replay: python3 /workspace/audit_evidence/05-cubic.py. The frozen dual-enumeration script and its recorded output were inspected, not executed.

## originality

PASS

The last failure 283 for the all-cube word is classical, as is the general character-sum method. The distinct statement is simultaneous occurrence of all 27 words already at every eligible prime beginning at 307, with 000 the sole omission at the preceding eligible prime. The decisive earlier results inspected concern one homogeneous word or a narrower subset of one word, not all mixed words. Priority remains qualified by the inaccessible 1983 full text.

## value

PASS

Simultaneous occurrence of all coset words on three consecutive nonzero positions is the natural mixed-color strengthening of the classical first triplet question. The finite threshold is meaningful because the lone classical obstruction could have been overtaken by a mixed-word obstruction; smaller primes show those conditions really differ. The proved all-word tail and complete finite interval resolve this sharp boundary rather than just listing examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
