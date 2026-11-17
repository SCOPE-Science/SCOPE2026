---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The submitted RESULT.md proof is sound for all distinct primes p,q and every n>0. If D²(n)=n, N=qν_p(n)+pν_q(n) and N' satisfy NN'=(pq)². Unique factorization gives the nine pairs N=p^u q^v, N'=p^(2-u)q^(2-v), 0≤u,v≤2. The valuation update enforces N'-N=(u-1)q+(v-1)p. Six sign/size contradictions, two cross-exponent contradictions and the forbidden N=1/N'=1 leave only (u,v)=(1,1), so D(n)=n. Solving qa+pb=pq gives p^p m or q^q m with gcd(m,pq)=1. Independent integer iteration checked 100000 (prime pair,n) cases; this is corroboration, not the universal proof. The finite test and actual verify.py were separately examined.

## originality

FAIL

Earlier unrestricted all-period theorems for the identical two-prime map already show every positive periodic point is fixed, exactly including all D² solutions and both fixed families. Submitted proof has no surviving distinct theorem or boundary.

## value

PASS

Excluding primitive two-cycles and determining exact periodic points are natural dynamical questions raised by generalized arithmetic subderivatives, and their unrestricted exclusion would be useful. Scientific value of the theorem as a fact is real, but it is entirely pre-established; correctness/value cannot rescue originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
