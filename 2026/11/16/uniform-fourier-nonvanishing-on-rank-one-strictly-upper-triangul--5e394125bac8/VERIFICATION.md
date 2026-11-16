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
# Finite exact corroboration

Run `python checker.py` with NumPy installed. The checker computes complete binary Walsh spectra through matrix dimension six, projective zero-count formulae for prime fields \(q\in\{3,5,7\}\), and direct trace-character transforms over \(\mathbb F_4\) through dimension four. It checks the exact low-dimensional zero counts and the congruence \(W\equiv-q\pmod{q^2}\) in every tested instance. It prints `RANK_ONE_TRIANGULAR_FOURIER_ALL_EXACT_CHECKS_PASS` only after all assertions succeed.

The calculations are finite corroboration, not substitutes for the chart proof over all fields and all dimensions. The prime-power check uses an explicit \(\mathbb F_4\) multiplication table and the actual additive trace character. No external proof certificate or independent audit has been produced.
