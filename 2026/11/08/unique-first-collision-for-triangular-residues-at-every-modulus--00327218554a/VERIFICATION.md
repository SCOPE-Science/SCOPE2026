---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For a<b, 2(T(b)-T(a))=(b-a)(a+b-1). The two positive factors have opposite parity, one strictly smaller, and product divisible by 2m. The odd member O has d=gcd(O,w) dividing w; coprimality forces the even E to be divisible by 2m/d. Thus 2b-1>=d+2m/d. Taking O=d,E=2m/d attains equality and makes integer difference m. Two distinct odd divisors cannot tie since d1*d2=2m impossible parity; equality forces a unique earlier witness. Independently scanned all m=1..2000 using direct first repeat and checked uniqueness and prime power boundary formulas; m=1 included. Indices are positive, T(1)=0.

## originality

PASS

The optimized discriminator literature fixes the prefix and seeks minimum modulus, not the exact first failure for any fixed modulus; earlier prime-power analysis of 2k(k-1) does not handle arbitrary composite m, while Ulness 2022 studies modular triangular pattern structure. This source gives explicit all-moduli formula and unique integer-difference witness.

## value

PASS

Natural and exact maximal injective-prefix length for a classical integer polynomial modulo every positive m; unique first witness, exact difference, and prime-power boundaries give an independently useful reusable arithmetic invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
