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

# Reproducibility and proof scope

Two independent Python 3 standard-library scripts are supplied in the same directory. Run `python3 verify_direct.py` and `python3 verify_motifs.py` from the extracted package. The first constructs every distinct deletion ball of each Dyck word for semilengths one through eight, builds graph edges by actual distinct output intersection counts, counts unordered triangles and compares with the stated closed sum. The second builds the canonical positive-vertex splice motifs directly and verifies the positive-height vertex count, uniqueness of all resulting triangles and all-range coefficients through semilength eight.

Both scripts ran successfully on the package source files; their final markers are `DIRECT_VERIFICATION_OK` and `MOTIF_VERIFICATION_OK`. Mathematical correctness for every semilength is proved in RESULT.md from the alternating-interval criterion, binary XOR interval classification and Catalan marked-vertex enumeration, not inferred from finite tests. Independent mathematical audit has not been performed.
