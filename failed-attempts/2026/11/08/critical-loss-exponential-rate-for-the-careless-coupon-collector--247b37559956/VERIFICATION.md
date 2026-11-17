---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For each fixed k-set, stationarity yields a_k=q^k[(1-k/n)a_k+(k/n)a_{k-1}], hence exact finite product and binomial inversion for the full stationary occupancy law. Coupling from the empty set gives a per-time all-full probability <=pi; coupling arbitrary starts gives TV error <=nq^t and polynomial-size blocks to hit all full with probability >=pi/2. Thus E T has same exponential rate as 1/pi; the product Riemann sum gives I(c)=int_0^1 log[1+(e^{cx}-1)/x]dx. The argument proves fixed c>0 but not a hitting prefactor. Independently verified n=2,q=4/5 stationary mass 32/75. These correct statements exactly reproduce stronger earlier theorems.

## originality

FAIL

Exact mathematical coverage is decisive. Oct18 published paper proves the same fixed-c post-loss careless-coupon mean exponent I(c) and even in-probability log hitting-time concentration. Nov2 published paper proves exactly the same stationary all-subset product, its sharp A(c) prefactor, and the same critical exponential rate. Oct13 paper gives equivalent factorial-moment stationary law. No independently new final claim survives.

## value

FAIL

The results are correct but precisely reproduced and strengthened by earlier published theorems for the identical post-loss chain and scaling. Rewriting the product, adding elementary finite expectation inequalities, or recasting the same integral does not yield distinct value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
