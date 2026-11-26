---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The cyclic average selects exactly the Fourier modes divisible by m. With the probability normalization dθ/(2π), the positive first cross-term at mode m forces all and only the aligned phases at s>0. Parseval gives the best-angle error increment 2g with g=s²/(1−s²)−2(rs)^m/[1−(rs)^m]. It diverges at s→1 for each r<1, and s=0 is one density regardless of phase. For m≥4, comparison with (rs)^m≤s⁴ gives g≥s²/(1+s²)>0. For m=2 the strictly increasing ratio (1−r²t)/(1−t), t=s², reduces the derivative sign test to crossing sqrt(2)r. The resulting t=2δ+O(δ²) gives 2g=−4δ²+O(δ³). For m=3 the numerator of g after multiplying by positive denominators is s²[1−u(2s−s³)], u=r³. The cubic has its unique maximum at s_c=sqrt(2/3), giving the stated critical u, and exactly four distinct minimizing densities at equality. The derivative sign for s>0 is the sign of R_u²−3u; R_u decreases and then increases since its derivative has sign Q_u and Q_u is strictly increasing from negative to positive. Above criticality a strictly negative value forces the larger stationary root to be the sole positive minimum. At the critical positive branch the factorization gives g_ss=18, permitting smooth continuation; 2g_u=−4s_c³/(1−u_c s_c³)²=−32sqrt(6)/9. These verify the onset laws and all global uniqueness assertions under the stated model. Replay: RESULT.md steps 1–4 (lines 54–111). Inspected finite quadrature/diagnostic evidence is supplementary, and r=1 is not included.

## originality

PASS

The distinct supported claim is the exact global continuous/coexisting/no-improvement taxonomy for a normalized one-Poisson population L² projection of a regular equal cyclic orbit, with exact radii and onset laws. The standard Poisson Fourier/mixture identities and related fits are not credited as new. The closest statements differ in metric or exclude the decisive geometric limit, and no covering statement was established by the bounded comparison.

## value

PASS

Exact nonlinear compression of cyclic harmonics distinguishes a continuous loss of uniform fitting, a discontinuous jump with genuine coexistence, and a regime where all nonuniform fits are worse. The sharp m=3 comparison, unique positive branch and loss slope go beyond a local bifurcation test, and the contrast with KL illustrates an observable consequence of the loss choice. The result does not claim the high-symmetry mixture is itself undetectable or uniform.

The dated certificate retains the supplied scientific assessment, sources and limitations.
