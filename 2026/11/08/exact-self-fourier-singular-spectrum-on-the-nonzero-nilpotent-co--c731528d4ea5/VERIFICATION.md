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

# Reproducibility and limits

The theorem's proof is in `RESULT.md`. The direct numerical replay is `check_spectrum.py`, with its only external dependency in `requirements.txt` (NumPy). Run from the directory containing these files:

```sh
OPENBLAS_NUM_THREADS=1 python check_spectrum.py
```

The program constructs \(F=\mathbb F_q\) from an explicit irreducible polynomial, represents each nonzero nilpotent matrix by its unique scalar/projective coordinates, evaluates \(\psi(\operatorname{tr}(XY))\) using the finite-field trace, and computes singular values directly. It does not use the claimed multiplicative-character diagonalization to construct the matrix or to calculate singular values. The tested orders are \(2,3,4,5,7,8,9,11\). Every comparison passed, and the largest absolute difference between computed and predicted singular values was less than \(8\times10^{-15}\). This is a finite numerical check only; correctness for all prime powers relies on the written algebraic argument.

The proof's crucial nonstandard step is the projective character-conference identity: for \(t\ne u\), the cross-ratio map \(r\mapsto\Delta(u,r)/\Delta(t,r)\) bijects \(\mathbb P^1(F)\setminus\{t,u\}\) with \(F^\times\), causing off-diagonal Gram sums to vanish whenever \(\chi^2\ne1\). The other critical boundary is the unique quadratic character for odd \(q\), absent for even \(q\). Each is explicitly established in `RESULT.md`.

No independent audit has been performed. The available literature does not conclusively establish first historical priority, and the Kawanaka (1982) full text was not available for direct comparison.
