---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Confirmed the nonstandard ninth-moment polynomial certificate exactly: rational integral of lower alternating J1 polynomial on [0,7/2] is 0.013703182867... >137/10000. Independent outward fixed-point interval sixth-power Simpson calculation on 6001 rational nodes and Watson tail bound gives I1(6)<0.108884052<109/1000. Also recomputed exact rational bounded-order k=2..11 sixth moment integration cores below 0.07; published Xu fifth-moment 13/40 plus Landau sup amplitude supplies k>=12 analytically, and a Sonin monotonicity argument handles k=2 sup<1/2. Hölder implies I1(q)>0.0137*2^(-(q-9)) while Ik(q)<0.1*2^(-(q-6)) for all real finite q>=9, with strict gap since 0.0137>0.0125. The sharp stability coefficient and equality modes follow from Xu radial-angular spectral theorem. Infinite range does not follow from finite numerics alone.

## originality

PASS

Xu identifies sharp global constant and spectral stability formula but expressly leaves maximizing positive circle degree unknown in general. Previously published SCOPE q=6 and q>=27 results do not imply 9<=q<27; new exact ninth-moment separator and Hölder improvement close that gap. Relevant high-order bounds imported and credited, not newly discovered.

## value

PASS

Identifies exact minimizing nonconstant stability direction for a continuous real-exponent half-line in a natural sharp Fourier extension inequality, replacing a sufficient earlier q>=27 threshold by q>=9. This is a motivated structural stability coefficient, not a tiny arbitrary slice, without claiming 9 is optimal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
