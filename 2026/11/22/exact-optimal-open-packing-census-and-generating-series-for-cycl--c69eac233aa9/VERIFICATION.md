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

# Verification and limitations

The exact proof is the local cyclic-word equivalence, transfer determinant factorization, and symbolic coefficient extraction in `RESULT.md`. Programs test independent portions of that derivation.

* Run `python3 verify_transfer.py` to enumerate permitted cyclic words over several clique orders and circumferences; recorded output is `transfer.log` ending in `TRANSFER_VERIFIED`.
* Compile `verify_direct.cpp` with `g++ -O3 -std=c++17 -o direct verify_direct.cpp` and execute `./direct`: independently construct graph neighborhoods and enumerate actual vertex subsets in six instances of up to 24 vertices; `direct.log` ends in `DIRECT_VERIFIED`.
* Run `python3 verify_symbolic.py` with SymPy installed to verify the two characteristic factors and their product against full transfer determinants for three clique orders; `symbolic.log` ends in `SYMBOLIC_VERIFIED`.

These finite tests do not certify the unrestricted theorem or an exhaustive literature claim; the proof is written in the main result. The previously known scalar maximum is expressly credited. No independent audit has been performed.
