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

Reconstructed the normalized singular spectrum (12/13, (1/13) repeated 12) of J_13-I_13 and Levene tree tridiagonal trace-norm lower bound. The positive 36-entry depth profile has S=5606050 and H=4330856. Leading 2-by-2 pinches yield integer radicands 146131600000000 and 3131600000000 with strict square-root floors 12088490 and 1769632, respectively. Recomputed rational lower surplus 7053468/1625>0, so the finite graph multiplier exceeds 2+7053468/(1625*5606050). Compressing any n>=13 crown-and-trees to 13 shore pairs proves the assertion for all n, not by extrapolating finite tests. The cited 2026 Levene tree trace-norm theorem is a necessary external premise; independent arithmetic confirms its application, not a new proof of that theorem.

## originality

PASS

The ORIGINAL claim that n>=13 is a new family productivity cutoff was superseded by a published n>=12 construction. The REPAIRED final claim is narrower: a concrete exact witness at 1000 branching and 35 height for n=13,14, compared with the n>=12 construction requiring 10000 branching and height100. A separate n>=15 witness at 1000 branching/height12 does not cover n13 or14. No inspected theorem implies the reduced-parameter certificate; originality is restricted to this quantitative witness, with same-day priority explicitly uncertain.

## value

PASS

The quantitative certificate is motivated by the natural resource-complexity question for a productive crown core: it reduces branching tenfold and height from 100 to 35 at orders13 and14 relative to the known n>=12 witness, while a faster 1000/12 certificate covers only n>=15. The precise smaller attachment bound can guide finite Schur multiplier constructions. The original qualitative cutoff claim would not be valuable independently and has been removed in full revised RESULT/SLOGAN.

The dated certificate retains the supplied scientific assessment, sources and limitations.
