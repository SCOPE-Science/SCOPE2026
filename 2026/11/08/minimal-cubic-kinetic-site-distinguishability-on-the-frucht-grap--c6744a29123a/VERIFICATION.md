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

## Exact computational checks

`python3 verify_frucht_adsorption.py` uses two distinct exact rational/integer dynamic programs on the declared eighteen-edge graph. The neighborhood-removal recurrence examines 97 distinct subsets; the independent arrival-order state recurrence counts exactly \(12!=479001600\) permutations (aggregated by states) and reaches 31 terminal accepted sets. It compares all twelve rational occupation probabilities and the full terminal cardinality law, including zero probability at all other occupancies, and checks sharp minimum numerator gap four when the probabilities have common denominator 17280. There is no Monte Carlo sampling, floating point approximation or unverified extrapolation. The twelve-vertex lower bound uses the known asymmetric-cubic-graph classification independently of the program.

## Scientific limits

The certificate verifies the finite kinetic calculation; it does not classify all cubic graphs or establish a previously unknown graph-catalog fact. The attached file contains its complete graph data and all computational dependencies (Python standard library). Historical priority beyond inspected sources has not been independently established.
