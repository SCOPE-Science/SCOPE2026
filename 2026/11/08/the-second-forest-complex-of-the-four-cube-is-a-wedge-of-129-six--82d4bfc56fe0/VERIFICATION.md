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

The reproduction command is `python3 verify_q4_forest2.py` and uses only the standard Python library. Run on this package's included script, it prints the exact line `VERIFY_Q4_SECOND_FOREST_WEDGE129_S6_OK` upon success. The output file is an actual completed run, not a promise of execution.

Independent face checks: union-find acyclicity plus maximum-degree predicate; separate DFS componentwise edge counting, checked against each other on all 65,536 subsets. Both gave 14,911 augmented simplices with face vector by cardinality \((1,16,120,560,1732,3552,4616,3392,922)\). There are 192 maximal six-faces and 922 maximal seven-faces (dimensions six and seven).

For forward and reverse vertex-toggle orders, all 85,424 Hasse incidences among the 14,910 nonempty faces were oriented and topologically sorted. Each matching has 7,383 pairs and remaining critical counts one zero-cell, seven five-cells, 136 six-cells. Both complete signed Morse degree-six matrices have a seven-by-seven minor of determinant \(-1\), computed with exact integer Bareiss elimination; both have 105 nonzero matrix entries. Direct original simplicial mod-two boundary ranks in degrees one through seven are \((15,105,455,1277,2275,2341,922)\).

The proof additionally uses standard discrete Morse cell equivalence and the Hurewicz classification of maps out of five-spheres into a wedge of five-spheres; these topological theorems are mathematical premises, not computationally verified by this script. It does not check arbitrary hypercube dimensions or inclusion-induced persistence. Independent external audit remains not performed.
