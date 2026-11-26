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

On uniform C6, orthogonality gives s=2A^2+2B^2+C^2 and T=2B^2+2C^2 for Fourier moduli A=|a|, B=|b|, C=|c|. The zero-sum triples are (1,1,4),(2,5,5) with multiplicity 3; (2,2,2),(4,4,4) with multiplicity 1; and (1,2,3),(3,4,5) with multiplicity 6. Therefore the cubic has the three real-part terms in the proof. Their simultaneous phase upper bound is attained by real positive coefficients. For B=0 the cubic vanishes; for B>0 scale B to 1. At r=C/B>0, the symmetric order-two generalized Rayleigh problem with denominator diagonal (2,2+r^2) has a simple largest root and a strictly positive eigenvector. The first row yields A/B=3r/(lambda-3). For z=r^2 the resulting H(z) extends continuously to 0 with value 3/sqrt(2) and tends to zero at infinity. Independently differentiated H and verified the elimination identity; its quartic has signs +,-,-,+ at 0,1,3,4 respectively and exactly two positive zeros by Descartes. The unsquared derivative numerator is positive at 0 and negative at 1, with only one possible zero in (0,2); its polynomial part is already negative and decreasing for z>=2, discarding the other squared candidate. This gives the unique strict interior maximum. Saturation at positive cubic requires b's phase to be twice a's phase, b^3 positive real, and the sign of c to cancel the phase of ab. Thus a's phase is pi*j/3 and c's sign is (-1)^j, exactly the six translates; negation and real scaling give the full family. T=0 has only the first harmonic and zero cubic. Independent symbolic replay and 65-digit evaluation gave z=0.417702187780093249..., K=2.366495837333407468..., K^2=5.600302548116345338..., r=0.646298837829756003..., t=1.968699378731683822.... The frozen displayed decimals are consistent as rounded approximations; the exact formulas govern.

## originality

PASS

The same six-cycle problem and its resonances are in Chen–Lam–Lu §6.1. Their same-normalization six-cycle upper estimate 59/10 is not the exact best squared constant, and the inspected six-cycle argument does not classify extremizers. Xie–Zhang's general bound also does not imply this sharper value. The supported new claim is the exact optimization and all equality cases, not the setup or underlying resonance computation.

## value

PASS

C6 is an existing endpoint case of a studied cubic inequality: the preceding primary work explicitly separated and estimated that case. The result resolves its exact extremal problem and removes the gap between the upper estimate and an attainable profile. The structural output is that every nondegenerate equality signal has the same amplitude ratios and translation-locked phases, not merely a modest numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
