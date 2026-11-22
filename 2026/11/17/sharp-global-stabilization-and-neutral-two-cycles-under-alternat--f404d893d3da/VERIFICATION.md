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

The reverse triangle inequality | |x|-xi |<=|x-xi| with xi=1/(1+a-b)>0 gives global componentwise error matrices LA=[[ar,r],[b,0]], LB=[[a,1],[bt,0]], L=LB LA>0. Its trace is a²r+b+brt, determinant b²rt<1, and det(I-L)=1-b-r(a²+b(1-b)t). Positivity and determinant <1 imply rho(L)<1 iff r<r*, proving uniform full-plane two-season decay and one-step controlled bound. In positive target neighborhood, the actual return Jacobian Q=diag(1,-1)Ldiag(1,-1), so its Floquet multipliers coincide with L, proving supercritical saddle instability. At r* vectors v=(a,-b(1-b)t), w=(-(1-b),ab) satisfy J_A v=w and J_B w=v; for small nonzero eps both x coordinates stay positive, so affine dynamics agrees with exact nonlinear absolute-value map. Thus an actual nonconstant period-two calendar orbit exists at criticality. Exact rational checks at (a,b,t)=(7/5,3/10,1/2) gave r*=140/413 and the cycle; additional independent floating matrix calculations for other parameters supported, not proved, the algebra.

## originality

PASS

Best-of-knowledge PASS: the model-specific earlier target-oriented control paper provides sufficient one-step and local bounds but does not in the inspected theorem/Lozi sections establish the unrestricted-plane exact two-step threshold or the critical continuum. Prior delayed Lozi recurrence and scalar pulse control concern different map/control classes.

## value

PASS

The exact global stability threshold for feedback that acts on only one coordinate each season is substantively stronger than conservative one-step sufficient control and supplies precise failure dynamics at the threshold. This identifies a natural periodic actuator-scheduling robustness boundary rather than a minor algebraic rearrangement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
