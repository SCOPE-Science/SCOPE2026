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

For the one-window update, normalize the sole residual secant or equivalently use its unnormalized least-squares coefficient t_j. Since AᵀA=SI and ⟨f,Af⟩=μ‖f‖², after an actual scalar step α_j the coefficient is 1−μ/(Sα_j). When α_j=β the correction vector Δx+βΔf equals βf_j, so the next step uses μ/S; after that step t_j=0 and the next step uses β. The initialization starts the induction. Both error-step matrices are nonsingular scaled rotations, so a nonzero initial error never vanishes and each secant is nonzero. They have norm factors z and r, giving the exact parity laws. Solving r²z²<1 gives the stated unique positive critical step; equality yields two fixed positive norm subsequences, and greater values give divergence. The unaccelerated norm factor z crosses 1 at 2μ/S; the threshold ratio and κ₂(A)=1 follow. At β=β_MR both steps coincide and every coefficient vanishes; the parity formulas still hold. In the cited Tang arXiv v1 the proper references are Algorithm 2.1 and limited-depth Proposition 2.7 (also Lemma 2.1), not the numbering in the frozen bibliography. Its window-one normalization matches the stated algorithm. The uploaded verifier and its recorded 486 and 605 checks were inspected, not executed. Its explicit threshold assertion compares β_crit with 2β_MR, rather than testing equality dynamics; the boundary conclusion follows from the algebra above.

## originality

FAIL

The exact full-parameter formula is not printed in the inspected earlier sources, but it is mechanically implied by their combination. In exact arithmetic window-one AATGS is ordinary AA(1) on q(x)=(I−βA)x+βb. Adam Smith's 2024 thesis already proves the alternating-zero mechanism using only the scaled-orthogonality identity that this q satisfies. Once that mechanism is applied, the previously published two-step rAA(1) propagator of Krzysik–De Sterck–Smith applies with α(v)=μ/(βS) identically, yielding the other scalar step and norm multiplier by direct substitution. Smith also states the alternating coefficients, individual norm factors and rescued divergence window in the βμ=1 subfamily. The unrestricted positive-β critical value and advantage then use only the norm of a scaled rotation and a quadratic inequality. This is documented prior implication, not a negative verdict from an unavailable source or a claim that the frozen formulas are false.

## value

FAIL

The stability question on a natural planar test family is motivated, and the explicit inequality is pedagogically useful. But alternating zero weights and rescue of divergent base iterations were already obtained in the skew fixed-point case; over the stated shifted family the remaining scalar formula and stability interval are mechanical evaluations of the earlier proof and propagator. The threshold-ratio limit does not supply a separate nonroutine invariant or extension. No genuinely distinct valuable remainder is established for a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
