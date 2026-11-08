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

# Reproduction of exact finite checks

`verify_morse.py` uses standard Python only. It reconstructs the specified twenty-four-edge graph, enumerates every matching, verifies the deterministic \(1385\)-pair partial matching, and topologically sorts the complete \(10816\)-cover Hasse orientation. It computes the exact signed integral \(46\times18\) Morse boundary and the specified determinant-three maximal minor using fraction-free integer elimination. Ranks over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) are \(18,17,18\). These facts imply exactly one nonunit Smith factor, equal to three.

`verify_simplicial.py` independently generates all matching faces via combinations and computes full simplicial boundary ranks over three prime fields, yielding reduced Betti vectors \((0,0,0,28,0,0)\), \((0,0,0,29,1,0)\), and \((0,0,0,28,0,0)\) for characteristics two, three, and five.

Run `python3 verify_morse.py` and `python3 verify_simplicial.py` from the directory containing these files. Their expected successful output is saved verbatim in `verify_output.txt`. The proof of the *integral homotopy type* uses the complete finite acyclicity verification plus the integral signed matrix and degree-classification argument; the modular calculation alone does not certify it. The checks are finite and do not claim a general family result. Independent human mathematical validation has not been performed.
