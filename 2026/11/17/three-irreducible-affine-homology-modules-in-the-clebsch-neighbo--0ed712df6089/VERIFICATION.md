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

The standalone `verify.py` was executed with Python 3 standard library only. It rebuilds the even-weight five-bit graph, confirms parameters \((16,5,0,2)\), enumerates the complete \(352\)-face open-neighborhood complex, and computes augmented boundary ranks \((1,15,65,64,16)\) over \(\mathbb F_2\). Elementary chain rank upper bounds prove these are also the ranks over \(\mathbb Q\).

For each of all \(1920\) affine automorphisms, two distinct integer computations of the reduced second-homology Lefschetz character agree: signed fixed faces and cycles of the vertex permutation inside invariant faces. Their character norm is \(3\). Discrete Fourier inversion on translations gives the exact multiplicities \((6,3,1)\) on the trivial, singleton and two-subset character orbits. Translation averaging reproduces the exterior-square standard character of \(S_5\). The verifier's last output line is `CLEBSCH_AFFINE_FOURIER_HOMOLOGY_PASS`.

All calculations are finite and exact. The code does not establish integral torsion, actions on other graph complexes, or mathematical novelty. Independent mathematical review has not been performed.
