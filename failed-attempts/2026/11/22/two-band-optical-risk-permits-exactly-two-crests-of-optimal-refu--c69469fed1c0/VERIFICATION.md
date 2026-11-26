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

The depth Hessian is strictly positive, the derivative at zero is 1−21k and the depth derivative tends to infinity. These prove existence and uniqueness, including the zero boundary branch; the nonzero Hessian gives smoothness on k>1/21. With y=kz and G(y)=e^(−y)+20e^(−20y), the stationarity equation is e^(y/k)=kG(y). The function log k+log G(y)−y/k increases in k and decreases in y, giving a strictly increasing coordinate y. At the threshold y tends to zero, while bounded y at infinite k would make the right side of stationarity diverge and the left approach one. Thus all y>0 are traversed. The sign of z_*' is the negative sign of f(y)=(y−1)e^(19y)+20(20y−1); f is negative, positive, negative, positive at 0, 1/10, 1/2, 1. The strict signs use e^(1.9)<8 and the fourth-degree Taylor lower bound e^(9.5)>360. Since f''=(361y−323)e^(19y) has exactly one positive zero, Rolle's theorem gives exactly three positive roots; another zero of f' at any root would contradict that curvature count. Therefore the three turns on the positive-depth branch are a strict maximum, minimum and maximum. The bound z_*<=log(21k)/(1+k) gives the decay. In the one-band case the positive solution is log(abk)/(1+bk); its derivative sign is that of 1+1/t−log(at) with t=bk, which strictly decreases from a positive threshold value to minus infinity. My Decimal replay of the three roots and the inverse stationarity equation reproduced all displayed digits of the three attenuation and depth values.

## originality

FAIL

The central mode-count claim is a direct corollary of published equal-shape Gamma-mixture bimodality criteria. On the positive branch stationarity gives z exp(z)=yG(y); hence z=W_0(yG(y)), with W_0 strictly increasing, and y(k) strictly increases onto (0,infinity). Thus the response has exactly the same extrema, in the same order, as yG(y). After multiplication by 20/21 this function is exactly a mixture of shape-2 Gamma densities with fast rate 20 (weight 1/21) and slow rate 1 (weight 20/21). Došlá (2009), Proposition 6, gives the precise bimodal region, and Ahmed–Goria–Hussein (2008), §2.2, gives the equivalent common-shape criterion. Substituting the stated parameters proves bimodality strictly inside that region. For one band the corresponding transformed curve is a multiple of the single shape-2 Gamma density, already strictly unimodal. The depth minimization interpretation does not change the mode count, and the threshold, limit and numerical coordinates are routine stationarity consequences. This is demonstrated prior implication, not an inference from inaccessible ecology literature.

## value

FAIL

The example is a correct illustration that uniquely optimizing a stylized tradeoff can give nonmonotone comparative statics. Here its proposed mathematical contribution is, however, a fixed parameter substitution in known Gamma-mixture bimodality, followed by monotone depth and attenuation coordinates. The one-band comparison is the elementary single-Gamma case, and the isolated decimal coordinates and endpoint facts do not supply an independently useful new result. The specific ratio and amplitudes are not independently motivated by a physical setting, and no new full two-band boundary, downstream application, or standalone structural theorem is established in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
