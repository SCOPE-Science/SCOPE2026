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

Hamiltonian F=x^2+y^2+k x^2 y^2 is conserved; its regular energy ovals are traversed with original-time T(A)=4K(-kA^2). Vertical area integration gives S(A)=4/k((1+kA^2)K(-kA^2)-E(-kA^2)); differentiating independently yields S′(A)=A T(A). Area sampling makes Pr(A_R<=a)=S(a)/S(R), T strictly decreasing gives exact tail; T(A)~4log(sqrt(k)A)/(sqrt(k)A) and S(R)~4Rlog B/sqrt(k) imply A_R/R=>Uniform(0,1) and normalized T=>1/U. The exact moment integral S(R)^(-1)int_0^R aT(a)^2 da gives E[Z_R]~(log B)/3. Independent mpmath direct vertical integrals and derivatives checked at (k,A)=(.6,2.3),(1.5,17), not used to infer the limit. The geometric and integral arguments prove all fixed k>0, A,R>0.

## originality

PASS

The period and elliptic asymptotics were previously derived for the same flow; area-sampled cross-orbit period distribution and its mean growth are the additional bounded claim. The published single-orbit time-occupation theorem has a different sampling space. General Hamiltonian action identities plus regular variation are credited, not claimed new. No inspected published theorem provides the exact uniform-area ensemble or its divergent coefficient. Priority remains best knowledge, not established by failed searches.

## value

PASS

Area sampling of invariant energy sublevels is a natural canonical measure; a Pareto limiting period with divergent mean is a meaningful distinction between typical orbital time scale and its expectation, sharper than a period calculation or elementary reparameterization. A researcher studying transport/ensemble statistics can use the exact finite-size law and moment coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
