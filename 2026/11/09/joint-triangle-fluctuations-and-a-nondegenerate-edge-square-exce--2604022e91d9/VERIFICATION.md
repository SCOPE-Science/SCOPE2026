---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Exact threshold-graph identities E_m=Σ(j−1)X_j and T_m=Σ_{j<k}(j−1)X_jX_k, centered expansion with quadratic R_m=O_P(n²) via maximal partial sums, and stationary finite-state irreducible aperiodic length-M urn process establish a martingale invariance principle. Transfer by weighted Riemann sums gives Gaussian stochastic integrals for e_n and t_n with kernel pair 2s and 6ρ(s−s²/2). Independently evaluated exact Itô covariance integrals 4/3, 5ρ/2 and 24ρ²/5, determinant 3v²ρ²/20, and delta-method excess variance (2/15)ρ²v. Checked stationary Pólya window law and innovation variance exactly for M=1..4. All M and n→∞ follow from fixed-memory functional CLT, not simulation. Note v=ρ(1−ρ)[1+2Mδ+M(M−1)δ²/(1+δ)].

## originality

PASS

PASS qualified: finite-memory edge-only Gaussian CLT and exact D_M were previously established; no new originality assigned to the edge marginal. The novel joint triangle fluctuation and nonzero residual after subtracting edge-density square are not implied by the old edge-only limit, requiring a distinct weighted quadratic motif projection.

## value

PASS

The exact positive Gaussian residual distinguishes joint triangle geometry from the square of edge density in a natural stationary finite-memory dependent threshold graph; explicit dependence on ρ,M,δ and a nondegenerate two-dimensional covariance matrix provide a useful fine-scale motif classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
