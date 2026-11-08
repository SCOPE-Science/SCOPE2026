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

# Verification details

The theorem is proved analytically using Weyl-basis Fourier diagonalization, integer zero-divisor completion of phase residues, the exact cosine-grid covering bound, and equality cases in AM--GM. The positivity comparison of non-mixed ambiguity branches uses only \(n\ge9\).

Run `python3 CHECK.py` with Python 3 and NumPy in the directory containing the unpacked files. Its actual finite checks covered odd composite orders 9, 15, 21, 25, 27, 33, 35, and 45; 120 randomized complex parameters per order; direct minimum ambiguity values, all mixed residue products, and an independently constructed full 81 by 81 lifted measurement singular-value decomposition at order nine. The executed checker reported `ODD_COMPOSITE_ONE_IMPULSE_CHECKS_PASSED 978`.

Finite checking cannot replace the unrestricted proof. The asserted minimax is within the one-coordinate-impulse family only; it makes no assertion of independent external validation, exhaustive publication priority, or robustness after erasures. The closely relevant 2026 source arXiv:2609.09614 was inspected at abstract level, not full text.
