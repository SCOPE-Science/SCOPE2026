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
# Reproducibility record

The accompanying `dodecahedral_f1_verifier.py` checks the graph from its explicit thirty-edge description and does not read any previously generated evidence. Invoke `python3 dodecahedral_f1_verifier.py` from the directory containing the source file. The program enumerates all subsets, checks both equivalent independent predicates, constructs forward and reverse element matchings, checks acyclicity by a full directed-Hasse topological sort, calculates integral Morse differentials, proves unit maximal minors with fraction-free determinant arithmetic, checks chain composition, and independently determines the stage-zero complex. Exact console output is embedded in `VERIFIER_OUTPUT.txt`.

The positive-stage face count is 63,143 including the empty simplex; 31,566 face pairs are matched in each reduction; each full Hasse graph has 410,520 incidences. Ascending residual critical dimensions and counts are 5:1, 6:6, 7:4, with primitive boundary ranks 1 and 4. Descending residual critical counts are 5:2, 6:6, 7:3, with primitive boundary ranks 2 and 3. Both imply the homotopy type of a six-sphere by integral CW cancellation. Stage zero has 5,828 faces with four critical 5-cells.

Limits: finite computational certificate only for the precisely defined 20-vertex graph; the result does not establish a general family classification. The recorded run and self-review do not constitute an independent external audit.
