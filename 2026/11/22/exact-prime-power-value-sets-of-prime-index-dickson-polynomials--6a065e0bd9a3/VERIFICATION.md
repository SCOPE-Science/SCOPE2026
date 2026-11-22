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

# Verification and scope

Run `python verify_prime_dickson.py` in a Python environment with SymPy available. The script directly builds the Dickson polynomials by recurrence, verifies the two critical polynomial identities for primes 5, 7, 11, 13, and 17, and enumerates the complete image/fiber histograms for 108 prime-power parameter cases. It additionally checks the excluded characteristic-three counterexample at modulus 81.

The proof in `RESULT.md` is an all-prime, all-exponent argument. Its two nonstandard steps are independently restated here: the normalized derivative is \(D_p'(X,a)/p\equiv(X^2-4a)^{(p-1)/2}\pmod p\), yielding bijective normalized ordinary branches; in the square-parameter exceptional branches, \(D_p(2+pu,1)=2+p^3uE(u)^2\) with \(E(u)\equiv1\pmod p\), yielding bijective normalized singular branches. Every other conclusion follows from these branch bijections and distinct reductions modulo \(p\).

The finite computations certify their tested cases and identities at the tested small primes only. They are not an infinite certificate. No independent audit, external verification, or institutional certification has been performed.
