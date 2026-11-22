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

Run `python3 verify_conference9.py` in the directory containing the files. The checker requires only the Python standard library and performs 27 exact Laurent-polynomial verifications, followed by 39 supplementary independent numerical DFT comparisons. It checks the three full antipodal-pair families and exact reflection pairs. The submitted proof, not the experiments, establishes the universal inequality, the equality classification, and nonexistence of even conference signals on the nine-cycle. The numerical comparisons are tolerant to floating-point rounding and do not certify global optimality.

The Fourier transform is unnormalized. The sharp energy \(792\), conference benchmark \(648\), and excess \(144\) are integers in that normalization. Boundary choices \(z=\pm1\) can produce overlapping descriptions of the pairing families, but the proof covers these cases without assuming disjoint families. No independent audit is claimed.
