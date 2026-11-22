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

# Reproducibility and scope

Run `python checker.py` in a directory containing the supplied complete files. The checker uses standard-library arbitrary-precision rational arithmetic to bracket \(\pi\) through Machin's formula and alternation for \(\arctan\), bracket \(\sqrt2\) and \(\sqrt\pi\) by exact squared-rational comparisons, and bound Gaussian special-function values using alternating Taylor series. It verifies \(L'(.99)>0\), \(L'(1)<0\), \(L(1)<0.4\), and \((2-\sqrt2)/\sqrt\pi>0.33\), giving the explicit strict hub-versus-leaf margin. It then tests scalar spectral expansions at selected positive times, degrees and cut positions, and checks an eigenfunction normalization with a finite-tail tolerance.

The proof of the infinite-dimensional operator inequality and all global extremizers is in `RESULT.md`, based on BV derivative-measure decomposition, orthogonal heat-semigroup splitting, Gaussian reflection bounds and Hilbert equality rigidity. Finite evaluations do not prove uniform inequalities over all cut positions or times, nor do they identify the largest admissible time threshold. No independent audit has been performed.
