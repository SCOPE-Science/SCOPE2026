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

# Verification

Analytic verification uses a complete orthonormal cosine basis on each zero-mean input cell and sine basis on each output cell. For each positive threshold the number of singular values strictly above it is a sum of exact ceiling-minus-one counts, so equality at the minimal threshold is also fully controlled. The power-sum formula uses an absolutely convergent Dirichlet series for every real \(p>1\).

`python check_spectrum.py` was run with Python 3 and reported `PASS: 55907 exact rational assertions; indexed value uses units pi*s_k`. It tests positive integer compositions and additional rational meshes for positive cell counts through five and ranks through eight, including equality rigidity and the two-cell second-rank example. These finite tests are supplemental to the proof. The findings are not independently certified.
