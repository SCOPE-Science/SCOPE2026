---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 19–46. A positive restriction attains its norm exactly when its spectral maximum is an eigenvalue. The orthogonal complement of the eigenvectors reduces the operator, and the closed span of any strictly increasing eigenvalue sequence would also be a reducing counterexample. Conversely, reducing subspaces of a pure-point operator decompose by eigenspaces, so reverse well order suffices. Closure preserves the order condition (approximate an increasing sequence by eigenvalues in disjoint ordered neighborhoods); the gaps immediately below spectral points give countability by disjoint rational witnesses. Compact invariance of essential spectrum then makes the perturbed spectrum countable, hence the spectral measures atomic. A forbidden increasing sequence of perturbed eigenvalues must converge to a common essential point with a gap immediately below it in the base spectrum. The small positive tail preserves a subgap by the signed Schur complement, and the finite-rank truncation can insert at most its rank there: the compressed resolvent has strictly positive derivative and each ordered eigenvalue crosses the relevant level at most once. For subtraction of the finite-rank negative part, the same gap count works, and the negative spectral subspace has dimension at most the subtracted rank by intersection with its kernel. Taking the modulus thus cannot introduce an increasing sequence from infinitely many negative eigenvalues. The scalar-base reducing-span obstruction works for every c > ||K||; a diagonal geometric tail gives arbitrarily small trace norm. The supplied checker was inspected, not executed, and only illustrates finite witnesses. The proof is analytic, not expert-attested or formally verified.

## originality

PASS

Credit the existing spectral criteria, finite-rank stability and scalar/trace-class obstruction. The supported distinct content is the fixed compact self-adjoint K classification for all positive bases, in particular the unconditional, noncommuting positive-compact implication across multiple essential levels. No inspected statement supplies that implication or makes it an immediate corollary.

## value

PASS

This is a sharp operator-class stability classification, not just a compactness example. Positive tails can have infinite rank and mix distinct essential levels: showing that they nevertheless cannot fill a left-hand essential gap with a forbidden increasing sequence explains precisely what sign information controls universal stability. The scalar obstruction makes that boundary usable and sharp.

The dated certificate retains the supplied scientific assessment, sources and limitations.
