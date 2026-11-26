---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Pass for the frozen numerical claim only. The residual is H_E+4n_E(log ψ); the Euclidean principal curvatures both shift by 2n_E(log ψ) and scale by ψ^−2. Harmonicity of ψ away from punctures gives Ric_g(n_g,n_g)=ψ^−4[−2ψ_nn/ψ+(6ψ_n²−2|∇ψ|²)/ψ²]. On an exact minimal surface the shifted Euclidean curvatures sum to zero, so |A_g|²=ψ^−4(k_1−k_2)²/2. Rayleigh–Ritz with the constant test function gives the continuum bound from the true minimum and mean. Read artifacts/stageF.py and verify_certificate.py and evaluated the archive with independent polar-coordinate code (/workspace/branches/independent_mots.py, not the uploaded programs). At N=800: interior residual 3.897e−11, H∈[0.382773952,0.414861710], sampled Q_min 0.157901353, mean 0.159996228, area 78.538913112; fresh Q agrees with saved Q to 5e−16. At N=400: Q_min 0.157901354 and mean 0.159996107. Independent solves at N=80 and 120 reproduce the reported minima and means to shown decimals. The ADM²-rescaled N=800 statistics are 0.631605411 and 0.639984913. A direct curvature expression on the sampled surface differs near the poles by up to 1.5e−5 from imposing the exact trace-free identity, consistent with the discrete stencils; the verifier integrates only interior samples. The script label ‘enclosure’ is not a certified result: there is no controlled continuum surface/error, and sampled derivative and endpoint estimates are not continuum bounds. Neither exact strict stability nor an outermost or Jang conclusion is certified by this evidence.

## originality

PASS

Pass only for the reproducible archived sampled potential statistics, not for studying or finding stability of individual equal-mass BL horizons in this parameter regime. Pook-Kolb et al. cover the same family and dimensionless point in their normalization, with individual-horizon principal-eigenvalue curves; a curve of λ_1 does not recover either sampled statistic of Q or the archived profile. The exact indexed statistics belong to this same frozen record. No earlier independent exact match for the narrowly worded numerical diagnostics was established by the checks.

## value

FAIL

Reproducibility alone does not make these two stencil-dependent summaries of a single standard parameter point a scientifically needed result. Once normalized by ADM mass, the record lies at the large-separation end of the equal-mass individual-horizon stability sweep in Pook-Kolb et al., which already evaluates the more directly relevant principal eigenvalue; there is no critical transition at the selected point. The frozen work does not provide a new controlled stability bound, a discrimination between competing schemes or outcomes, or a justified use for the extra digits in the potential summaries. It only corroborates an already studied positivity regime, without an exact prior eigenvalue comparison or a continuum error estimate. A value-only change in wording would not supply that missing contribution; a genuine validated bound or motivated comparison would be different scientific work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
