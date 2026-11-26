---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For two regularly separated endpoints x=cv−su, y=cv+su, the angle tests give |u·z|<s and v·z<c. Uniform projections have constant density 1/2 on [−1,1], and the excluded cap is in the belt except on a null boundary. Coincidence gives zero, agreeing with K, while at antipodes strict acuteness has probability zero rather than K=1/2. With probability normalization the Funk–Hecke eigenvalue is half the Legendre integral. Shifted Rodrigues and integration by parts against u^(1/2) give the displayed gamma ratio; the vanishing factor u^ℓ(1−u)^ℓ makes the boundary terms zero. Alternatively Eq. (27) of Brauchart–Dick gives all coefficients directly after parity rescaling. Each degree contributes 2ℓ+1 modes, and absolute uniform convergence follows by bounding each degree block by (2ℓ+1)|λℓ|. The exact deficit is valid for arbitrary Borel μ; harmonic density separates μ from σ, and only antipodal pairs require a correction. The degree-one Hoeffding projection (order one, not harmonic degree one) vanishes by rotation invariance; the pair sum enters with factor n−2 and the canonical triple remainder has variance O(n³). A finite harmonic CLT plus the canonical pair L² tail bound gives the factor 1/2 in the chaos. The diagonal gives trace 1/2; positive probability of a small finite partial sum and independently small tail gives the sharp upper support endpoint, and an unbounded chi-square term gives no lower bound. Direct integration gives the squared norm (π−3)/8 and thus variance (π−3)/16. Replay: python /workspace/audit_checks/reconstruct.py 5 checks the first ten integrals and the cross-term exactly. The frozen numerical checker was inspected, not executed; the asymptotic and uniqueness conclusions rely on analysis.

## originality

FAIL

The exact signed spectrum is mechanically implied by an explicit earlier Euclidean chord-distance expansion, not just by a general qualitative negative-type result. Put D(x,y)=||x−y|| and let R act by y↦−y. The previously reported acute conditional kernel (credited in the frozen finding) yields h=(1/2)D+(1/4)DR−1 as kernels. Brauchart–Dick, arXiv:1203.5157v1, p. 12 equations (25)–(27), with d=2, s=3/2, gives the eigenvalues ρℓ=(4/3)(−1/2)ℓ/(5/2)ℓ=−4/[(2ℓ−1)(2ℓ+1)(2ℓ+3)] for ℓ≥1, where the ratios denote rising factorials. Multiplying by (1/2+(-1)^ℓ/4) gives precisely the claimed λℓ. Integrating the known convergent expansion gives rigidity by the positivity of that multiplier, with the direct right-angle observation at antipodes providing the atomic correction. Plugging that same spectrum into the standard order-two canonical limit gives the full displayed law, and its support statement follows immediately from the signs and finite trace. This is a concrete prior-implication finding, not a claim that an older article states the complete acute-triangle result verbatim or that an inaccessible source proves it.

## value

FAIL

The triangle statistics are natural and the acute formulation is useful exposition, but the new-looking exact weights are a parity reweighting of prior coefficients, the arbitrary-measure correction is the direct diameter/right-angle exception, and the limit and endpoint are routine consequences with those known inputs. The frozen record does not add a separate substantive estimate, classification, or theorem that survives this reduction and warrants repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
