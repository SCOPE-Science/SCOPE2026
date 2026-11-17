---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Overlap-graph vertices (a,b,c) with a!=b,b!=c number q(q-1)^2. Allowed four-edges are (a,b,c,d) with a!=b,b!=c,c!=d,(a,b)!=(c,d); at repeated-endpoint vertices a=c both in/out degrees q-2, otherwise q-1. Each ternary-restricted induced graph is strongly connected; sharing two-symbol repeated-endpoint vertices connects all 3-symbol subgraphs, proving global connectivity for q>=3. Elimination to ordered-pair coordinates splits the Laplacian into a constant, (q-1) standard 2x2 blocks, symmetric row-sum-zero and antisymmetric row-sum-zero components, dimensions totaling q(q-1). Determinants produce the claimed factors x, (x-q+1)^A, Q_q(x)^B and P_q(x)^(q-1). Directed matrix-tree and BEST with unique edge labels yield the all-q expression. Independently constructed Laplacians at q=3 and 4 have exact characteristic polynomials matching factorization; exact arborescence counts are 12 and 49589822592000. Finite checks corroborate but do not replace the invariant-subspace proof.

## originality

PASS

The published November 2 tandem-square-avoidance universal-cycle theorem excludes abab alone, allows adjacent identical letters and has q^3 vertices, hence its exact BEST product does not apply to the present graph with q(q-1)^2 vertices and additional excluded length-two squares. Euler-tour counts are not additive under edge removal. Shur examines globally square-free cyclic words, a different universal coverage question; Alhakim uses square-free in the adjacent-separation sense; Penne appears to concern restricted existence but full text inaccessible. No inspected full theorem gives this precise all-q spectral factorization or product; originality is best of knowledge with Penne explicitly unresolved access.

## value

PASS

Length four is the first local window where a square of length two is present in addition to adjacent-letter squares. Counting every universal cycle for this complete natural restricted language across all q is a substantial exact classification, with a nontrivial overlap-Laplacian spectrum and direct implications for constrained de Bruijn scheduling. The answer is an infinite-alphabet family with motivated object and invariant, not just a finite numeric search.

The dated certificate retains the supplied scientific assessment, sources and limitations.
