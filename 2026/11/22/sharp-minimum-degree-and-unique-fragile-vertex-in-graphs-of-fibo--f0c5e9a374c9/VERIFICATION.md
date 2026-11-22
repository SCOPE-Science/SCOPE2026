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

# Reproducibility

Run `python3 verify.py` alongside this document. The output was `VERIFY_OK parameter_pairs=63 admissible_words=16018`. The program tests each of 63 pairs for integer `q` in 2–8 and length `n` in 1–min(12,q+4), generating admissible binary words, calculating exact one-coordinate-flip degrees, and comparing all asserted minima and their multiplicities, including the named extremizers.

The all-length proof is in RESULT.md. Enumeration up to finite limits cannot itself establish the infinite parameter statement. The verification does not establish historical originality, connectivity, or Hamiltonicity.
