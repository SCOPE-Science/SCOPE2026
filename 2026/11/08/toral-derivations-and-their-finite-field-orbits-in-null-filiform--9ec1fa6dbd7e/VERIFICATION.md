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
# Computational verification

The script `verify_toral.py` is self-contained and uses only Python 3's standard library. Run `python3 verify_toral.py` in a directory containing that file. It computes finite fields of orders 2, 3, 4 (using \(t^2+t+1\)), and 5; it derives the matrix of each candidate derivation and directly checks all defining Leibniz derivation equations. It then compares powers \(D^p\), matrix rank, and the explicit spectral-projection conjugacy. Seventeen cases range from \((q,n)=(2,2)\) to \((5,4)\), including \((4,5)\). In six additional small cases the script enumerates every \(n\)-by-\(n\) endomorphism and independently recovers the complete derivation parameterization and predicted toral count.

The captured stdout is in `toral_output.txt` with the final line `NULL_FILIFORM_P_TORAL_DERIVATIONS_PASS`. Sample outputs: \(q=2,n=7\) gives 9 toral derivations, \(q=3,n=5\) gives 55, \(q=4,n=5\) gives 17, and \(q=5,n=4\) gives 501. All assertions completed. These finite tests do not certify infinitely many field orders and dimensions; those rely on the proof in `RESULT.md`.

No independent audit or certification has been performed.
