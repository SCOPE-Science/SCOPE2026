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

Hamiltonian equations reproduce the displayed flow; p and V are positive/strictly single-well at k>a², giving unique closed energy ovals and exact physical-time/Euclidean-area quadratures with A_s_prime=T_s. The half-mass F_s(E)=int_0^{r_s}p_s(r)^-1/2 dr has an exact arcsinh primitive. Its signed difference tends to -2/sqrt(k) artanh(a/sqrt(k)); its derivative difference g(u) is bounded near 0 and O(u^-5/4) at infinity, so Abel kernel dominated convergence yields sqrt(E)(T_+-T_-)->sqrt2 int g=B, with the endpoint range O(E^-1/4). Each F_s_prime has 1/(4sqrt(k)u) tail and produces T(E)=log E/(sqrt(2kE))+O(E^-1/2), giving L. Integrating A_s_prime establishes the 2B area constant and 1/logE occupation bias. The exact mass-coordinate potential difference factorization in S=sinh(sqrt(k)z), h=cosh(sqrt(k)z)-1 has sign(a) because 3h²+5h+1+3(a²/k)h(h-1)>0; independent symbolic polynomial reduction modulo S²=h(h+2) verified the factorization. Positive Abel kernel then gives strict all-energy signed area ordering; reflection (x,y,a)->(-x,-y,-a) preserves full period/area, while explicit tanh inverse is global analytic.

## originality

PASS

Earlier same-system work establishes global center, leading fair-sign occupation and even a two-term unsigned total period. None of the inspected full same-model sources provides the finite signed half-period asymptotic B, global strict signed-area ordering or the resulting sign-sensitive analytic inverse; these are the claimed incremental findings.

## value

PASS

The sign of the asymmetry coefficient is intrinsically invisible to every unsigned period/area measurement owing to exact reflection symmetry. An explicit signed residence statistic and strict finite-energy area comparison resolve a natural inverse-identifiability obstruction, adding mathematically motivated sharp information to the model rather than a routine period recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
