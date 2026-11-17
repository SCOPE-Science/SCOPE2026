---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Reduce the full-space relaxed operator on each nontrivial principal-angle plane to B=[[1−omega*s²,0],[omega*c*s,1−omega]] (or transpose), with remaining scalar blocks. Compute I−BᵀB=omega[[s²(2−omega),−cs(1−omega)],[-cs(1−omega),2−omega]] and determinant omega² s²((2−omega)²−c²(1−omega)²). PSD for all blocks holds iff 0<=omega<=(2+c)/(1+c). Norm of the first column is sqrt(c²+(1−c²)(omega−1)²), so the unique minimizer of ||T−P|| is omega=1, min c. The known asymptotic spectral optimizer 2/(2−c²) crosses safety when c³+2c²−2 changes sign, giving one root 0.839286755... . Independent exact symbolic Gram identity and rational 2x2 tests corroborated the calculations; the all-angle proof is analytic.

## originality

PASS

Best-of-knowledge: primary Bauschke et al. (2014/2016) gives the identical T_omega=(1−omega)I+omega P_U P_V, principal-angle canonical block and asymptotically optimal parameter 2/(2−c²). Its theorem 3.6 compares spectral rates, not the exact full-space Euclidean norm for one step. The sharp nonexpansive interval 0<=omega<=(2+c)/(1+c), unique norm-minimizer omega=1, and cubic conflict frontier are distinct singular-value claims, not implied by spectral-rate optimality. Older Cegielski–Suchocka method includes an outer projector; full text inaccessible and remains risk.

## value

PASS

The precise distinction between first-step Euclidean nonexpansivity and faster asymptotic spectral convergence is substantive for nonnormal alternating-projection dynamics. The optimal spectral relaxation can expand Euclidean error even when stable, with an exact geometric cubic threshold; this is not a textbook consequence of eigenvalue bounds alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
