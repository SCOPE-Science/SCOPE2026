---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Reconstructing from the two Stern pair digit maps (a,b)→(a,a+b) and (a+b,b) gives adjacent coprimality and the two flanking values a+k(a+b), b+k(a+b) for n+1=2^k(2u+1); this works also at k=0 and at n=0. Their difference and coprimality give gcd(2k+1,a−b). Reznick's Theorem 4.7 concerns arbitrary initial intervals and each fixed modulus d≥2, including composite moduli; d=1 is trivial. Primitive diagonal pairs modulo p^a number p^a−p^(a−1) of p^(2a)−p^(2a−2), so CRT yields the claimed q_d. The allowed run lengths start at (d−1)/2 and have step d; their geometric weights give the stated closed factor. The proportion with k≥K is at most 2^(−K) in every interval [0,N), by counting multiples of 2^K in [1,N]. This permits both conditioning and tightness; exact value h on each fixed k is a finite congruence condition. For inversion one may first use finite divisor inversion within each run stratum and then sum over strata: the absolute majorant ∑(2k+1)2^(−k−1) is finite. The stratum k=(h−1)/2 contributes strictly positive mass for each odd h. Independent bit-map replay confirms the identity on 65,536 indices and exact rational evaluations at d=3,5,7; an independent conditional mixture agrees with the Möbius series, which yields 0.89734042214605 with absolute truncation error at most 2^−49.

## originality

FAIL

The October 13 indexed two-step Stern law already determines the complete exact-value distribution with positive odd support, and gives the stronger conditional divisor law at every fixed trailing-run stratum. Its prime-power tails and stratum weights give the frozen divisor formula by a geometric sum; standard Möbius inversion gives the alternate exact-value expression. These are statements about the same sequence and lag, not just similar Stern statistics.

## value

FAIL

The first nontrivial lag is well motivated and the full distribution would be useful as a new result. The existing stronger law already answers that question, and its conditional tails give the closed divisibility formula by a single geometric summation. The alternative standard inversion and numerical example do not establish a separate worthwhile unknown invariant. No surviving valuable claim warrants repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
