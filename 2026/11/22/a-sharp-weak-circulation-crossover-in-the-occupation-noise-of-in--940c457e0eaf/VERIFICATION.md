---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The flux identity 2T=1−tanh(gΔ/2) gives the stated dissipative term in the derivative of V=||x−1/M||². The bias-dependent part of the linear flux contributes zero by cyclic summation; the symmetric part contributes −(1/2)Σ Δ_i². For fixed M the Poincaré constant is positive and the finite jump-generator remainder in LV is at most 2/N. For V², the jump chain rule gives L(V²)=2VLV+Σ rate·(ΔV)², with the last term O(V/N+1/N³), giving stationary E[V²]=O(N⁻²). The scaled processes have tight stationary initial laws, drift bounded by a constant times ||Z|| uniformly in N, bounded martingale bracket rates and jumps of size O(N⁻¹/²). A martingale maximal bound and Gronwall give compact containment; increment tightness follows by localization and the same drift and bracket bounds. On compact sets the drift and bracket tend to HZ and Q, with higher jump terms vanishing. Every stationary subsequential limit solves the OU martingale problem; on the zero-sum hyperplane all nonzero modes are strictly stable, hence the limiting stationary law is unique. Fourth moments give uniform integrability for the lag covariances. The 1/N correction in the alternate rule is a uniform O(1/N) change to the fraction drift at fixed parameters, hence vanishes in the fluctuation drift and can be absorbed in the Lyapunov bounds. Fourier diagonalization of H and Q yields the stated decay, frequency and stationary covariance, with no zero mode. Integrating the exponentially decaying lag covariance yields the sample-mean variance coefficient. Strict monotonicity follows from at least one nonzero sine mode for M≥3. At zero bias the cosecant-square sum gives the stated coefficient. For α=(M+g)/M and d=|δ|>0, an independent roots-of-unity check writes each nonconstant-mode integrand as the Poisson kernel d⁻¹(1−r²)/(1−2r cos θ+r²), r=(α−d)/(α+d). Averaging all grid modes and removing the zero mode gives A_M=2/[M(M+g)]·[(M/d)(1+r^M)/(1−r^M)−α/d²]. This confirms the coth limit from r^M→exp(−2|ζ|/(1+κ)) and gives 2/[d(M+g)] when Md→infinity, in particular for fixed nonzero d. The unbiased/zero-ζ limit is as stated. The crossover describes departure from order-one noise at bias scale 1/M; vanishing biases above that window can have intermediate orders, not necessarily order M⁻¹. Replay in RESULT.md §§1–4. VERIFICATION.md and check.py were inspected, not run: 1,506 counts the first printout and 1,554 the full checker, which addresses the OU algebra and asymptotics rather than proving the particle limit. The assessment is only for the stated sequential limits.

## originality

PASS

The distinct result credited is the all-M stationary fluctuation and occupation-noise theorem for the interacting repulsive particle model, with explicit bias and interaction dependence. The formal linearization framework is prior work, and the integrated OU coefficient and coth profile, taken as facts about a biased nearest-neighbor cycle, are standard cycle-potential mathematics or follow from the exact prior hitting solution. No separate novelty is credited to those cycle identities. The existing WKB approximation and walk results do not establish the stationary particle-to-OU limit and its temporal covariance for this full interacting family.

## value

PASS

The useful invariant is the occupation-time noise of the interacting particle model in its stationary limit, not a repackaged cycle sum. Justifying the stationary fluctuation field across the whole repulsive class lets one distinguish bias-invariant instantaneous variance from bias-sensitive temporal precision, and quantify exactly when the precision changes with ring size. The concentration argument and exact asymptotics together make this an independently useful benchmark; the textbook walk and series ingredients alone would not meet that bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
