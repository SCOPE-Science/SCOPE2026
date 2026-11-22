---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Computed the map on the matrix units E_ij using the weighted Cauchy dual S'e_j=sqrt((j+2)/(j+1)) e_(j+1) and the positive telescoping projection coefficients. Every matrix diagonal is invariant under the resulting backward bidiagonal operator. The eigenvalue recurrence (lambda-n/(2(n+1)))u_n=(1/2)sqrt((n+2)/(n+1)*(n+d+2)/(n+d+1))u_(n+1) telescopes to u_n=u_0 sqrt((d+1)/((n+1)(n+d+1))) product_(j<=n)(2lambda-1+1/j). For z=2lambda-1 nonzero nonterminating, gamma ratios give |u_n|~const |z|^n n^(Re(1/z)-1). Therefore all |z|<1 occur; |z|>1 do not; on |z|=1 the l2 criterion is Re z<1/2, including z=-1 as a terminating special case. Nonnegative and negative matrix diagonals are orthogonal, and one nonzero eigenvector per diagonal implies infinite geometric multiplicity. No statement about entire spectrum. Independently checked 275 finite exact recurrence identities across d=0..4, five rational z choices and 11 steps, which validate algebra but not the infinite square-summability proof.

## originality

PASS

Panja 2026 defines exactly the underlying UCP map on the Bergman space, identifies bounded-operator fixed points and proves compact fixed-point exclusion, which only settles lambda=1 among these Hilbert–Schmidt candidates. The full boundary eigenarc and every non-fixed point eigenvalue require the diagonal recurrence and gamma asymptotics and were not stated in the inspected primary source. General weighted backward shift eigenvector theory is mathematical groundwork; a theorem specialized to this exact coefficient sequence may still exist but was not found in searched material.

## value

PASS

For the natural operator whose harmonic-symbol Toeplitz fixed-point structure is known, a complete Hilbert–Schmidt eigenvalue classification with a strict, nontrivial partial-circle boundary is a useful spectral invariant. The infinitely degenerate admitted eigenvalues contrast sharply with compact fixed-point rigidity and identify an actual summability transition, not a routine numeric lookup or arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
