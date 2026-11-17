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

The transform convention is unnormalized A_f(x,χ)=∑ f(t) overline(f(t−x)) overline(χ(t)), for finite abelian G, proper H of order h>=2, y outside, z nonzero. Expanding four disjoint product types proves h−1 nonzero H-shift rows of q=N/h characters and a zero-shift row with N entries minus q/r cancellations iff r is even and |z|²=h. For quotient order r>2 the ±(y+H) cross-cosets do not overlap, contributing 2hN. For r=2 they coincide, cross-row factors z+bar z overline χ(x); evaluation of character χ(x) over its o(x) roots produces exactly N/o(x) vanished entries iff d=ord(−bar z/z) divides o(x). This gives the complete support formulas, all phase-attainable levels, minimum at calibrated |z|²=h and d|gcd orders, and the lower bound from o(x)>=2 with sharp elementary two-torsion equality classification. Independent exact Fourier enumeration over cyclic Z8 with H even and z=2,2i returned support 41, with z=1 support 42; a binary two-dimensional equality check and original exact cyclotomic test cases corroborate. These finite examples are not an arbitrary-group proof.

## originality

PASS

Nicola 2022/2023 theorems classify extremal finite Gabor/STFT ambiguity support and equality waveforms, including subgroup indicators, but the materially inspected 2023 Theorem 4.5 does not enumerate all exact support levels after adding one nonzero off-subgroup impulse, optimize its phase for each torsion coset, or distinguish quotient order two from higher orders. Nearby two-sparse or three-tap cyclic support records address different supports/window geometries. The self-ambiguity expansion here is elementary Fourier orthogonality; novelty is restricted to the full torsion-sensitive support stratification, sharp bound and equality phases for every finite abelian G. Historical priority provisional because a specialized Gabor-perturbation paper may contain an equivalent count.

## value

PASS

A subgroup indicator is a natural exact localization extremizer in finite time-frequency analysis; adding one point outside the subgroup is the minimal structural perturbation. Classifying exact cancellations shows an otherwise invisible order-two quotient produces an arithmetic phase staircase, provides a sharp universal gap with exact equality configurations, and distinguishes all higher quotient orders. This useful structural instability result neither claims a general new uncertainty principle nor noise-stable estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
