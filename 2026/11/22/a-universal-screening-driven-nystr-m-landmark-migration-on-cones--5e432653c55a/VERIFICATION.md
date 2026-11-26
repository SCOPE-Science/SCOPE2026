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

The constant and hub/base contrast modes give cone eigenvalues 0 and m+1; the orthogonal mean-zero base modes have eigenvalues b_j=1+ν_j. Walk-regularity implies regularity and constant diagonal of all Laplacian spectral projectors by polynomial interpolation in the adjacency matrix. Thus the peripheral resolvent diagonals r, and their derivatives, are independent of the vertex. The hub diagonal is h=(μ+1)/(μ(μ+m+1)); computing each peripheral projector weight gives r/h=1+Σ c_j μ/[m(μ+1)(μ+b_j)]. The complement identity on the mean-zero space gives c_j≥0, with some positive unless the base is complete. The ratio is strictly greater than 1, and the error difference E_p-E_o is (log(r/h))′ by K′=-K². The derivative of the ratio is Φ/[m(μ+1)²]; each nonzero term of Φ has derivative -2c_j b_j(μ+1)/(μ+b_j)³ and the sum changes sign from positive to negative. This proves the unique global switch, all tie cases and the square-root bounds (strict for multiple contributing values). The conditional covariance block is the inverse of the retained principal precision matrix by the Schur complement, verifying the screened grounding interpretation. For cycles C₄ only ν=2 contributes, yielding √3. For growing cycles, with f=(1+ν-μ²)/(μ+1+ν)², the full periodic sum yields Φ/m²=I-(f(0)+J)/m+O(e^{-cm}), uniformly near the limiting root (the summands are analytic in a common strip). Setting Y=μ+3-2cos θ gives f=1/Y-μ(μ+1)/Y², so integration and differentiation give I=(μ+1)(5-2μ-μ²)/[(μ+1)(μ+5)]^{3/2}. Also J=1-μ(μ+1)/√[(μ+1)(μ+5)]-(μ+1)I. At x=√6-1 the root is simple, I′(x)=-2(x+1)²/D^{3/2}, so the first correction is (f_x(0)+J(x))/I′(x), precisely the stated positive γ (the sign reduces to 57>22√6). Root localization follows from opposite signs on both sides of x and uniqueness; Taylor expansion gives the O(m⁻²) remainder. Replay: RESULT.md proof steps 1–4. The supplied finite checker was inspected, not executed.

## originality

PASS

Credit the standard Nyström, inverse-trace leader and conditional covariance formulations. The best-supported distinct result is the unique uniformly screened switch on all qualifying cones and its wheel correction, not the first discovery of hub/periphery migration under any tuning or a new objective.

## value

PASS

The result gives an exact optimizer for a natural resolvent model and a systematic failure of the largest-diagonal heuristic, not an isolated small graph. It gives a spectral threshold requiring only the base eigenvalues and a sharp first size correction for a canonical family. The interpretation applies only to the one-landmark trace objective, not arbitrary loss or landmark counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
