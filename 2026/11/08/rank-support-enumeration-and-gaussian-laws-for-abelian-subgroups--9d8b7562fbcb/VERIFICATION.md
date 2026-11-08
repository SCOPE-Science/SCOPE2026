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

The complete rank–support formula and central limit theorem are proved mathematically in `RESULT.md`. Finite checks supplement the proof rather than replacing it. Running `python3 verify.py` verifies the coefficient-by-coefficient equality of two independently organized counts: direct enumeration of reduced-row-echelon subspaces satisfying path-edge isotropy, and transfer-matrix counts followed by subspace-lattice Möbius inversion. The script handles prime fields \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) and the extension field \(\mathbb F_4\), and it separately checks the rank-two rational generating function.

Expected output: `VERIFY_OK: 86 independent reduced-echelon support enumerations plus rank-two rational-series checks`.

The tests do not verify asymptotic convergence for all lengths, the publication-priority claim, or the entirety of known literature. All scientific claims rely on the proof's exact transfer identity, Gaussian inversion, and strict dominant-eigenvalue gap. No independent mathematical audit has been performed.
