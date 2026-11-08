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

# Reproducible verification

The theorem is proved symbolically in `RESULT.md`. To reproduce finite corroboration, run `python3 verify.py` from the directory containing that file. The program uses only the standard Python library, performs no downloads, and prints the field, scalar, computed character-exponent set, predicted total, and direct coefficient-enumeration count. Its recorded output is embedded as `verification_output.txt` and ends with `VERIFY_OK checked=24`.

The checks include all permissible scalars over the prime fields of orders \(3\) and \(5\), several over \(7\), every permissible scalar over the additive field \(\mathbb F_9\) with \(\mathbb F_3\)-coefficients, every permissible scalar over fields of orders \(4\) and \(8\) with \(\mathbb F_2\)-coefficients, and two selected scalars over \(\mathbb F_{16}\) with \(\mathbb F_2\)-coefficients. In the extension-field checks, field multiplication is implemented by the irreducible polynomials \(T^2+1\) over \(\mathbb F_3\), \(T^2+T+1\) and \(T^3+T+1\) over \(\mathbb F_2\), and \(T^4+T+1\) over \(\mathbb F_2\). A separate bitmask recurrence tests all \(2^{16}\) binary coefficient vectors in the largest finite check, without reusing the character-space proof.

The exhaustive cases are finite checks only: they do not prove the formula for arbitrary field size, coefficient degree, or parameter. The general result instead follows from the nilpotent augmentation ideal, exponent-\(p\) principal-unit group, equivariant filtration, Maschke splitting, and regular-character decomposition, as recorded in `RESULT.md`. The categorical/historical priority of the theorem has not been independently audited.
