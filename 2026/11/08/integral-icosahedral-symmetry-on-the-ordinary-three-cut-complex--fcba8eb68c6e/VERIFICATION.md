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

Run `python3 verify_icosa_equivariant.py` from the directory containing the embedded file; it requires only Python 3.9 or newer. `verify_output.txt` records the successful execution of the identical source file.

The code independently enumerates direct cut faces and the Alexander dual on all vertex subsets, validates each of the sixty free-face collapse pairs against the *current* complex, compares signed boundary ranks over the fields of orders two, three and five, and checks all 120 automorphisms. In particular, the signed Lefschetz character is separately computed on the full cut complex and on its dual for each automorphism.

These finite checks verify the stated **finite graph** and its integral structural proof. Computed ranks over fields are corroboration; the proof of integral module structure is the explicit elementary collapse, relative-chain argument and equivariant Alexander duality. The proof does not claim an equivariant CW decomposition or a theorem for other graphs. No independent external audit has been performed.
