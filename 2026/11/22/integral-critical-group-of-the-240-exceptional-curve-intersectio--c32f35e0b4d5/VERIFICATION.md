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

# Reproducibility notes

Run `python3 verify_e8.py` using Python 3 with no optional dependencies. The executable generates the entire doubled-root model of \(E_8\) from first principles. It verifies the exhaustive incidence and degree counts, connectedness, and the exact matrix identity \(A^4-114A^3-1620A^2+13608A=0\). It then performs two complete independent-sink reductions of the \(239\)-square Laplacian for each of the four primes dividing the spanning-tree number.

The finite Smith computation uses exact modular integer operations: unit pivots are invertible in the current prime-power ring; a residual block is divided only when every entry is divisible by the prime; precision \(2^9,3^5,5^3,7^3\) resolves every pivot. The resulting invariant factors satisfy divisibility and have product \(2^{508}3^{393}5^{83}7^{120}\), as independently computed from the exact adjacency spectrum. The executable prints `E8_DEL_PEZZO_240_CRITICAL_GROUP_OK` after all assertions pass.

No floating-point eigensolver, probabilistic rank estimate, or incomplete enumeration supports the theorem. The transfer from this finite model to every smooth degree-one del Pezzo surface in characteristic zero relies on the classical exceptional-class/\(E_8\)-root identification. Independent external review and global historical priority certification remain unperformed.
