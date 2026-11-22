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

# Reproducibility and verification

To run the bundled standalone diagnostic, install the NumPy dependency specified in `requirements.txt` and execute `python verify.py` in the same directory. The script recomputes full Euclidean-arclength chord averages from the two graph branches, integrates each of the four ordered pair types, and uses exact perimeter normalization. It compares differences in the rescaled deficits between \(\varepsilon=0.04\) and \(\varepsilon=0.02\), against the predicted squared-width coefficients \(1/48\) for a triangular tent and \(1/30\) for the parabolic profile. A shifted parabola with different graph midline is also tested. All three diagnostics passed during preparation.

The proof independently checks the normalization \(\mathbb E|U-V|=2/3\) for independent horizontal uniforms on \([-1,1]\), which after division by perimeter four gives \(1/6\). The logarithm arises from opposite-graph pairs only. The exact integral primitive and its uniform expansion for widths bounded by endpoint distance establish the claim for all admissible Lipschitz profiles. The finite numerical checks cannot establish this infinitely quantified theorem, originality or independent verification.
