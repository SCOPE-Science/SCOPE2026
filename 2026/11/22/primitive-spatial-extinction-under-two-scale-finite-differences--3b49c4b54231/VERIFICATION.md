---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The exact kernel formula was checked from the shift-module polynomial representation: for each divisor period, multiplying by the two-scale difference polynomial has kernel degree given by the union of roots of two binomial factors. The primitive total follows from exact divisor Möbius inversion; the spectral decomposition proves the existence condition and the nonzero-map arithmetic boundary.

Run `python3 check_two_scale.py` with the bundled file and no third-party packages. The actual check passed 58,939 directly enumerated configurations over finite fields of characteristics 2, 3 and 5, across 110 stride-pair/ring-length comparisons. These finite checks are corroboration, not proof of the unrestricted statement.

Independent mathematical validation was not performed. The result concerns one-step zero outputs on cyclic rings of length coprime to field characteristic. Prior general classifications might subsume the specialization; historical priority remains provisional.
