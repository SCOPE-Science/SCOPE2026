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

The analytical argument uses the signed-arcsine supporting-line distribution, an exact arcsine angular integral, a comparison with the complete elliptic integral \(K\), a uniform logarithmic singular expansion, and Scheffé's lemma. The first four are reconstructed in `RESULT.md`; their denominator normalization and the integrable endpoint \(\lambda=u=1\) are explicit there.

Execute `python check_offcenter_chord.py` with packages in `requirements.txt`. The checker calculates the exact angular interception probability independently of the endpoint simulation; it compares fixed-radius intensities to SciPy's elliptic integral, compares compact-parameter boundary asymptotics at three target radii, and simulates 1,600,000 independently selected endpoint pairs for each of two target positions using the Cartesian line-point distance formula. Its diagnostic completion message is `OFFCENTER_BOUNDARY_CHORD_CHECKS_OK`. The numerical tests support normalization and finite-scale accuracy; they neither certify uniform-infinite limits nor replace the proof of the conditional total-variation limit.

The proof does not settle the case of disks protruding outside the unit circle, nor give a uniform estimate as \(\lambda\to\infty\). The most directly related 1966 primary article was not fully accessible; independent historical verification remains undone.
