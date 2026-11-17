---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For the two-state transient generator Q=[[-(2e+z),2e],[c,-(e+c+z)]], solve backward equations to obtain mean M=(c+3e+z)/(2e²+z(c+3e+z)) and principal extinction-decay eigenvalue Lambda=z+ell(c), ell=(U-sqrt(U²-8e²))/2, U=c+3e. With c=c0 exp(-ad), z=z0 exp(-bd), b>a>0, direct differentiation gives M-prime numerator bz(N²−2e²)−2ae²c and Lambda-prime=−bz+ac ell/Delta. The first sign is strictly decreasing after division by c, the second sign strictly increasing after factoring z, so each optimum exists and is unique, interior or d=0. Comparing the thresholds ell/Delta >2e²/(N²−2e²), verified algebraically from Delta²=U²−8e², establishes 0<=d_T<=d_M with strict inequality when d_M>0. Thresholds z_M and z_T are the unique positive derivative-zero amplitudes; comparison gives 0<z_M<z_T and all three regimes. Independently checked derivatives by SymPy and numerical roots at e=c0=a=1,b=2 for z0=.03,.08,.3: (d_T,d_M)=(0,0),(0,0.0976825677),(0.6025942056,1.0454816873). Boundaries and domain 0<a<b are explicit. Neither finite grids nor solver logs substitute for proof.

## originality

PASS

Wagner--Ross--Possingham introduce the reserve-spacing trade-off and eigenvalue criterion in a different *discrete-time* model allowing one-reserve catastrophe outcomes, rather than a continuous-time state-independent systemwide-fatal shock. Their objective is late-survival eigenvalue, not a universal cross-objective ordering between initial-full-state mean lifetime and tail decay. Published two-patch extinction work studies fixed directional-rescue allocation and symmetry with no spacing-dependent common catastrophe. The new claim is a nontrivial exact comparison of two optimizers with three sharp amplitude regimes, not the Markov model concept or standard spectral formula. McCarthy and Blowes papers are plausible historical competitors but their complete primary text could not be inspected; novelty is best-of-knowledge with prominent risk, not an unqualified NOT_COVERING assertion.

## value

PASS

Choice of reserve spacing is a natural conservation optimization problem and the mean initial-extinction time and asymptotic survival time are two genuinely different persistence metrics. The all-parameter inequality d_T<=d_M and exact phase boundaries show when the objectives make different spatial decisions. The result is a meaningful model-specific decision boundary, not an assertion that these rates are empirically calibrated or that the conclusion holds for arbitrary catastrophe models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
