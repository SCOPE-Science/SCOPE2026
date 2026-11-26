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

Reconstructed RESULT.md lines 34–70. Planck prefactors cancel at each wavelength, giving r_j=(s^k−1)/(t^k−1), k=4,2,1. For t>s>1, r_2/r_3=(s+1)/(t+1)<1 and r_1/r_2=(s²+1)/(t²+1)<1, so reciprocal depths order strictly when β>0. Factoring the two differences gives F_s(t)=(s+1)(s+t)/(1+t²); differentiation and endpoints give the strictly decreasing bijection onto (0,2s(s+1)/(1+s²)). In this interval R<s(s+1), so the quadratic has negative constant and positive leading coefficient: the plus radical is the only positive root, and the range calculation ensures t>s. Recovering β from the last two reciprocals and α from either of them matches the first via the same ratio. The equations f=β/(α+β), δ=1/(α+β) give the exact interior constraints β>0 and α>1; strict ordering already gives β>0. With any two distinct channels the two affine coefficients vary continuously as t varies, retaining the strict inequalities in a neighborhood, so the ambiguity is indeed local at every interior point. Even for arbitrary distinct monochromatic wavelengths the contrasts differ: with κ=T_star/T_c>1, log((e^x−1)/(e^(κx)−1)) has derivative [g(x)−g(κx)]/x<0, g(x)=x/(1−e^(−x)) increasing for x>0. Achromatic endpoints lose the spot information as stated. The s=2,t=3 example gives differences 75/16 and 25/8, R=3/2 and (α,β)=(75,25). I inspected checker.py without executing it; the synthetic runs reported by the record are not a proof of its all-parameter claim.

## originality

PASS

The supported distinct claim is the globally exact inverse and sharp physical data range at the three specified monochromatic wavelengths, together with the exact minimal channel count in that model. The transit-light-source forward formula, the use of multicolour information, and the broader principle of breaking spot degeneracies with another band are not credited as new. No inspected exact theorem settles this prescribed inverse and its image.

## value

PASS

This gives one simple exact model in which observers can distinguish structural two-band ambiguity from an invertible three-band diagnostic. The geometric wavelengths give a factorization that proves global rather than local identification and make rejection of incompatible positive triples possible. The strict α bound has the physical meaning that the planet is smaller than the available photospheric area. Value is as a noiseless identifiability and feasibility benchmark, not an instrument-ready estimator or an assertion about arbitrary wavelength triples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
