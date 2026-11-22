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

# Reproducibility and limits

Run `python3 verify_sharpness.py`. Expected line: `TAGGED_PARTS_SHARPNESS_OK nonleading_finite_pairs 11 coefficient_assertions 15 depths 3`. The script checks first-two-column minors and the exact starting value using integer arithmetic; its eta-quotient calculation uses modular integers through index 648 (3-adic precision 30) and checks three sample depths. These checks are finite and supplementary. For the infinite claim, the proof of the new unique-minimum induction uses Li–Tang (2026), Lemma 5.2(ii), which applies to all levels and indices, and Theorem 3.2's coefficient recurrences. Full mathematical independence or external certification has not been claimed.
