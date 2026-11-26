---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The four cases cover all n>=3 of support size at most five. Even mixed supports force 6|psi(n), so phi(psi(n))/psi(n)<=1/3, and strict monotonicity of 1+1/p bounds psi(n)/n by 1152/385. Equality requires both the first five primes and no prime outside {2,3} in psi(n); the prime-power formula forces exponents 1 at 5,7,11 and allows any positive exponents at 2,3. Remaining cases give 1/2, 512/715 and 20480/22971, each strictly smaller. Direct computation gives psi(39270)=124416 and its totient 41472; it shows failure is possible at six factors, not that every six-factor input fails. At n=2 the composition equals 2. The independently written /workspace/reproduction/independent_5.py uses exact trial division and reproduced 299731 eligible inputs, 22 equality cases and 23 violations (first 39270) up to 300000; the unbounded result rests on the proof, not the finite run.

## originality

FAIL

Demonstrably covered by a mechanical sharpening of the already published October 12 five-support barrier proof. Its actual proof, not just its stated theorem, gives the exact bounds 1/3 and 1152/385 for the two factors of the even ratio. It also already bounds the odd branches by (1/2)(4608/2431) and (1/3)(1536/715), both strictly below 384/385. Multiply the displayed bounds and inspect equality in those same two even products: the five smallest primes are necessary, and no other primes than 2 and 3 may divide psi(n); the prior prime-power formula gives exactly the stated equality family. The prior record already gives the very same six-prime counterexample. No new inequality or case estimate is needed for the assigned sharp global result. The same-date six-support record supplies parallel overlap but is not needed to infer priority.

## value

FAIL

An exact maximum with equality cases on the five-support layer is a natural question, but this answer simply reports the sharp product of the earlier quantified bounds and their elementary equality conditions. The changed odd split is unnecessary for the frozen maximum, and the reversal is known. No independently valuable unresolved remainder is shown.

The dated certificate retains the supplied scientific assessment, sources and limitations.
