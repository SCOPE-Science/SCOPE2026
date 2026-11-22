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

The accompanying standalone `verify.py` is executable with Python 3 and SymPy. Running `python verify.py` reports `PASS exact symbolic identities and 1513 finite checks`.

Symbolic checks establish algebraic identities for the hub and leaf diagonals of the resolvent and for the simultaneous boundary. Exact rational tests construct the full Markov generator, invert the resolvent, check stochastic row sums, off-diagonal sign, and exact equivalence between all diagonal signs and the stated polynomials. Additional regime tests use 40-digit approximations only as corroboration.

The proof in `RESULT.md`, not numerical sampling, establishes the global unique return-rate optimum and all positive-real/integer quantifiers. Numerical tests cannot certify the infinite family or exclusion of all equivalent published sources. An independent mathematical audit has not been performed.
