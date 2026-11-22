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

# Verification of the paired-cubic irreducibility theorem

The attached `verify.py` uses an Eratosthenes sieve to list every prime through \(850\) (exactly \(146\) primes). For each prime it constructs the full rational-map image \(T_p\) and computes \(N_p=p-|T_p\cup(-T_p)|\). Independently, for all primes through \(101\), it evaluates the two original cubics at every field element and compares the resulting irreducibility counts. The observed zero-count primes are exactly \(2,3,5,13\).

The analytical proof does not infer a universal assertion from computation. It proves geometric monodromy \(S_3\times S_3\) and genus \(13\) in characteristics at least \(11\); a Frobenius twist and the Weil bound give \(\lvert9N_p-(p+1)\rvert\le26\sqrt p+93\). The explicit lower bound is positive at every integer \(p\ge851\), leaving the finite sieve only to classify primes below that cutoff.

The certificate also evaluates example values \(N_7=N_{11}=2\), \(N_{13}=0\), \(N_{17}=2\), \(N_{19}=2\), \(N_{23}=2\), and \(N_{29}=6\). The exact symbolic derivative, discriminant, resultant and branch indices are established algebraically in `RESULT.md`; the standalone certificate concerns finite arithmetic, not a computer-assisted proof of the Weil bound. Independent audit has not been performed.
