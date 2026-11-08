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

# Reproducibility

Run `python3 check_kneser.py` and `python3 check_petersen_exhaustive.py` with Python 3 and no external packages. The first constructs the Kneser graph \(KG(5,2)\) and checks all thirty independent pairs, the complement map in both directions, the induced path of length two, all sixty color-support assignments, and all one-color jumps. The second constructs the generalized Petersen graph \(GP(5,2)\) from outer-cycle, spokes and pentagram; enumerates all \(4^{10}=1,048,576\) assignments of the four possible color subsets and determines every optimum and every one-color jump. Their saved standard outputs are `kneser_output.txt` and `petersen_output.txt`. Both programs were run directly from their packaged source paths and returned successfully.

The finite enumeration is exhaustive for the defined ten-vertex models. The paper's analytic argument supplies independent proofs of the lower bound, complete optimal-state classification, and immobility. The two programs use distinct graph constructions and state-generation methods. They do not establish priority in the published literature or any extension to other graphs and moves. Independent audit has not been performed.
