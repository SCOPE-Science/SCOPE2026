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
# Verification and limits

Run `python CHECK.py` using the Python standard library. It enumerates every affine-branch solution of \(T^m(x)=x\) for \(2\le m\le12\) over exact rational numbers, rejects branch-inconsistent solutions, counts crossings, computes least period, and checks both the exact marked fixed-point coefficients and the proposed Möbius-inverted primitive-orbit counts. The completed invocation reported 8,202 exact comparisons and no discrepancies. The code is finite validation only; neither infinitely many periods nor the Gaussian limit are certified computationally.

The unrestricted results are supported by the argument in `RESULT.md`: inverse-branch uniqueness on the Markov partition, complete treatment of the two periodic boundary points, a weighted trace identity, arithmetic inversion and an analytic Perron-eigenvalue/quasi-powers central limit argument. The conversion from over-rotation number to unfolding number uses the published low-modality equality theorem (Bhattacharya, arXiv:2403.16549, Corollary 4.11). No external independent audit has been performed.
