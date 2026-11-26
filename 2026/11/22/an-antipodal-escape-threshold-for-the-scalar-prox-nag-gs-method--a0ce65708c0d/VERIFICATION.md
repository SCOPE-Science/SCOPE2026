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

Source Algorithm 1 allows positive h and alpha; gamma_0=h gives gamma_n=h and equal couplings a=alpha/(1+alpha). Its deterministic quadratic-plus-L1 update is the stated soft threshold. Near zero the proximal input lies strictly in the dead zone, and once v=0 and x sufficiently small, x is multiplied by b on each further step. Globally the threshold subtracts a bounded perturbation of magnitude at most theta from the smooth linear update. The smooth determinant is b^2, with trace 2b+a^2(1-k); the Schur inequalities reduce to 1-b^2, a^2 k, and a^2(k_*-k) all positive, so summable powers and bounded input give all-start boundedness below k_*. An antipodal orbit forces v=-c x and, after selecting x>0 by oddness, the active threshold equation a(k-k_*)x=theta. It has the unique positive solution exactly in the supercritical regime. On the positive-sign cone x>=X and v=-cx-w, w>=0, the explicitly positive input gives x^+=-x-aw and w^+=a(k-k_*)(x-X)+(b^2+a^2(k-k_*))w. The sign-reversed cone follows by oddness. The two-dimensional displacement matrix has strictly positive entries and characteristic polynomial negative at 1. Every nonzero nonnegative displacement thus has a positive Perron projection with expanding eigenvalue >1 and its x-displacement grows exponentially. On the prescribed diagonal x_0=v_0=R, x_1=R and the negative active threshold yields v_1=(1-ak)R+theta<-cR for the stated R; ak_*-2/a=2b^2/a>0. This verifies entry with nonzero displacement and alternating divergence.

## originality

PASS

The map is from source Prox-NAG-GS and its linear Schur inequality matches the smooth NAG-GS mode, which are both prior inputs. The supported distinct claim is a nonlinear local-versus-large-start split across that frontier for positive L1, with an exact finite-amplitude antipodal cycle in its stated class and diagonal escape. The closest inspected scalar bifurcation records concern other maps, and the closest method theorems cover a smooth mode or a stricter sufficient composite convergence range, not the nonlinear claims here.

## value

PASS

A canonical scalar strongly convex quadratic with positive L1 exposes an optimizer-specific failure mode: local exponential attraction across the entire parameter range coexists with exponentially escaping admissible starts beyond a sharp frontier. The cycle amplitude, exact invariant cone and prescribed diagonal starts make this a reusable stability benchmark; it is stronger than a matrix-instability example with unrestricted momentum initialization or a numerical observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
