---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification details

The exact-integer checker `verify.py` reconstructs equal half-divisor-sum partitions for \(2^b q\), checks coprime-multiplier preservation and the refined sieve implication. It checks that primes satisfying \(p\equiv N\pmod B\) but not \(p\equiv N\pmod{Bq}\) yield Zumkeller complements in each sampled finite case. Its finite output is not the infinite proof.

The analytic proof uses the prime number theorem to bound the least odd prime not dividing \(N\), and uses the classical Siegel–Walfisz theorem for both moduli \(B\) and \(Bq\), bounded by a fixed logarithmic power. Subtracting the two uniform formulas gives the local main term \((1-1/q)\operatorname{Li}(N/2)/\varphi(B)\) and a negligible relative error. The bounded-degree congruence test deliberately does not exclude even cofactors, which are absorbed into a higher power of two in the Zumkeller base.

Because the constants in Siegel–Walfisz may be ineffective, the proof does not give a numerical threshold or an exact all-prime-representation asymptotic. Independent audit has not been performed.
