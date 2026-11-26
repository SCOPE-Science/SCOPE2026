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

Expanding the exact tensor gives L_i=2h_i²+2[H(y⊙h)]_i. Since yᵀH=1ᵀ−hᵀ and yᵀh=1/2, yᵀL=1, so the uniformly locally Lipschitz measurable-time field is tangent to the simplex. Its bounded per-capita rates preserve positivity at each finite time and give global continuation. At y*=ker A∩{1ᵀy=1}, H y*=1/2 and (y*)ᵀH=1ᵀ/2, so both mixture vector fields vanish. The same identities give (y*)ᵀL=1+2Q for arbitrary x; d_i x_i*=D*y_i* then yields V′=−2D*αQ almost everywhere. Interior entropy sublevels are compact. Q has positive-definite quadratic leading term in tangent directions because the share map is invertible and ker A contains no nonzero tangent vector, while V has positive-definite tangent Hessian. Thus Q/V is bounded above and below by positive constants (no direction-independent limiting ratio is needed). Integrating the two comparisons proves both directions including a strictly positive finite-exposure entropy gap. In the finite case, integrating the log equation leaves bounded log-endpoint terms and an O(S(T)) perturbation, forcing every Cesàro share limit into the normalized kernel; the infinite case follows from convergence. For g=3 a positive level is a regular simple closed curve, for example by strict radial increase on rays from x*, and the pure pairwise field has nonzero speed there. Compactness proves distance to that orbit tends to zero, not phase selection. The frozen exact-fraction checker was inspected, not run, and tests finite algebra only.

## originality

PASS

The same tensor and the relevance of proportional demography are prior. In the closest source, Eq. (B4) cancels an explicit rate-heterogeneity term under proportionality but leaves αG(x); this is not a proved globally coercive dissipation or a lower entropy bound for finite time-dependent exposure. The reviewed calculation reduces the remainder to a definite quadratic relative to the weighted equilibrium, and treats the sharp two-sided integral criterion and the offspring-average conclusion. No covering statement was identified in the strongest inspected sources or catalogue matches. This is a bounded assessment, not a historical priority certificate.

## value

PASS

The sharp criterion distinguishes vanishing schedules such as (1+t)^−1 and (1+t)^−2, which an autonomous threshold or inspection of the limiting mixture cannot distinguish. It gives both attraction and persistence with bounds for the natural demographic subcase where pairwise dynamics is conservative. It also separates pointwise coexistence from exact average offspring balance and identifies the limiting geometric object for three competitors. No claim is made outside the model or about phase.

The dated certificate retains the supplied scientific assessment, sources and limitations.
