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

# Executable verification and proof boundary

Run `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python checker.py` in a directory containing the embedded `checker.py`, with NumPy and SciPy installed. It independently builds the eight-dimensional tensor Hamiltonian, exponentiates it, and reconstructs each qubit's excited-battery probability. It checks random complex pure chargers, both signs of detuning, nonzero coupling and collision duration; it verifies concurrence-resolved upper bounds, three attaining rotations, and equalized local product measurement probabilities. A specified four-component maximally entangled non-Bell charger is checked over several input phases and eight consecutive exact recurrences.

Observed: `PASS: 525 independent checks; 75 random full-Hamiltonian comparisons, 75 local measurement equalizations, concurrence sharpness at 3 angles each`, followed by `PASS: 24 additional maximally-entangled closed-recursion checks; non-Bell charger converges to half-charge`. In the explicit example the phase-swing roundoff was \(2.22\times10^{-16}\) and the one-step excitation with the documented parameters was \(0.40588235294117636\).

These randomized finite checks are corroboration, not an exhaustive certificate or an independent audit. The exactness and all-parameter conclusions rest on the analytic excitation-sector reduction, the pure-state concurrence/Bloch argument, the equality construction and the local-product zero-diagonal lemma in `RESULT.md`. No claims are made for noisy dynamics or mixed charger states.
