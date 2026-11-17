---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The system is strongly cooperative for delta>0, strictly sublinear because u/(m+u)-hu decreases strictly for u>0 when m>=1/h, and bounded by a logistic scalar comparison. Its zero Jacobian L has det=delta(e-s)-es and Perron sign positive below delta_c (or always if e<=s). Strictly ordered scalar multiples yield uniqueness and attraction of the one positive equilibrium via monotone comparison. Negative Perron root gives exponential decay with positive left eigenvector. At delta_c weighted mass a*u+v decreases at least s*v^2; integrability and uniform continuity force v->0 and u->0, so the center-stable decomposition X=z(a,1)+w(1,-a) yields w/z->0 and zprime=-k z^2+o(z^2), k=[s+a^3(h-1/m)]/(1+a^2)>0; hence the universal physical-time t^-1 profile. Lyapunov–Schmidt projection gives alpha=(1-a)^2/(1+a^2) and branch slope alpha/k. Boundary m=1/h remains quadratic via the v component.

## originality

PASS

Best-of-knowledge novel exact result after checked primary source scope comparisons. The closest inspected primary results differ by parameter regime, sample law, or strictly weaker quantitative conclusion; inaccessible full texts and independent historical priority remain explicit risks.

## value

PASS

A high-Allee patch is a strict sink alone; equal migration can rescue or destroy persistence. The full sharp classification fills the original source model’s missing parameter ranges, while the global critical t^-1 law and branch slope quantify a biologically natural extinction transition, not an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
