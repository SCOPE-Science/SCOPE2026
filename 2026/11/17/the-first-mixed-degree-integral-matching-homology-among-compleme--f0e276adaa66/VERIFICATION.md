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

The standalone program `verify_antihole.py` reconstructs all faces and signed boundary matrices for \(3\le n\le9\), computes integral unimodular reductions and checks that no nonunit Smith factors remain. It emits the exact face numbers, boundary ranks, and torsion-free reduced Betti groups listed in the finding. It uses only standard Python. Replay command: `python3 verify_antihole.py`.

Reproduced result: `ANTICYCLE_COMPLEMENT_INTEGRAL_BOUNDARIES_PASS`.

The independent finite-field checks over moduli \(2\), \(3\), and \(5\) agreed with the integer computation in the positive homology degrees for \(5\le n\le9\). These are corroborative only. No classification beyond \(n=9\), wedge-of-spheres homotopy equivalence, external audit, or independent certification is claimed.
