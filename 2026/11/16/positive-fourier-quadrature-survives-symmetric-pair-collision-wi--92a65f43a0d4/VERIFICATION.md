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

The proof uses finite Fourier orthogonality; the Dirichlet-kernel trigonometric identity; strict cosecant comparison on the circle; rank of a one-pair-collision Fourier sampling matrix; and a first-order perturbation formula for an isolated simple zero singular value. These steps are stated explicitly in `RESULT.md`.

`python check.py` was executed successfully with NumPy and reported 1,226 passed assertions. The checks covered every odd grid size from 3 through 63, nine displacements at each size (including exact collision), exactness on all Fourier frequencies in the prescribed band, positivity, equality of the paired weights, and the numerical singular slope for eight odd sizes. The matrix at collision was checked for rank \(N-1\) at those sizes. These computations do not verify the theorem for unbounded \(N\).

The normalized integral is \((2\pi)^{-1}\int f\), Fourier evaluation is scaled by \(1/\sqrt N\), and the collision is approached from \(\alpha<1/2\). The unique pre-collision weights are distinguished from the merged-on-distinct-sites endpoint weights. Historical priority was assessed against relevant full texts and research-record summaries, without an independent audit or uniqueness certification.
