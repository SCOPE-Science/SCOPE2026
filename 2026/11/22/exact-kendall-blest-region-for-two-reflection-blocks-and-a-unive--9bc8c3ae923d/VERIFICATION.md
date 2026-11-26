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

Different blocks are ordered concordantly, while two draws in the same reflection interval are discordant almost surely, giving τ=1−2Σℓ_i². Integrating (2x−ℓ)² over the block gives ℓ³/3 and its sum coordinate is constant, giving the stated Blest penalty. With s²=Σℓ_i² the lower envelope follows from h_i≥0 and monotonicity of 2√x−x on [0,1], with equality only for one initial interval when 0<s<1. The nonnegative loss sum extends to countably many blocks. Fixed positive lengths maximize η only by right packing; swapping two packed blocks changes the divided loss by 2ab(a²−b²), so the shorter precedes the longer. After substituting r=a/b the divided loss is s⁴f(r). Direct differentiation gives f′(r)=−2rP(r)/(1+r²)³, and P′<0 on [0,1] with opposite endpoint signs, so the unique unconstrained minimizer is r_*. The length factor (1+r)/√(1+r²) is strictly increasing to r=1. Thus below t_* the feasible ratio ends before r_* and saturation forces (a,b)=((1−√(−t))/2,(1+√(−t))/2); above t_* the unconstrained minimizer fits. Substituting gives both claimed formulas with equality at the transition; independent cubic bisection agrees with the three reported decimals. Strict packing, ordering, and ratio optimization prove the maximizer classification. The only cases s=0,1 are identity and full reflection. Sliding one block and then increasing the right-packed ratio connects the extreme values continuously at fixed τ; the strict one-block improvement follows from 1−f(r)=2r²(1−r)/(1+r²)². For refinement, after packing and sorting, split a positive lowest block a into c<d with c²+d²=a² and added length less than the available slack. The divided-loss gain is 2c²d(d−c)+2B(a³−c³−d³)>0, where B is the total length above it; Kendalls are identical. The restriction of the lower bound to block sums matters: mixing the identity and full reflection copulas in proportions 3/4 and 1/4 gives τ=η=1/2 (the cross Kendall expectation is zero), below L(1/2)=5/8.

## originality

PASS

The supported distinct claim is the complete attainable two-block Kendall–Blest section, especially the upper optimizer, cubic ratio and length-saturation transition with an equality classification. Rockel already gives the general block identities and the strict one-block split at fixed Kendall τ. The sharp countable lower bound is a short consequence of the old loss identity, and the finite refinement uses and extends the known splitting mechanism; neither prior ingredient is credited as new. The constrained optimization with exact transition, placements and section filling is not supplied by the inspected prior statements. The matched indexed two-block record is the frozen record itself. Other regions in the reviewed sources replace one of the coefficients. This is a bounded best-of-knowledge decision.

## value

PASS

The two-block family is the first deformable refinement of the one-block candidate in the existing Kendall–Blest boundary problem. The exact optimal extent of that improvement, including a geometric saturation transition and all attainable values, is a useful sharp benchmark and a constructive bound for the unrestricted problem. It is not merely another improved example. The known local block formula and routine lower-bound corollary are not the basis for this judgment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
