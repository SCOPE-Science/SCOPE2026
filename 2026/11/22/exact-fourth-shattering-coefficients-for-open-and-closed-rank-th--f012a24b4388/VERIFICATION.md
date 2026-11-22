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

The standalone Python checker enumerated 666 valid ordered Venn-cell multiplicity profiles and discarded 196 with duplicate queried triples. It reproduced all 15 grouped coefficients, the direct ordered-support identity at order nine, and both fourth-coefficient values at orders seven through twelve. The independent C++ test enumerated every unordered support of cardinality zero through four in the graph on 84 triples at order nine and reproduced both support polynomials through the fourth coefficient.

Run `python3 verify_kneser_rank_four.py` and `c++ -O3 -std=c++17 direct_kg9.cpp -o direct_kg9 && ./direct_kg9` in this directory. Only Python's standard library and a C++17 compiler are needed. The all-order conclusion relies on the finite, mathematically exhaustive four-row Venn-signature reduction, not on extrapolating the order-nine census. The code and proof have not received independent mathematical review.
