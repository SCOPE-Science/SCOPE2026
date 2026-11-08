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

# Reproducibility and limitations

Run `python3 verify.py` with the Python standard library; its exact-arithmetic output is recorded in `verification_output.txt`. The checker tests integer zero-sum vectors over a bounded grid for odd cardinalities 3, 5, 7, symbolic integer coefficient inequalities through 101 entries, and exact normalized extreme vectors for dimensions \(2\)–\(23\). This computational evidence is not a substitute for the all-real, all-dimensional analytic proof in RESULT.md. The checks do not cover arbitrary perturbations of the regular-simplex geometry or multistep behavior.

The manuscript supplies a complete proof for every \(n\ge2\); independent mathematical validation has not been performed.
