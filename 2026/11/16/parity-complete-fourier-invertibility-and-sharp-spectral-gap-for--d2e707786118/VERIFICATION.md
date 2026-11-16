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

# Reproduction checks

The script `ladder_walsh_check.py` is self-contained and requires only Python 3. Execute with `python3 ladder_walsh_check.py`. It enumerates all spanning trees independently of the signed matrix-tree determinant, constructs the full Boolean edge indicator, and computes complete integer Fourier coefficients by a Walsh–Hadamard transform.

Checks performed: all frequencies for \(n=1,\ldots,7\), with ordinary spanning-tree counts \(1,4,15,56,209,780,2911\). At \(n=2,4,6\), the zero counts from exhaustive computation were \(6,200,7378\). For every odd tested length, no coefficient was zero and the smallest absolute value was \(1\); for every even tested length, the explicit family vanished. The determinant-of-cofactor identity for the all-negative-rungs signature was checked at \(n=1,\ldots,13\), and the flexible signed-path eigenvector was tested across all designated rail sign assignments for even \(n\le22\). The expected terminal marker is `LADDER_SPANNING_TREE_WALSH_EXACT_CHECKS_PASS`.

These are finite independent computations checking the algebraic derivations, not a computational certificate for all \(n\). The infinite statements follow from the determinant factorization, eigenvector witness, and parity argument supplied in `RESULT.md`. No external audit has been performed.
