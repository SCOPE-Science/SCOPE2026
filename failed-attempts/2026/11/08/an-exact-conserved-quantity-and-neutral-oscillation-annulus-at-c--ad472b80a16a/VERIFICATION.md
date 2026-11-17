---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PASS. At the critical linear feedback u=m/n, s=log(r/(1-r)), Y(x)=1/Gamma(x), a=nc/epsilon and qcoeff=nb/epsilon, the exact source equations yield dot Y=(aY-qcoeff sigma(s)) dot s. Differentiation shows d/dt[e^{-as}Y+qcoeff integral_{s*}^s e^{-av}sigma(v)dv]=0 identically in (0,1)^2. Gamma has one strict interior maximum at x*=m/(m+n), and the conserved H has a positive-definite diagonal Hessian at (x*,r*), giving regular compact ovals via Morse lemma and periodic nonattracting flow there. Direct Jacobian product gives omega²=mc(1-r*)/((m+n)epsilon), hence period limit 2pi/omega. Independent exact symbolic cancellation and scale transformation to previous invariant checked; universal claim established analytically, not by sample trajectories.

## originality

FAIL

FAIL by decisive earlier coverage, not missing access. An earlier 2026-11-02 published Resultary finding First integral and sharp orbit–extinction separatrix in a collective-risk feedback game proves the same critical System I for all matching integers/parameters and obtains the SAME invariant up to multiplication by b: its I(r)=exp(-as) and h(x)=b Gamma(x), so b*[I(r)/h(x)+(n/epsilon)integral_{r*}^r I(z)/(1-z)dz] = exp(-as)/Gamma(x)+(nb/epsilon)integral_{s*}^s exp(-av)sigma(v)dv, exactly current H. It also proves a stronger entire-interior energy trichotomy and periodic annulus; the present local center and small-period linearization are elementary consequences. Full earlier RESULT.md read and formulas compared; title/parameter overlap is not the basis of rejection.

## value

FAIL

FAIL as a distinct final research finding because the exact conserved quantity, entire neutral periodic annulus, and nonisolated-cycle contrast are explicitly proved in the earlier stronger same-model work. The small-amplitude period is the routine eigenfrequency at the same equilibrium and does not constitute an independently motivated surviving new exact invariant. Mathematical correctness and model significance were recognized, but this restatement adds no distinct substantive result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
