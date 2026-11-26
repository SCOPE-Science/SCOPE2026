---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The two affine maps take the interiors of cells 1,3,4,6 to (2/3,1) and cells 2,5 to (1/3,2/3); their orientations do not affect the uniform pushforward. Conditional uniformity on each newly visited cell is preserved even with the map choices fixed in advance. Overlap lengths give the two rows in the proof, and the invariant masses (1,1,1,3,5,5)/16 give the stated density. For f the digit-3 indicator, Pf is 1/2 on cells 2,5 and 0 elsewhere. For g=f−3/16, Pg takes the values 5/16 and −3/16 on these two types; the type transition probabilities 1/6 and 1/2 into {2,5} give P(Pg)=−Pg/3. E(B₀B₁)=1/32 and Var(B₀)=39/256 give the claimed covariance. With ρ=−1/3 the triangular geometric sum gives slope 39/256+2(3/256)ρ/(1−ρ)=75/512 and boundary coefficient −2(3/256)ρ/(1−ρ)²=9/2048. The chain communicates via cell 5 and has a self-loop at cell 2, so the finite-chain additive CLT applies. The digit-2 middle state must be cell 5 for the final 3; this gives the triple probabilities 1/32 and 1/8 and the corresponding two-digit denominators 5/32 and 21/32. These calculations apply at p=0 and 1 as well. Analytical replay suffices; the finite checker was inspected, not executed.

## originality

FAIL

A distinct indexed statement covers the central stationary digit-process law, all positive-lag covariances, the finite-sum variance and the Gaussian coefficient for this same six-cell system, under the stronger hypothesis of arbitrary fixed switching schedules (hence also iid switching by averaging). The six-cell refinement and the two explicit non-Markov conditionals are short consequences of the stated branch geometry and stationary masses; they do not recover a distinct substantive theorem. This is a coverage finding, not a claim about which record was derived first.

## value

FAIL

Parameter nonidentifiability and exact fluctuations are meaningful for this observed dynamical system, but already covered. The remaining six-cell presentation and conditional witness are immediate from the common branch images and short cylinders of that process. They add neither a distinct obstruction nor a quantitatively independent invariant that merits a repaired claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
