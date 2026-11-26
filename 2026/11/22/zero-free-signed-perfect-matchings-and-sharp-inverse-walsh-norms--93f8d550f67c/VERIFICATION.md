---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Independent exact replay used the two-copy disjoint-2-subset graph, row-by-row subset dynamic enumeration, a breadth-first tree gauge, and direct character sums in both directions. It recovered 60 matchings, 20 per edge, pair-extension frequencies 0:60, 4:75, 6:120, 8:60, 10:120, and all the claimed reduced multiplicities. The product expansion gives 60-40|S| plus four times an even sum modulo 8 for any signing, which proves uniform nonvanishing without sampling. The connected graph has a 19-dimensional cut space; switching by a single vertex changes the sign, and cut-equivariance of the reciprocal forces support on the affine all-odd boundary fiber. Chord restriction is bijective on this fiber because a cycle supported on a tree is zero. The direct reciprocal sum scaled by 60 recovered 1343 nonzero values and absolute numerator 557056 over 60·2048. The l1 norm is attained on a delta; the l-infinity norm is attained by taking the signs of the kernel at one output. Orthogonal Fourier diagonalization gives 1/4 and condition number 15.

## originality

PASS

Credit the classical graph descriptions, previously counted unsigned matchings, switching, and Fourier diagonalization. The supported distinction is the universal signed nonvanishing and evaluated complete graph-specific reduced spectrum and reciprocal kernel norms. The closest inspected alternatives change the support object, not just notation.

## value

PASS

The Desargues graph is a natural highly symmetric cubic bipartite support, not a tailored sparse matrix. Invertibility for every signing is not assured by the unsigned count, and the complete spectrum and exact inverse norm quantify sensitivity of recovery to perturbations in different norms. The arithmetic support and exact sparsity are useful beyond a yes/no nonvanishing test, without claiming a general graph-family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
