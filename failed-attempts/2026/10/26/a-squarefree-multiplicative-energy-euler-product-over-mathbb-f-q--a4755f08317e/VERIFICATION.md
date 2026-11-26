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

The six allowed prime-occurrence patterns give a unique five-factor decomposition, not a quotient by swaps. Equal degrees force deg A=deg D=u, deg B=deg C=v, and deg G+u+v=n. For fixed G, reduction modulo the product of finitely many prime squares is exactly uniform for all sufficiently large u,v. Above a cutoff containing the primes of G, failure requires a square in one of four factors or a shared prime in one of six pairs. Each event is bounded by |P|^-2 uniformly, including when a divisibility condition is impossible by degree. The summable tail proves the stated interior limit. At most 2M boundary pairs are lost for min(u,v)<M, and the weights q^(-2 deg G) have total at most (1-1/q)^-1, proving the Cesàro and dominated limits in the necessary order. The G sum inserts z²/(1+4z) locally; z=|P|^-1. All factors are positive, and log factors are O(z²). Exactly q linear primes yield -9/q, with O(q^-2) from all remainders. As a finite cross-check independent of the supplied script, rejecting quadratics T²+bT+c with b²-4c=0 mod 3 leaves six; multiplying all 36 ordered pairs modulo 3 and summing squared product multiplicities gives E_sf(3,2)=66. The infinite result does not rest on enumeration.

## originality

FAIL

A distinct same-date Resultary record states the same fixed-field energy with the identical Euler product and the stronger remainder O_q(q^{2n}); it also contains the claimed large-field expansion. This is statement-level coverage, not evidence of which result was first. The alternative five-factor/CRT proof is not a distinct energy theorem.

## value

FAIL

The squarefree collision factor is a natural invariant. The frozen contribution, however, supplies no new count, range or bound beyond the matched record and is quantitatively weaker. Its elementary alternative proof is a useful exposition, not a demonstrated additional scientific result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
