---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

In the invariant sector y=-x in (0,1), p in (0,1), the SIS equation is pdot=-beta p[y+(1-y)p], hence p<=p0/(1+beta p0t). For kx<1/3, F(y,0)=tanh(y+kx y³)-y<0 from arctanh y>y+y³/3. Comparison with z-dot=F(z,0)/tau yields y>=z~(At)^-1/2, so p<=C e^{-a sqrt t} and py^-2=O(t e^{-a sqrt t}). With w=y^-2 and c=1/3-kx,d=2/15-kx, exact Taylor gives wdot=A-2d/(tau w)-2kp p w/tau+O(p+w^-2). Integrable errors yield w=At-(d/c) log t+K+o(1). Thus y=(At)^-1/2+O(log t/t^(3/2)); the correction and (1-y)p are integrable, giving a finite positive limit for p exp(beta sqrt(2tau/c) sqrt t). Neutral x0=0 is invariant with p=p0/(1+beta p0t). Proof is global for every strict negative-opinion interior initial point under fixed stated parameters.

## originality

PASS

The complete motivating opinion–SIS primary article imposes u0<1 in its main equilibrium theorems; the co-critical u0=1, beta=delta boundary with full negative-opinion sector exact stretched-exponential law and positive prefactor is distinct. General cubic relaxation predicts only part of the opinion power, not model-specific SIS prefactor and signed log correction.

## value

PASS

The simultaneous epidemic and opinion linear critical thresholds give two qualitatively different clearance universality classes depending on initial opinion: strict risk aversion gives e^{-C sqrt(t)} with a positive trajectory-specific amplitude, neutral opinion gives 1/t. The signed log correction flips at kx=2/15; both are motivated, parameter-sharp observations in a natural coupled epidemic system, beyond routine cubic normal form.

The dated certificate retains the supplied scientific assessment, sources and limitations.
