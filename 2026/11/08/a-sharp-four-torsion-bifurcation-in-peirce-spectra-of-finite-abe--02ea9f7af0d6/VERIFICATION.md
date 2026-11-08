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

## Exact reproducibility

Run `python verify.py` with Python 3 and SymPy installed. The script uses explicit basis products \(e_xe_y=e_{2y-x}\), not the Fourier recurrence used in the proof. It checks 14 cyclic and product-group presentations of orders 1–12, 188 exact assertions, the idempotency of the uniform and basis elements, the spectral boundary witnesses, and six specializations of the four-torsion eigenvalue construction including \(2+3i\). It prints each tested group and a final `VERIFY_OK` line. A full replay produced byte-identical `verification_output.txt`.

## Limits of computation

This is finite testing of selected idempotents, not exhaustive enumeration of all complex idempotents. The arbitrary-\(G\) and arbitrary-\(\lambda\) statements rely on the symbolic Fourier argument and exact representation block decomposition in `RESULT.md`. No external or independent validation was performed.
