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

The calculation and checks reported here concern the stated rare-seed first-hitting law only. The symbolic coefficients are reproduced independently from their finite products by `CHECK.py`. A separate Boolean bit-mask implementation constructs the Kneser adjacency relation, evolves configurations synchronously, and tests the transversal criterion and two-step identity on configurations of \(KG(9,3)\), \(KG(10,3)\), and \(KG(6,2)\). The fixed-seed numerical comparison covers \(k=3,4\) with \(n=120,240,480\); rare-obstruction sampling uses deterministic reproducible pseudo-random data for two additional parameter sets. All outputs appear in `CHECK_OUTPUT.txt`.

A finite computation does not certify asymptotic error terms. Those follow from the all-size exact disjoint-family probability, the two-identification obstruction classification, and a binomial factorial-moment bound for larger seed families. The rare-failure samples have statistical noise and finite-order corrections; they are not expected to equal the leading asymptotic term exactly.
