---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The two branches map into disjoint opposite sides of b, avoiding the switch at all iterates after the first. The left two-step map is rC_q on [0,1], strictly increasing, mapping into (0,1); its iterates converge monotonically to fixed points, each representing a distinct primitive two-cycle. The strict log-concavity of C_q′, with C_q′ vanishing at both endpoints, gives one peak and hence exactly one minimum of H_q=C_q−uC_q′. Direct differentiation gives ∂_q H_q<0 in the interior. At s tan s=1, the normalized decreasing single map f_q(u)=q cos(πu/2) fixes u*=2s/π with derivative −1 at q*=2/(π sin s), so G=f_q² has G′=1 and G″=0 there. Also s>π/4, hence q*<1. This is the unique zero minimum of H, and the two simple zeros above q* produce the stated horizontal-line census including clipping by r<1. At roots the multiplier is 1−H_q/C_q, checking outer attraction, middle repulsion and neutral folds; the folds have nonzero second derivatives. At the cusp the cubic coefficient is −(π²/4)(1/3+s²/2), from Taylor composition; the parameter unfolding is transverse since the determinant for (G−u,G′−1) in (q,r) there is r C_q′ ∂_q H_q≠0. For all nonfixed critical initial returns strict monotonicity preserves the sign of the error, and the inverse-square increment gives the claimed signed relaxation. On r=q>q*, the single-map fixed point has slope magnitude A z tan(Az)>1, which together with endpoint signs gives three roots, persisting locally. Even-iterate limits in the two branches and dominated convergence force invariant measures to be supported on the finite set of cycle points; one-step invariance assigns equal weights within each pair.

## originality

PASS

The cosine branches and general cusp mechanisms are prior. The exact cusp point, fold census over the full strict-alternation region, and critical coefficient for these cosine branches are distinct from the closest inspected claims.

## value

PASS

For a documented oscillator map the result replaces numerical pictures with a global orbit and invariant-measure classification and an exact curve of robust coexistence. Identifying all admissible folds and the exact slow relaxation at the critical point adds information not supplied by the bare observation that monotone returns converge or by analogous polynomial examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
