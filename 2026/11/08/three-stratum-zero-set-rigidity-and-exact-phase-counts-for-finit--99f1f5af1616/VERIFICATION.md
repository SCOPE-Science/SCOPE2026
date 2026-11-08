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
# Reproducibility

Run `python3 CHECK.py` in the same directory. The script requires only the Python standard library. It constructs the cyclotomic quotient \(\mathbb Z[T]/(\Phi_{pq}(T))\) and evaluates every requested polynomial as an integer coefficient vector. It compares all actual Fourier zero sets with the predicted empty/origin/line sets and verifies the coefficient assignments on every tested support. The executed run reported `CHECK_OK arrays=45188 Fourier_coefficients=1528052`.

The checks exhaust all nonempty supports of size at most four for \(p\in\{5,7\}\) and \(q\in\{2,4\}\), all such supports for \((p,q)=(5,8)\), and the indicated four-site support for \((p,q)=(7,8)\). They do not exhaust untested primes or support sizes. The proof for all parameters is the four-step algebraic argument in `RESULT.md`, not finite enumeration. No independent audit has been performed.
