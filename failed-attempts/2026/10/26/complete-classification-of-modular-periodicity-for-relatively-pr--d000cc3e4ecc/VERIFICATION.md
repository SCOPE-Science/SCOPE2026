---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For nonempty subsets the divisor Möbius test of the joint gcd yields Σ μ(d)(2^(n/d)−1); the constants cancel only for n>1. Parity is immediate for n>1, and mod 3 the sum is zero on odd n≥3 and on 4|n; for n=2w, w>1 odd, the odd and even squarefree divisors pair to give 2Σ_{e|w}μ(e)=0. For odd m≥5 the order d of 2 is >2, so a prime p≡−1 mod d (chosen >B) has Φ(p)≡2^(-1)−2≠0 mod m. A different prime q≡1 mod lcm(T,d) makes Φ(pq)≡0 and pq≡p mod T. Dirichlet supplies arbitrarily large primes in these reduced classes. For 4|m choose p>B odd, p≡1 mod T, and Φ(p),Φ(p²) are respectively 2 and 0 mod 4, sufficient to distinguish them modulo m. Every other nondivisor of 6 has odd part ≥5. An eventual period would force equal residues at any two indices above its threshold in the same T-class. Thus the theorem is true as stated.

## originality

FAIL

The full Ayad–Kihel paper was recovered. Despite Theorem 3 being worded for f(n), its proof explicitly rules out eventual periodicity of Φ itself for every prime ℓ≥5, using the same prime/semiprime witnesses above any threshold. Lemma 2 gives the positive mod-3 case. The extension to every odd m≥5 is a mechanical change to the same argument (Euler's totient of m or ord_m(2) in place of ℓ−1; 2^(-1)−2=−3/2 mod m). The mod-4 case is an immediate Möbius/square-divisibility check. The exact all-moduli wording is not stated in the earlier paper; the lack of an independent mathematical remainder, not a missing publication or an exact-match assumption, determines the verdict.

## value

FAIL

Classifying eventual periods is a natural task and the original prime obstruction is worthwhile. Once the directly matching 2009 prime proof is credited, the extension is a parameter substitution for odd moduli; the extra square obstruction is the immediate mod-4 reduction to μ(n). Separating out 9 or 4 would not provide an independently valuable result beyond those deductions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
