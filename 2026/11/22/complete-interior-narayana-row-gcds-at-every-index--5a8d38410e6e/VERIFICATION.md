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
# Reproducible checks and their limits

Run `python3 verify.py` with the standard Python library. The checker directly recomputes the integer Narayana row and its gcd for every index from 3 through 600 (598 rows); separately, Legendre's factorial-valuation formula checks 5210 local prime-minima for indices 3 through 700, including irrelevant primes; it then tests 21 explicit boundary and larger prime-power cases. The observed output from the packaged program is `VERIFY_OK direct_rows=598 local_minima=5210 special_cases=21`.

These are exact finite calculations; they neither enumerate all indices nor establish an infinite theorem. The mathematical proof for all indices is the four-step primewise argument in RESULT.md, including Lucas witnesses and sharp valuations at prime-power rows and predecessors. Independent audit has not been performed. Historical priority remains subject to unlocated or inaccessible literature.
