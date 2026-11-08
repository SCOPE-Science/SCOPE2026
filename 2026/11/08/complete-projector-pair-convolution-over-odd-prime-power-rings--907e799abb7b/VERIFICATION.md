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
# Verification evidence

The complete proof of the infinite family is in `RESULT.md`, with all congruences, valuation ranges, Hensel-lifting steps, and Fourier normalization. The accompanying standard-library `check.py` separately enumerates the projector set and each ordered pair for moduli \(3,9,27,5,25,7,11,13\). It verifies the complete pointwise convolution against the formula on **all trace-two target matrices**, every target's positive support, the sharp minimum and its multiplicity, and the closed additive energy by integer arithmetic. Running `python3 check.py` printed `PROJECTOR_PAIR_CONVOLUTION_PASS` with assertions enabled.

At modulus \(9\) it checked \(108\) projectors and \(729\) targets, with energy \(218700\) and minimum \(12\), attained at \(378\) targets. At modulus \(25\) it checked \(750\) projectors and \(15625\) targets, with energy \(25031250\) and minimum \(20\), attained at \(3750\) targets. At modulus \(27\) it checked \(972\) projectors and \(19683\) targets, with energy \(54561276\). These observations corroborate but cannot certify the all-prime, all-depth theorem. The Fourier fourth moment is verified mathematically by character orthogonality; no floating-point Fourier computation is used as proof.

Independent mathematical review has not been performed. General prior density formulas may pose a historical-priority risk.
