---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-15.md",
      "INDEPENDENT_AUDIT_2026-11-15.json"
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

For odd primes p and n>=2, smooth normalization has exactly two Fp-rational off-affine places (one additional above u=0, one totally ramified at infinity). Over Fp, (u+1)v=B(u); the exceptional u=-1 fiber contributes p iff p|2n+1 and p=3 mod4. Over Fp², the linear map v->uv^p+v is invertible if N(u)!=1; norm-one fibers split by u^((p+1)/2)=±1 and their image condition gives N1=p+1+p delta epsilon and N2=p²+1+p(p-1)delta/2. The zeta coefficients follow via Newton identities. Independent Fp² arithmetic verified eight pairs, including both delta regimes; finite examples are not universal proof.

## originality

PASS

The exact curve and high-extension maximality, automorphism triviality, genus, and ramification are credited to Bartoli–Borges–Timpanella–Zini. The inspected primary paper does not state these first two prime-field point counts or zeta coefficients; maximality at p^(4n+2) does not uniquely determine early traces. The new claim is the two explicit low-degree counts.

## value

PASS

The early Frobenius traces and first zeta coefficients are canonical arithmetic invariants of a high-genus family otherwise studied for maximality far above its base field. Their congruence transition in p,n is a natural exact phenomenon and usable input to further zeta/Jacobian analysis, with no unproved full zeta claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
