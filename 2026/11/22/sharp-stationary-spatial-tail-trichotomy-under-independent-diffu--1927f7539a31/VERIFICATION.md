---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The invariant positional sample is a centered Gaussian conditional on the integrated diffusivity during an independent exponential backward reset age. This needs no iid excursions: the position resets do not regenerate the joint process, but the stationary diffusivity history and reset age are independent, and a reset erases the initial position. Conditioning on the first refresh gives Φ_r(k)=rQ_r(k²)/(1−λQ_r(k²)), with Q_r(z)=∫W(d)/(a+dz) dd and a=r+λ. To justify the complete spectral resolution in RESULT.md lines 70–89, let M be multiplication by d on L²(W dd), let Π project onto the constant function 1, and put A=aI−λΠ. The rank-one inverse identity writes the transform as r⟨1,(A+zM)⁻¹1⟩=⟨1,(I+zA⁻¹/²MA⁻¹/²)⁻¹1⟩. A is strictly positive and M has zero kernel. The spectral theorem thus gives a positive Stieltjes measure (normalized by ∫s⁻¹ dmeasure=1), and interior C¹ regularity gives locally uniform cut boundary values. There W(a/s)>0 prevents denominator zeros; Stieltjes inversion gives exactly the continuous density in (2) and rules out a hidden singular measure on s>a. In the gap, Q_r(−s) increases from 1/a to H/a, giving the unique subcritical pole and the stated positive residue from the derivative. At s=a there is no atom: in the critical case Q_r(−a+δ)−H/a has order −δ^ν by edge scaling from the gap, so δF_r(−a+δ)→0; in the other cases F_r is bounded at the endpoint. Fourier inversion gives the exponential-mixture kernel with 1/(2√s). For the cut expansion set u=1−d and use the exact moving pole u₀=ε/(a+ε). Subtracting H/a leaves, to leading order, (C/a^(1+ν)) ε^ν times the scaled PV integral of v^(ν−1)/(v−1+i0), namely −π[cot(πν)+i]. Splitting below, near and above u₀ and subtracting the remainder's value at u₀ locally controls the PV error using the assumed derivative estimate; it is o(ε^ν). Thus the spectral edge is proportional to ε^ν for r>r_c and ε^(−ν) at criticality. With y=√s−√a, the continuum is e^(−√a x) times the Laplace integral of ρ_r((√a+y)²) in y, giving the exact gamma factors and the powers in lines 24–26. At positive distance from the edge the continuum is exponentially negligible, by the Stieltjes normalization. Below r_c the pole dominates. Finally the boundary moment can also be evaluated directly by the nonnegative series over refresh counts: rQ_r(−a) Σ_{j≥0}(λQ_r(−a))^j, with Q_r(−a)=H/a. This gives the asserted finite value and divergence regimes. For the beta law H=(ν+1)/ν, as claimed. Supplied verify_reset_edge.py was inspected, not executed; its numerical diagnostics are reported finite checks only.

## originality

PASS

Credit the previously established diffusivity-refresh dynamics, renewal transform and secular pole/edge mechanism. The distinct result on the available evidence is the exact stationary spatial-tail trichotomy for a regular bounded diffusivity edge, including critical and supercritical powers, evaluated amplitudes and the boundary-moment criterion. Position-only is the protocol in the theorem, not a claim that these stationary laws cannot occur under a joint reset. Cited fixed-time primary full-text coverage remains an access risk, not evidence for novelty.

## value

PASS

The theorem resolves how the dominant stationary tail changes when an isolated point of the spectrum meets a continuous edge. The single rate √a cannot distinguish the critical and supercritical tails: the algebraic factors on the two sides of integrability differ, and only above threshold is the boundary exponential moment finite. The explicit amplitudes and threshold for a class of edge densities give more than a rate estimate or a rephrasing of the underlying fixed-time BBP mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
