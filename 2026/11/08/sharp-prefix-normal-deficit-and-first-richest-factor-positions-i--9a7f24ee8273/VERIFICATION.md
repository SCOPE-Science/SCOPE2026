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

The scientific proof is the two all-length induction arguments in `RESULT.md`. Verification uses Python standard-library programs provided with their source, not external certification. Actual execution results:

```
DIRECT_OK extrema n=1..512, special positions j=1..7, length 32768
DIGITAL_OK length 16384 sharp envelope j=1..7; all four recurrence cases checked
```

`verifiers/verify_direct.py` independently generates the substitution fixed-point prefix and computes every sampled factor's ones count for lengths 1 through 512. It confirms the structural extrema recurrences and the unique first maximizer among starting indices zero through \(N_r\) for seven levels. The sampled factor extrema do not certify the entire infinite word; the parity argument in `RESULT.md` does.

`verifiers/verify_digital.py` calculates the fixed point from the parity of the two-adic valuation of \(j+1\), checks the resulting bit recursion, compares its prefix sums with the exact recurrence, and checks deficit and sharp-envelope identities up to 16384. Again the infinite property depends on the induction, not its finite sample.

The proof's elementary arithmetic and finite scripts do not constitute independent human audit. The all-length numerical extrema were studied in earlier abelian-complexity literature; the additional positional uniqueness and earliest-start assertion are the main distinctive statements and deserve independent examination.
