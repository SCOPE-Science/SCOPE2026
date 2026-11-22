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

Reduced exact p=1 four-compartment map to probability-preserving F(a,r)=(ea+H(a)(1-a-r),ta+zr); s1 multiplier exp[-(ca+m)]<1 so nonfixed periodic states cannot have s1>0. If a0>a1 in hypothetical two-cycle, subtracting r equations gives r1-r0=t(a0-a1)/(1+z), s1-s0=(1-t/(1+z))(a0-a1); subtracting a equations requires -(1+e)Delta=H(a0)s0-H(a1)s1 >= -(1-t/(1+z))Delta for monotone H, contradiction. For exact H, H/a=c int_0^1 exp[-(ca+m)u]du strictly decreases, giving one positive equilibrium iff e+Hprime(0)>1 (the established R_tau threshold) and global extinction at/below. At endemic equilibrium J=[[A,-h],[t,z]], A=e-h+(1-e)eta with 0<eta<1; Jury factors (1-A)(1-z)+th, (1+A)(1+z)+th and 1-zA-th all positive since zA+th<=max(z,t)<1. Full transverse multiplier exp[-(ca+m)]<1. Independently verified rational nonmonotone H bump cycle exactly (1/2,9/40)<->(1/5,3/10). Does not rule out longer cycles or global supercritical convergence.

## originality

PASS

Best-of-knowledge scope-limited advance beyond the threshold and numerical one-stage stability reported in the original 2026 finite-round competing-risk paper. The no-two-cycle comparison theorem for arbitrary nondecreasing probability incidence and uniform endemic Schur inequalities were not stated in the reviewed original, and related SIS/SIR maps differ in the update law.

## value

PASS

An all-parameter exclusion of the first possible discrete-time oscillatory bifurcation in a natural epidemic map, with a sharp monotonicity boundary witness and exact stability classification, resolves a substantive dynamics gap, not a routine numerical parameter check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
