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

The source RESULT gives the complete b,d,c>0 symmetric two-patch ODE, states hyperbolic stability only of the two pure corners and the unique anti-diagonal interior fixed point, and excludes zero-eigenvalue endpoints. The pure-corner Jacobian has eigenvalues -b/2-d±sqrt(d^2+c^2), giving c<C0=sqrt(b^2/4+bd). Writing x=(1+m)/2, y=(1-m)/2 gives H(m)=(1-m^2)(bm+2c)-8dm, with exactly one positive root in (0,1) by Descartes signs and endpoint crossing; the root increases with c. The mixed Jacobian eigenvalues are alpha(m), alpha(m)-2d, alpha=b(1-m^2)/4-4dm^2/(1-m^2), strictly decreasing. Its zero yields C1=sqrt(bd)/2*(4-sqrt(4+b/d)). Intersecting strict inequalities gives max(0,C1)<c<C0, or max(b/2,C1)<c<C0 under robust opposing local margins. The exact b=3,d=1,c=23/12, m=1/2 stationary witness and mixed eigenvalues -37/48,-133/48 independently check. The b/d=9/4 comparison follows by solving C1=b/2. No basin, additional equilibrium, or boundary classification is proved.

## originality

PASS

The exact stability wedge is an explicit sharp finite two-patch classification not supplied by the qualitatively related PDE/backward-bifurcation literature. The physical phenomenon of mixed and pure simultaneous attractors is not claimed new. No retrieved Resultary earlier record states these three particular ODE equilibria and both exact thresholds; that unsuccessful search is not proof of priority.

## value

PASS

An analytically sharp and explicitly nonempty parameter wedge for three specified hyperbolic sinks, plus the b/d=9/4 point where mixed-state stability becomes automatic, is a motivated bifurcation boundary in a natural symmetric migration-selection model, beyond a routine Jacobian evaluation because the interior equilibrium must be eliminated and quantified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
