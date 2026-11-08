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
# Computational verification and limits

Run `python3 artifacts/check_attractors.py` with Python 3 standard library and `python3 artifacts/check_spectrum.py` with Python 3 and NumPy. Exact captured outputs are in `artifacts/attractor_output.txt` and `artifacts/spectrum_output.txt`.

The first checker exhausts all 46 graph parameter pairs \(2\le a\le8\), \(1\le b\le8\), \(a+b\le12\), examining 46,088 labelled configurations and their selected-vertex transitions. Its Tarjan algorithm identifies the complete closed communicating-class decomposition, checks that the recurrent set equals the entire maximum-cut set, and independently computes predicted class sizes. The second reconstructs every two-rank Laplacian and checks the complete integer eigenvalue multiset and gap for 13 nonabsorbing parameter instances, totalling 574 matrix rows over those tests. Both checks returned their respective `*_OK` markers.

These computations are finite regression checks. The universal claims for every integer \(a\ge2\), \(b\ge1\) rest on the explicit cut path, global cut classification, and Boolean-lattice singular-value argument in RESULT.md. NumPy diagonalization checks use an absolute eigenvalue tolerance of \(10^{-8}\); they do not constitute exact certificates for arbitrarily large matrices. There is no independent audit evidence.
