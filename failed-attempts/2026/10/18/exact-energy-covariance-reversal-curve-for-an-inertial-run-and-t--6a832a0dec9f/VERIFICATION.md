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

The damped drift is Hurwitz for every g>0, giving the unique bounded stationary solution by convolution with the stationary two-sided chain; sign symmetry gives zero first moments and the stationary q² identity gives E[qp]=0. The signed generator contributes −2ρ, not −ρ. As a check on the proof-critical mixed moment, put B=1+2gρ+4ρ² and let x=L21, y=L12. Eliminating L30 and L03 gives a x−2y=M20 and 2d x+e y=3M02 with a=g+2ρ+3/(2ρ), d=3g+2ρ and e=3+d(2g+2ρ). Their determinant is ae+4d>0. The unweighted fourth-order equations eliminate M13 and M04 to give g(3g²+4)M22=(3+3g²)x+(5g+2ρ)y. Substituting M20=(g+2ρ)/(gB), M02=2ρ/(gB) gives the displayed M22; equivalently, with D3=2ρ(ae+4d) and N as in RESULT.md, NB−(g+2ρ)(3g²+4)D3=−2gP, the exact subtraction needed for the covariance. Strictly positive ∂ρP, ∂gP and the sign of P(g,0) give the unique decreasing threshold. The factorization P(0,ρ)=(12ρ²−1)(4ρ²+9) checks the first endpoint; continuity and monotonicity give the other, both only as limits. The two energy prefactors multiply to a⁴/(4k²). Replay: RESULT.md lines 33–84 and the two-equation elimination above. The supplied symbolic script was inspected, not executed; its algebraic and rational-instance checks are not separate external attestation.

## originality

FAIL

A distinct indexed Resultary record (66ee9dbaa5a1) demonstrably covers the entire substantive result. Its two parameter renamings u=ρ and μ=k, and its physical rather than normalized covariance prefactor, give the identical rational covariance, quartic and global threshold classification including both endpoint limits. Its degree-four numerator is also identical. This is not the frozen record itself: the stable ID, title, Findings, organization and supporting-script reference differ. The displayed catalogue dates do not determine discovery order or priority. The failure is demonstrated equivalent coverage and lack of a distinct supported contribution, not a priority or provenance accusation. No separable novel remainder in the frozen claim warrants repair.

## value

PASS

As a mathematical question, whether kinetic and potential energies have either correlation sign despite zero linear position–velocity correlation is independently motivated in this standard nonequilibrium model. A sharp phase boundary with a global damping threshold and monotonicity gives more insight than moments at a few parameters. This value of the result itself does not make a duplicate an admissible new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
