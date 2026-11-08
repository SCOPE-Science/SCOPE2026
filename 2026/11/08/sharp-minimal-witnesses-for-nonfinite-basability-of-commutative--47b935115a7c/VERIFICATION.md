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

# Verification record

Run `python3 verify.py` using Python 3 and only its standard library, from the directory containing this file. It builds finite multiplication tables, checks all ordered triples for associativity, and checks zero absorption, commutativity, exact cardinality, strict power filtration, nilpotency index, vanishing maximal powers, and the invariant separating the parity and hook family. The generated `verification_output.txt` records 16 constructed models and 76,824 ordered associative-triple tests, including \(d=3,\ldots,13\) for hook models and odd \(d=5,7,9,11,13\) for parity models.

These are exact finite computations but do not enumerate **all semigroups** of those orders; the lower bound and unrestricted family assertions are mathematical deductions in `RESULT.md`. The necessary full-power-semiring finite-basis equivalence is an explicitly cited published theorem (Wang–Yin–Wang, Corollary 1.2), not recomputed or independently reproved here. The computed examples test its semigroup-side hypothesis, not the infinite problem of finite equational bases. Independent mathematical audit: not performed.
