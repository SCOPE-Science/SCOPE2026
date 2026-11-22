---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The full degree<=2 polynomial band restricts uniquely to edge Walsh coefficients h_i+h_j, ell_i s+ell_j t, gamma_ij st, with dimension 2d+C(d,2). All-edge Walsh orthogonality and triangle equations prove injectivity. For support<=4, a nonzero linear odd component yields at least 2r(d-r)+C(r,2)>=6 supported values. The even part induces an edge set F of at most two nonzero pair sums. Deleting <=2 edges from K_d leaves connected nonbipartite graph for d>=5, and at d=4 only deletion of a perfect matching leaves a four-cycle. Thus h=0 normally, yielding C(d,2) complete coordinate squares, while d=4 yields 3*2*2=12 further matching antipodal-pair unions, exactly 18 supports. The supplied exact Bareiss checker of 12950 d=4 erasure patterns was inspected as code, and the proof is independent of finite tests.

## originality

PASS

Best-of-knowledge novelty assessment from actual statement-versus-implication comparisons and the indicated primary source reading, with stated residual risks.

## value

PASS

Four-erasure minimum distance and its exact supports determine the sharp minimum pattern of deterministic reconstruction failure for a standard root-system harmonic sampling design. The dimension-four 24-cell exception is a structural K4 cycle phenomenon, not an arbitrary finite slice, and the classification covers all d>=4.

The dated certificate retains the supplied scientific assessment, sources and limitations.
