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

# Verification and reproducibility

The result concerns independently uniform binary words and the number of distinct words remaining after exactly two disjoint length-two deletion bursts. Run `python3 checker.py` from the folder containing the two files `RESULT.md` and `checker.py`, or with only the checker present; no external packages are required.

The checker calculates each sphere directly from all admissible pairs of deletion intervals. Separately, it calculates the symbolic canonical-history expression from delayed comparison indicators. It exhausts all binary source words at lengths 4 through 13, computing moments as exact fractions, then checks 1,000 longer pseudorandom examples. Expected final output ends with `PASS: 17368 source words; exact direct-channel and moment checks`.

The all-length variance and limit theorem are justified by the symbolic derivation in `RESULT.md`; enumeration is finite corroboration and not proof of the asymptotic assertion. The canonical-representation input is the published Propositions 1–2 in arXiv:2606.01245. The independent audit status remains unperformed.
