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

# Verification and reproducibility

`CHECK.py` is a complete standard-library Python 3 checker. From the directory containing these files, run `python3 CHECK.py`.

Its exact arithmetic checks verify \(\det A_1=\det A_2=1\), their common trace \(-4\), common squared Frobenius norm \(18\), both matrices \(Q=I+A^\mathsf TA\), their determinant \(20\), and the shortest positive reciprocal-quadratic values \(1/10\) and \(1/5\) with multiplicity two. The next distinct values are \(2/5\) and \(3/10\).

The checker enumerates all integer quadruples with entries from \(-4\) through \(4\) and determinant one, retains the hyperbolic matrices of squared Frobenius norm at most \(18\), and prints the complete eight signed-trace/cost groups. It finds an explicit signed-unimodular integral change of basis relating every quadratic form within each fixed-trace group of cost less than \(18\). The search bound is exhaustive because a matrix entry of absolute value at least five would already exceed the cost budget.

For the reciprocal-lattice minima, \(Q^{-1}\succeq I/\det Q\) in this two-dimensional determinant-one family. Since a coordinate unit vector has dual length at most \(1/2\), a minimizing integer vector at the relevant costs must have squared Euclidean length at most \(10\); the checker covers this region. Its direct-versus-Poisson truncated Gaussian comparisons cover ten parameter/matrix pairs and serve only as diagnostics.

**Limits:** Finite direct-sum truncations are not proofs of Poisson summation or asymptotic Gaussian-tail estimates. The analytical argument in `RESULT.md` proves the infinite identities and remainder. No external independent review or certification has been performed.
