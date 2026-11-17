---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For every integer d,q>=3 the RK4 heat endpoint is a degree-four polynomial in the combinatorial Hamming Laplacian. The distance-regulated adjacency recursion yields exactly four nonzero offdiagonal shell types. The distance-three entry is h^3(1-h/h3) and becomes negative for all h>h3; distance-four entry is h^4. The diagonal is positive because the scalar degree-four exponential Taylor polynomial is positive for all nonnegative Laplacian eigenvalues. The displayed Bernstein-basis identities for distance-one and distance-two shell polynomials imply nonnegativity throughout [0,h3] for d>=4 and for d=3, q<=12. At d=3, q>=13, the last degree-three Bernstein coefficient (64-5q)/(81q) is negative; via t/(1-t) the cubic has exactly one positive root (Descartes), so the adjacent entry crosses once before h3. I independently reconstructed Hamming adjacency and Laplacian powers and checked at d,q=(3,12),(3,13),(4,3),(7,13): the distance-three entry vanishes exactly at h3, is negative just beyond, while distance-one at h3 changes from +1/4374 at (3,12) to -2/41067 at (3,13), as claimed. The all-parameter assertions rest on exact positive symbolic Bernstein coefficients, not finite tests. Row-sum one follows from L*1=0. Spectral stability alpha/(dq) > h3 follows from Laplacian eigenvalues jq and alpha>2.

## originality

PASS

PASS best-of-knowledge: earlier universal SSP positivity restrictions, general numerical positivity-step theory, and absolute monotonicity do not give a sharp end-step positivity threshold on this Hamming graph family. Related exact RK4 results on paths, bipartite graphs, complete multipartite graphs and directed cycles are for different graph structures; the Hamming product q>=3 has distance 3 and 4 shell constraints not implied by those formulas. The recent Radau IIA Hamming-family theorem concerns a different time integrator. An actual Resultary search and a complete primary Horváth 2005 text/SSP references did not reveal an implication of the precise q=13 boundary. Residual risk from unavailable historical specialist numerical-analysis full text remains.

## value

PASS

End-step nonnegativity is the exact Markov/diffusion property needed for nonnegative data; scalar RK4 spectral stability alone is insufficient. A complete sharp horizon for an infinite canonical graph family and discrete switch of the first negative transition at q=13 is a substantial structural classification, not a routine SSP substitution or single test case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
