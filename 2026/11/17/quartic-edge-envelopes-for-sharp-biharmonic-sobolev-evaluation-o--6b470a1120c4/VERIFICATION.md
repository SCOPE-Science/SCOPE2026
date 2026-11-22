---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For the zero-mean Kirchhoff Laplacian L=-d^2/ds^2 on a connected finite compact loopless metric multigraph, f(x)=<Lf,g(x,.)> and Cauchy–Schwarz give the exact point-evaluation norm Q(x)=||g(x,.)||_2^2 and equality only along L^{-1}g. Vertex Green functions solve a finite weighted Laplacian with source 1_a-(sum incident lengths)/(2T), and the normalization of edge-integrated quadratic polynomials fixes the additive constant. For an interior point x_t of edge (a,b), the global Green kernel equals (1-t)g_a+t g_b plus a same-edge Dirichlet tent of height ell and minus its mean ell^2t(1-t)/(2T). Expanding its square gives an exact degree<=4 polynomial for every t, not sampled interpolation. Endpoint/cubic stationary roots/flat edges exhaust the extrema. The t^4 coefficient ell^2(ell-r_ab-ell^2/T)/3 follows from the Green-potential resistance identity; Foster trace gives sum 3p_e/ell_e^3=beta_1-1. Bridges give negative leading coefficient, and beta_1>=2 forces some positive one. Independent Neumann spectral zeta checks reproduce Q(0)=T^3/45 and Q(T/2)=T^3/720 for T=1, verifying interval boundary normalization. The inspected checker independently subdivides edges into new Kirchhoff vertices and compares exact rational kernels for finitely many multigraphs; that is corroborative, not a general proof.

## originality

PASS

PASS, qualified: Baker–Rumely gives Laplace Green spectral representations and resistance, but the universal explicit quartic H² evaluation envelope, stationary-point classification, and Foster leading-coefficient law were not present in the inspected full-text material; the stronger first-order H¹ envelopes do not imply fourth-degree integrated-square Green diagonals.

## value

PASS

PASS: the exact sharp H² Sobolev embedding constant for every finite metric multigraph with arbitrary positive lengths is a natural spectral-geometric invariant; reducing continuous maximization to finitely many cubic equations and classifying ALL norming points is substantive. The cycle-rank sign identity makes graph topology visible in quartic curvature and is not a routine restatement of the H¹ case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
