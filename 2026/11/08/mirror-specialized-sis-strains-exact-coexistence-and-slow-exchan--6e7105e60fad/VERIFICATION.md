---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For the exact two-patch mass-action six-ODE model with 0<a<b, equal migration d>0 and mass N=2, stationarity of patch totals gives one mass per patch. Vanishing determinants of the two positive Metzler infection matrices subtract to (1+d)(b-a)(s1-s2)=0, so s1=s2. The unique positive Perron zero of L(s), increasing on [0,1], exists precisely if Lambda(d)>0; second determinant root cannot have positive Perron vectors. Equating per-patch infected mass forces equal strain amplitudes and unique (p,q,q,p). Linearization splits even/odd Hurwitz 2x2 blocks with negative trace and positive determinants, plus eigenvalue -2d on fixed total mass; this proves local, not global, attraction. As d grows with a+b>2, the odd slow eigenvalue is -[(b-a)^2(a+b-2)/(4(a+b)^2)]/d+o(1/d); the other slow even eigenvalue stays bounded negative. For a+b<2,b>1 the invasion cutoff is d_c=(b-1)(1-a)/(2-a-b), strict. Independently differentiated full six equations at a=1/2,b=3,d=3/2 and obtained residual zero and exact characteristic polynomial z(z+3)(8z²+34z+5)(8z²+34z+29)/64. Critical a+b=2 strong migration asymptotics not claimed.

## originality

PASS

The same-equations initiating 2023 source only supplies sufficient coexistence criteria, raises uniqueness/stability as future work, and does not give mirror Perron-root iff cutoff or the d^-1 strain-exchange coefficient. Later continuous-space and constant-transmission-ratio results overlap SIS epidemiology but are not established to imply the same parameterized finite-patch theorem. Best-knowledge priority retains inaccessible-PDE/full-literature risk.

## value

PASS

A natural analytically solvable heterogeneous two-strain spatial SIS benchmark resolves an existence/uniqueness/local-stability gap, identifies exact migration viability boundary and proves near-neutral strain-composition relaxation despite strong spatial mixing. The sharp slow rate is not a routine threshold substitution and is relevant to coexistence timescales.

The dated certificate retains the supplied scientific assessment, sources and limitations.
