---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Integrating the normalized Thomas–Fermi profile gives a zero plateau through λ=a, the partial-coverage polynomial 1−3a/(2λ)+a³/(2λ³), then the full-coverage expression 3(b−a)/(2λ)−(b³−a³)/(2λ³). They match in value and first derivative at b. The latter derivative has the sign of a²+ab+b²−λ², so the unique maximum lies above b, equals (b−a)/λ_c, and is less than one since λ_c²−(b−a)²=3ab. Differentiating the continuous reset survival gives the stated h. The strict positive-count exceedance set is exactly the interval between the two inverse scales; the difference of S gives its probability, yields the two Jacobians on differentiation, and tends to S(a) at zero. The zero atom from the plateau is therefore correctly normalized and there is no atom at the maximum. At a the contact coefficient is 3/(2a²); combining its inverse Jacobian with h(a) for a>1 or h(1+u)∼r₀u^{−1/2} gives the two prefactors. For the distant branch, λ_+∼3(b−a)/(2k) and log h=−r₀λ+O(log λ), while the Jacobian contributes only O(log λ) to the log density. At the maximum the contact coefficient is 3(b−a)/(2λ_c³), giving two equal leading square-root Jacobians, their stated sum, and conditional weights tending to one half in the continuous branch-weight version of the conditional law. Fresh sample quadratures matched the survival difference to relative error below 3×10⁻¹⁶ on two shells, including a=1; finite differences and both endpoint checks were consistent with the formulas.

## originality

PASS

The supported distinct contribution is the complete nonmonotone shell classification, its geometry-only interior maximum, two-branch law and fold coefficient, and the resulting two-scale ambiguity. The common-scale conditional profile and scale distribution are known; subtracting centered counts already gives the shell map. Both lower-edge exponents and prefactors of the dominant branch are covered by the centered result after local reflection, and the distant-branch log rate is inherited from the centered tail with the effective width. These are not priority claims. The frozen citation to Appendix H should read Appendix C in the inspected version.

## value

PASS

A two-sided exterior shell is a natural observable: it initially gains mass when the expanding cloud reaches it but eventually loses mass as the profile dilutes. This creates an exact upper limit and two possible cloud scales even for ideal, noiseless macroscopic counting, unlike a centered-window observation. The geometry of the fold and the conditional near-edge weights give a concrete inverse-measurement consequence, beyond reproducing known endpoint powers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
