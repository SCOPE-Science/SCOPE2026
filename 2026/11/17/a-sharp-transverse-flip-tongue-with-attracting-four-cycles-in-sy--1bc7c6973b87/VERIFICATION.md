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

In symmetric mean/difference coordinates s,v the equal-growth two-species Ricker map has even s and odd v components. The synchronous two-cycle a=h(d)-d,b=h(d)+d is exact and positive; longitudinal multiplier m=1-2h+Q has |m0|<1 at d0=2arsinh(1). The transverse multiplier mu=1-2kh+k^2Q obeys mu+1=-Delta, with Delta=sinh^2(d/2)-1-Q(k-k*)^2. Its zero set gives both physical square-root branches. For G=F^2, solving G(s,v)=S(s,v) using the even-coordinate implicit function gives the reduced odd equation -Delta+gamma(d,k)v^2+O(v^4)=0. Explicit composition gives gamma0≈2.18375756345>0; hence unique nearby exchange-related v=±sqrt(Delta/gamma0)[1+o(1)] precisely when Delta>0. This produces one primitive four-cycle by phase separation and G switching the unequal states. The derivative of H=S∘G has slow eigenvalue 1-2Delta+o(Delta) and fast eigenvalue ->m0, proving local attraction. Finite numeric examples corroborate but do not prove the IFT classification.

## originality

PASS

Earlier Ricker competition work includes period-four out-of-phase mode plots and a general synchronous-cycle Floquet reduction, which covers qualitative phenomena and exact linear multipliers. The present nonlinear analytic codimension-two cusp, gamma0 sign, local uniqueness/supercriticality and exact square-root tongue width require new higher-order calculations not supplied by the inspected numerical modes or linear spectral theorem.

## value

PASS

Resolves the local bifurcation type and stability of an observed dynamical mode using a nontrivial explicit cubic coefficient; produces an exact two-parameter tongue, sharp square-root opening and local uniqueness. These explain whether the synchronous attractor is replaced by an attracting off-diagonal primitive-four orbit, a motivated dynamical question unanswerable from linear Floquet data alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
