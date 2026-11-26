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

The oxygen deficit x=C−O satisfies x'=r−m x. Its period map has slope E_H E_L in (0,1); the periodic past-integral solution is positive and bounded above by (r0+r1)/m_L<C. The positive periodic adjoint w'=m w−1 converts the mean by integrating (wx)'=wr−x. Its endpoint values and two exponential segments yield the stated mean by integration; in particular, ∫w'e^(iνt)dt equals Δ[m_H(1−E_L)(z−E_H)/(m_H+iν) − m_L(1−E_H)(1−E_L z)/(m_L+iν)]. The integration-by-parts boundary term vanishes, and expansion gives the submitted W_n with its sign and normalization. Its numerator would vanish only if the unit-modulus z equaled (R+iνν_v)/(R+iνν_u). The strictly positive product (m_H−m_L)(1−E_H)(1−E_L)=ν_u−ν_v and 0<ν_v make that ratio strictly smaller than one in modulus. The minus sign in the mean O makes −arg W_n the minimum, its antipode the maximum, and 2r1|W_n| their gap. Equal duty has z=1 for even n, giving zero raw rate harmonic but a strictly nonzero response. Degenerate rate contrast, duty or forcing amplitude are not within the strict conclusion, and no uniform-in-n positive gap is inferred. The frozen support script was read, not run. An independent reproduction (`python3 /workspace/independent_checks.py 1`) solves and integrates the driven complex deficit without an adjoint; it agreed for 102 finite settings to at most 8.10×10^(−17) in absolute error, including the half-duty n=2 gap 0.003427820700178107 at r1=1/2. The calculation corroborates the sign and formula; the strict modulus argument proves the universal result.

## originality

PASS

Best of current knowledge, the supported distinct claim is strict all-harmonic noncancellation for the two-level residence response, including even harmonics at equal duty. Sinusoidality from linearity and the periodic adjoint alone are not claimed as novel. The distinct periodic and oxygen-related records address different quantities. External lake and sediment papers have material access limitations, so no comprehensive priority claim or whole-paper negative claim is made for them.

## value

PASS

Equal high/low duty makes the raw even harmonics vanish exactly, yet every even harmonic of demand can still change the average oxygen through the residence response. This exposes a specific failure of reasoning from raw harmonic matching and supplies a computable benchmark for a time-dependent oxygen budget. It is not an empirical lake forecast, a hypoxia-duration result, or a finding about multi-level or spatially heterogeneous systems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
