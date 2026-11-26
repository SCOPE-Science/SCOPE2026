---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The proof applies to all the stated weights and residues. Rotation removes the symbol phase, and gamma-ratio monomial norms give the reducing weighted shifts with weights w_j. Expansion of the finite product over the m factors gives w_j²=1−(alpha+1)/j+O(j^−2) and w_j=1−(alpha+1)/(2j)+O(j^−2). The coefficient limits give a compact perturbation of the constant Jacobi block and hence its Fredholm interval, also for c=0. For 0<c<1, after alternating signs, an independent way to write the exact shifted form is sum_j cw_j|u_(j+1)−u_j|² + sum_j V_j|u_j|² with V_j=w_j²−1+2c−c(w_j+w_(j−1)), taking w_(−1)=0. Thus V_j=−(alpha+1)(1−c)/j+O(j^−2). In [N,2N] the potential is bounded above by −(alpha+1)(1−c)/(4N) for large N, while Dirichlet sine vectors on consecutive segments of length K sqrt(N), separated by one zero site, have weighted kinetic cost at most c pi²/(K² N). The span has dimension proportional to sqrt(N) and Rayleigh loss at least eta/N after choosing K large. The min–max inequality at that intermediate threshold is non-strict as written; taking N=floor(eta/(2 epsilon)) supplies strict slack at the claimed counting threshold L_c−epsilon, so the final statement follows. For c=0, the weights squared are strictly increasing to 1 and give the explicit discrete eigenvalues. For c>=1 the pointwise bounds on the analytic multiplier imply the asserted full spectral interval, blockwise as well. A Jacobi recurrence with nonzero off-diagonals gives simplicity for c>0 within each block. These are analytic checks; the supplied finite rational inequalities are supplementary and were not used as a proof of the infinite count.

## originality

FAIL

The lower counting bound and qualitative cascade are correct but are corollaries of an older, exactly solvable discrete Coulomb model. After the frozen record's elementary residue decomposition and weight expansion, comparison to that model even yields a sharp leading asymptotic for every block. Thus the decisive quantitative assertion is covered by prior mathematics, not merely reminiscent of another Bergman example. This finding is based on the recurrence, discrete mass formula and form comparison, not on lack of access to another paper or on the date of a same-day record.

## value

FAIL

This is a natural Bergman spectral question, and the elementary proof of the lower estimate is correct. However, the frozen result supplies only the standard essential band and phase cases plus a weaker version of what direct comparison to the classical Coulomb spectrum already yields. It establishes neither new outlier locations nor a new invariant beyond that comparison. A readable worked specialization can be useful exposition, but the claimed count is mechanically implied and is not a distinct mathematical finding under the stated standard. No repaired finding is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
