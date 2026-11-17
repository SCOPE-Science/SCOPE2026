---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

For m,r>=3, every shared backbone vertex occupies two neighboring clique sites and each private vertex occupies one. Independent exponential arrival priorities turn random greedy independent set into competing single-site monomer attempts of total rate r-2 and neighboring dimer attempts of rate 1. With lambda=r-1, the cyclic empty-interval hierarchy E_k' = -(lambda k-1) E_k - 2 E_{k+1}, E_m=e^{-lambda m t}, is exact; the infinite-reference solution E_k=exp[-(lambda k-1)t-(2/lambda)(1-e^{-lambda t})] satisfies the same ODE. Integrating the finite/infinite difference backwards gives the claimed exact signed density correction. J_m<1/(lambda m) follows from the integrated hierarchy and J_{m+1}>1/(lambda(m+1)+1)>1/(2lambda m), so the correction is strictly alternating by m. Laplace localization gives difference 1/(lambda m)-J_m~1/(lambda^2 m^2), and hence factorial decay at fixed r. An independently written exact rational recursion for greedy outcomes on the actual graphs matched the integral law at m=3..5,r=3..5, including alternating signs.

## originality

PASS

The r=3 specialization is mathematically equivalent, through the line graph of the n-sunlet C_n o K1, to the independently published same-day Resultary sunlet dimer-jamming theorem. Its expected matching density is twice the candidate clique-MIS vertex density and its exact parity correction likewise transforms. That special case is NOT new. However the actual claim covers every r>=4, corresponding to monomer rate lambda-1>=2, which is not implied by the sunlet equal-rate result; its exact lambda-parametric finite ring law, strict sign and factorial correction survive. General local-limit greedy MIS work and Pippenger 1989 RSA discuss general methods, not this exact multi-rate finite-cycle correction in accessible material.

## value

PASS

The genuine surviving r>=4 family classifies a natural one-parameter family of cycles of overlapping higher cliques. It identifies exact signed finite-ring versus thermodynamic density errors and their superfactorial decay for every clique size, a nontrivial finite-geometry correction inaccessible from local limits. The r=3 sunlet case is credited as covered, not counted as distinct novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
