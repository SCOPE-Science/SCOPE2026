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

The proof is self-contained apart from the conventional definitions of prime valuations, the Chinese remainder theorem, and known periodicity of the quotient (also independently established by the prime-local formula in the proof). The key recurrence is derived directly from the \(2\)-adic residue signs; the nonvanishing argument at odd primes uses parity of the number of residues, not a numerical assumption.

Execute `python3 verify.py`. The verifier uses only the Python 3 standard library and compares direct quotient computations with prime-local formulae, checks all dyadic recurrence values through level nine, and checks the exact candidate zero pattern up to window length 160. Its observed output was:

```
PASS: 34161 quotient residues; 1031 truncated-valuation sums; 3373 prime-local sign sums; k=1..160, e=1..9
```

The finite checks do not establish infinitely many cases; equations (1)–(9) in `RESULT.md` supply the all-integer argument. The previously published complete fixed-window value-frequency formula is an important coverage limitation: the new conclusion is the uniform cancellation locus, not the finite distribution itself. No independent mathematical audit has been completed.
