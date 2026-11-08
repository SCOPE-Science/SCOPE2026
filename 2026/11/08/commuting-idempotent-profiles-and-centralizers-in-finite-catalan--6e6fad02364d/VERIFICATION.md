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

# Reproduction and verification

Execute `python3 verify.py` using Python 3 and its standard library only. No external data is required. The script builds the full weakly increasing order-decreasing transformation monoids on labeled chains with one through seven points and compares their explicitly composed idempotents with the fixed-point-set normal form.

For each chain size from one through nine, it directly checks every ordered pair of idempotents for commutativity, records the full \((|S\setminus T|,|T\setminus S|,|S\cap T|-1)\) profile, and independently reconstructs the same trivariate coefficients from weighted compositions. It checks, separately, the commuting-idempotent centralizer size for **every** idempotent at these sizes by the endpoint-bit sum. It verifies the exact cardinality sequence and recurrence. A successful run ends with `VERIFY_OK`.

The verified totals for sizes one through nine are \(1,4,14,48,164,560,1912,6528,22288\). The finite experiments do not prove the rational identity for arbitrarily long chains or the asymptotic distribution. Those statements follow from the fixed-point normal form, the gap bijection, and rational partial fractions detailed in `RESULT.md`.

The integer sequence alone is known from OEIS A007070. Publication priority for the refined semigroup interpretation has not been independently established.
