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
# Verification of the composite cyclic minimax

Run `python3 verify.py` in a Python environment with NumPy installed. The checker constructs the complete complex linear operator lifting from the normalized projectors, performs singular-value decompositions independently of the analytical Weyl diagonalization, and compares the result with the full closed ambiguity spectrum at each optimal candidate. It checks the sharp ratio and three perturbed parameter choices in each of eight composite dimensions: 6, 8, 9, 10, 12, 14, 15, 16.

Actual execution: `DIRECT_SPECTRA_PASS 1134`. This comprises 1102 individual spectral singular-value comparisons and 32 additional ratio/perturbation assertions. Each dimension's direct matrix size is \(N^2\times N^2\); the largest tested dimension is \(N=16\). All comparisons were within the specified NumPy tolerances. These finite computations do not constitute proof for every composite order, and the stated all-order theorem rests on the mathematical steps in `RESULT.md`.

The sharpness argument verifies all three separate ambiguity branches and the arithmetic zero-product case. The comparison with earlier prime-only and all-modulus rank statements is about mathematical implication, not just differing titles.
