---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For p>2, 2-cycle gap d∈(0,p) satisfies q=Qp(d)=p+d coth(d/2−artanh(d/p)), increasing from p²/(p−2) to ∞ on 0<d<d∞. Thus exactly one prime two-cycle in the asserted regime, not merely computational detection. Let d∞=2θ, p=2θ coth θ=P(θ). Derivatives P′>0,P″>0 give limiting M∞=(1−p)²−d∞²=1−2θP′(θ), crossing −1 once where θP′=1; implicit expansion in t=1/q gives d=d∞−K/q+O(q⁻²), M=M∞+C/q+O(q⁻²). At crossing C=4(p³−3p²+4p−1)>0, M∞′=−2(1+θP″/P′)<0, so S=−C/M∞′≈6.745591544665048>0. Sign of multiplier locally yields attracting/repelling sides. No claim of nondegenerate flip bifurcation at equality. Scripts inspect actual equations; numerical roots only corroborate analytic IFT.

## originality

PASS

Best-of-knowledge PASS specifically for positive 1/q displacement coefficient of period-two multiplier −1 locus and the finite-q attracting limit-threshold distinction. Ricker limiting threshold and existence of the prime 2-cycle are previously known: Kryzhevich et al. 2021 prove same map cycle existence and Alonso Mozo et al. 2025 rigorously locate finite-q period doublings. Their inspected full main parameter discussions and numerical continuation do not state or imply first asymptotic coefficient S. Mathematically distinct stronger coverage was searched, not found.

## value

PASS

The sign and quantitative shift in a natural strong-predation limit answer a meaningful stability question: the finite-strength model is attracting exactly where the limiting Ricker model is neutral. The explicit leading-order drift is neither fitted from a finite scan nor implied by the old leading limit; it determines an experimentally relevant finite-q boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
