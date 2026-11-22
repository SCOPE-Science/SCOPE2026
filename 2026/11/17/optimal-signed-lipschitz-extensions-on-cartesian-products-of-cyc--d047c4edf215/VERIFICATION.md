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

For k>=2 cycles of lengths n_i>=3 with unit shortest-path metrics, triangle inequality requires R>=D/2. A bounded real-linear one-point extension must have coefficient sum one; its norm is max(1,rho(w)/R). Averaging signed distance potentials across all x gives rho(w)>=c=sum floor(n_i²/4)/n_i, attained by uniform positive weights. If equality rho(w)=c holds then all S_x(w)=c; for any negative coefficient at z, select a vertex x at graph diameter D from z and increase only f_x(z)=-d(x,z) by small epsilon. Every adjacent edge remains 1-Lipschitz but its functional improves strictly, contradiction: all exact minimizers are positive. For positive w, rho(w)=max_x S_x(w). Additivity of distances means all S_x constant exactly when each factor marginal has constant cycle-distance convolution; cyclic second differences force odd marginal uniform or even marginal antipodally equal. Independent factor constraints yield affine dimension N-1-sum_odd(n_i-1)-sum_even(n_i/2), and strictly positive uniform weights ensure relative interior. For R>c, the rho sublevel set contains a full-dimensional open neighborhood of uniform weights and a negative coefficient via a four-cell zero-marginal checkerboard followed by a small signed transfer. Independently computed c and affine dimensions: (3,4): N12,c=5/3,dim7; (4,4): N16,c=2,dim11; (5,6): N30,c=27/10,dim22; (3,4,4): N48,c=8/3,dim41. Finite LP code inspected; analytic proof covers all k and lengths.

## originality

PASS

PASS best-of-knowledge for the complete joint signed equality-polytope classification for products of at least two cycles, not for the earlier general vertex-transitive optimum norm. The full published single-cycle theorem exactly supplies each factor equality constraint but not the positivity of general correlated signed couplings, independent cross-factor geometry, dimension, or sharp signed transition for products; a potential general tensorization theorem is retained as priority risk.

## value

PASS

Classifying all optimizers of an actual nonunique Lipschitz extension problem is a natural structural question in Lipschitz-free transport geometry. Arbitrary correlated couplings on product cycles form high-dimensional optimizer polytopes, and the sharp crossing to signed full-dimensional solutions at R=c is a meaningful qualitative change. These are mathematically useful even though the optimal numerical value itself follows from transitive averaging.

The dated certificate retains the supplied scientific assessment, sources and limitations.
