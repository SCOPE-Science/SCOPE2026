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

The complete analytical proof is in `RESULT.md`. Its central proof obligations are: tight-edge connectivity and integrality of all maximizers; disjoint endpoint support of level-zero and level-two families; the concave two-capacity envelope; strict improvement under balancing and strict separation of high-imbalance and binary configurations; and the exact equality count. All were checked symbolically, for every integer \(n\ge4\), without depending on enumeration.

Execute `python3 verify_triangular_spread.py` (standard Python 3, no external packages). The checker independently enumerates admissible integer-valued profiles for \(n=4,5,6\), verifies the exact sharp numerator and complete number of maximizers, and uses integer arithmetic to check the capacity envelope and closed formulas over additional finite ranges. Verified output:

```
EXACT_ALL_INTEGER_EXTREMIZERS_OK 4 6 6
EXACT_ALL_INTEGER_EXTREMIZERS_OK 5 110 20
EXACT_ALL_INTEGER_EXTREMIZERS_OK 6 2120 20
EXACT_CAPACITY_ENVELOPE_INEQUALITIES_OK 22201
EXACT_CLOSED_FORMS_AND_BINARY_SEPARATION_OK 2997
ALL_TRIANGULAR_GRAPH_SPREAD_CHECKS_OK
```

The integer capacity comparison extends only through \(n=300\) in the checker; the formula checks extend through \(n=3000\). Their finite nature is explicit. The infinite statements rely on the displayed algebra in `RESULT.md` and do not follow from those finite experiments. Sources in `RESULT.md` support historical context, not a certification of publication priority. Independent audit remains unperformed.
