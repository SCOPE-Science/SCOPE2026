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
# Reproduction and verification

Run `python3 verify.py` with only the Python 3 standard library. The test explicitly constructs 32768 binary alternating matrices, computes their ranks by elimination, and performs three integer-valued complete Walsh transforms. It checks the eigenvalue triple and exact orbit multiplicity for each of the 32768 characters; it additionally checks the polynomial formulas and unique root for field orders 2, 3, 4, 5, 7 and 11. The expected final marker is `ALTERNATING_SIX_NEGATIVE_TYPE_SPECTRUM_PASS`. No finite computation proves the all-field statement; the proof in RESULT.md supplies the infinite quantification. Complete text of an identified 1975 association-scheme source remained inaccessible, which limits historical priority. No independent external mathematical validation has occurred.
