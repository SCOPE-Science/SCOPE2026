---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

PASS. In K_d(α)=[-1,1]^d∩{∑|x_i|≤αd}, coordinate symmetry gives L(K_d)^2=E[U_1²|∑U_i≤αd]/(4 Pr(∑U_i≤αd)^(2/d)), U uniform [0,1]. Exponential tilt q_λ(u)∝e^-λu on [0,1], with α=1/λ-1/(e^λ-1), and bounded-density local CLT yield limit m2 exp(2I)/4 (α<1/2), whereas α≥1/2 gives 1/12. Differentiating leads to B(λ) exponential polynomial; its e^(2λ)B(λ) Taylor coefficient sequence begins zeros c0..4, then 10,46,112,132,-258 and all c_n<0 for n≥9. Dividing by λ^8 yields strictly decreasing function crossing once, so unique λ*=2.841711738..., α*=0.289962235..., L²=0.06227292078..., below 1/12 and 1/(2e²). Independent exact coefficient and high-precision minimizer checks corroborated; all-dimensional claim follows from local CLT and analytic sign argument, not finite exact integration.

## originality

PASS

PASS on inspected evidence for a UNIQUE globally optimal limiting isotropic constant over proportional cube/cross-polytope intersections. Kabluchko–Prochno work develops Gibbs/maximum entropy and intersection volumes; Alonso-Gutiérrez–Prochno gives broad isotropic limit for Orlicz balls under conditions, not a published sharp unique radius minimizer of this hard-clipped family; Frühwirth–Prochno studies concentration/deviations, not this constrained isotropic optimum. The known general techniques are credited, while explicit exponential polynomial one-crossing optimizing α remains distinct. Historical risk: a general Orlicz/large-deviation result may implicitly encode the formula and older equivalent geometric optimization could exist.

## value

PASS

PASS. Isotropic constant is a central affine-invariant convex-geometry measure; cube∩scaled cross-polytope is a canonical continuous interpolation. The fact that neither endpoint minimizes limiting constant, together with a unique nontrivial interior optimum, explicit λ/α characterization and global sign proof, gives a useful exact asymptotic extremal benchmark. It is not a generic normalized volume calculation or arbitrary numerical grid.

The dated certificate retains the supplied scientific assessment, sources and limitations.
