---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For f(S)=(−1)^|S|, its Boolean Möbius transform at C is the binomial sum (−2)^|C|. Every subset of A∩B is retained by downward closure, so the exact integral congruence is H=Z diag((−2)^|C|) Zᵀ with Z the unit lower-triangular incidence matrix. Unimodularity, changing signs and sorting by cardinality give the divisibility chain 2^|C|. The same congruence gives the signed determinant and Sylvester inertia. Multiplying the two Boolean inverse-zeta entries and summing over C⊇A∪B gives the stated inverse, including its sign. Invertible basis changes persist modulo 2^r; the one-coordinate kernel of 2^k has 2^min(k,r) elements. All factors are units modulo odd integers, and at n=0 the singleton ideal gives [1].

## originality

FAIL

The principal Walsh matrix is exactly a classical meet matrix: take the Boolean meet-semilattice, the downward-closed family, and the weight f(S)=(−1)^|S|. The standard integral incidence factorization and meet-matrix inverse specialize with the single binomial transform (−2)^|C|. Because those diagonal moduli already divide one another in face order, the Smith and modular conclusions require no additional structural theorem about Walsh matrices.

## value

FAIL

The exact modular sample count is useful information, but in this scope it is a routine coordinatewise consequence of a classical incidence diagonalization specialized by the binomial theorem. The finding does not address stability, unequal row and column supports, or another nonmechanical sampling invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
