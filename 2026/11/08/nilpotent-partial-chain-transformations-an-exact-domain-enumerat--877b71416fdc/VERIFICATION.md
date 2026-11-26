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

The monotone restriction to a persistent cycle is an increasing bijection of a finite chain and fixes it pointwise, so fixed points are precisely the obstruction to nilpotence even without injectivity. Marking fixed points forces monotone values into the adjacent closed target intervals; the end gaps therefore give B, the interior gaps C, and no marked point gives A. Signed marking gives A−zu B²/(1+zu C). Summing the coefficient identity [x^m]T(x)^(m+h)/(1−x) by substituting x=zT(x) gives the Jacobian denominator (1−zR)(1−zT′(zR))=R sqrt(Δ), yielding exactly the stated radical and constant term 1. For uniform singularity, R=2/(1+z+sqrt(Δ)) is nonzero on the chosen branch near the dominant disk. A zero of sqrt(Δ)+uzR would require sqrt(Δ)=−u(1+z)/(u+2), hence (1+z)^2=(u+2)^2 z. At u=1 the smaller root (7−3√5)/2 is positive and has the opposite sign of sqrt(Δ); the larger is outside a slit disk containing the dominant singularity. These exclusions persist in a common rescaled slit neighborhood after z=ρ(u)w for complex u near 1. The denominator at z=ρ equals u/(1+u) and the linear coefficient in sqrt(Δ) of its reciprocal is −sqrt(1+u)/(u²sqrt(ρ)); the expansion is a convergent Puiseux series, so uniform transfer gives the stated relative O(1/n). The leading log-mgf is 2n arsinh(sqrt(exp(t))) up to its value at t=0, giving derivatives 1/√2 and 1/(4√2) after division by n. Uniform analytic error permits differentiation for the O(1) moment remainders and gives the centered normalized Gaussian law.

## originality

PASS

Credit earlier fixed-point counts and the maximal-domain stratum in this exact monoid. The supported distinct part is the all-domain refinement for partial weakly increasing maps together with its intrinsic Gaussian constants. The nearest rank-limit result for strictly increasing partial injections is for a different sample space. Priority is assessed on accessible evidence and is not exhaustive.

## value

PASS

Domain size is a natural parameter of a partial transformation, not a cut chosen after computation. Counting the entire nilpotent stratum by that parameter and identifying its global fluctuations with explicit constants are usable beyond the unweighted count, in particular for sampling and comparisons between weak and injective maps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
