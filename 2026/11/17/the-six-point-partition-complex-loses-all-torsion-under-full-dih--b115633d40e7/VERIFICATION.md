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

# Reproducible verification

Execute `python verify_partition_dihedral.py`. This uses only Python's standard library and reconstructs every intermediate object directly from the mathematical definition. It checks Burnside's lemma against the independently enumerated face-orbit counts, exact vanishing of successive boundary compositions, every integral coefficient-one algebraic cancellation, and that the final matrices vanish with ranks \((1,0,0,12)\).

The recorded stdout appears in `verification_output.txt`; the output is not substituted for the executable checks. Exact integer arithmetic is used throughout. The separate simple-connectivity argument and homological-to-homotopical passage are given in `RESULT.md`; those mathematical deductions do not follow from matrix output alone. No independent audit has been performed.
