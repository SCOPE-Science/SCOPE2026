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

# Verification instructions

Run the two standalone Python 3 standard-library files as follows:

```text
python verify_matching_symmetry.py
python verify_direct_coloring.py
```

The matching-first program independently determines \(288\) perfect matchings, \(144\) unlabelled three-factorizations, their complete \(S_6\)-orbit and the \(36\) distinct order-five stabilizer subgroups. For each stabilizer, it checks four factorizations forming the full induced \(C_4\) quotient. It also checks all colour-pair two-factor cycle patterns, \((30)\) and \((10,20)\).

The direct-colouring program independently enumerates all proper named three-edge-colourings by constrained assignment of the forty-five incidence edges, generates full bichromatic-component Kempe changes, and checks that the \(864\) states form \(36\) components of \(24\) states each, all five-regular with shortest-path profile \((1,5,13,5)\) from every state. Both programs have been executed successfully on their actual file paths. No randomized tests are used, and no infinite statement is inferred from finite enumeration.

The scope is exactly the thirty-vertex duad–syntheme Tutte–Coxeter graph with the specified Kempe move. No independent audit was performed.
