---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For s monochromatic parts there are binom(m,s) choices and (q)_{2m-s} ordered colour injections; conditioning one part to be monochromatic leaves q choices and Z_{m-1,q-1} colourings. Colour symmetry makes each nonzero-frequency block identical, with diagonal 1, opposite-pair entry r=(qp-1)/(q-1), and other entry b=-1/(q-1); cross-frequencies and the constant are orthogonal. The block is (1-r)I+(r-b)P+bJ, with P the block diagonal of 2-by-2 all-ones blocks and J the full all-ones matrix. Its three eigenspaces give exactly the stated levels and multiplicities. At q=m only monochromatic parts occur, giving the stated rank and nullity. For q>m positive definiteness also follows by comparing colourings differing at one vertex that is recoloured to a spare colour: in a vanishing sum of one-site functions, this forces every single-site function to be constant, using arbitrary relabellings of colours. The pair level exceeds the other levels and 1, while conditional coincidence 1/(q-K)>1/q, K the number of colours used on other parts, implies L_anti<1. At q=m+1 the S=0 and S=1 counts are in ratio 1:m, giving p=m/(m+1) and squared condition number 2m+1. Since m-1<=K<=2m-2 at large palette, p=1/q+O_m(q^-2); the total mode is then the minimum and the resulting ratio has coefficient 2m. These are all-parameter algebraic checks; the frozen script was read, not run. The spectrum is for the constant and one-site functions only, not all frequencies of the product space.

## originality

FAIL

No inspected catalogue entry states the cross-polytope numbers verbatim. But a distinct indexed proof already gives the exact general one-site Gram reduction on arbitrary graphs, and the established complete-multipartite chromatic enumerator gives both of the only inputs required here. Their specialization leaves the simultaneous diagonalization of I, the within-pair all-ones blocks and the total all-ones matrix, with routine endpoint counts and comparisons. Same-day catalogue date does not imply priority; the adverse result is based on the mathematical implication, not the date or a title match.

## value

FAIL

The rank and norm control are natural quantitative invariants for one-site interpolation, and the elementary derivation is transparent. On this family, though, the complete spectrum reduces to mechanically using existing general Gram and counting formulas and diagonalizing three commuting all-ones matrices. The rank above the chromatic palette also follows by spare-colour recolouring, and 2m+1 is the direct first-extra-colour substitution. No distinct substantive invariant beyond this specialization is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
