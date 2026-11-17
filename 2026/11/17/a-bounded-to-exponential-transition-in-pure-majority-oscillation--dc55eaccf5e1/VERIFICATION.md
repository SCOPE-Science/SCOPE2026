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

The direct simulator `verify_direct.cpp` enumerates every binary configuration on the labelled graphs for clique width 3 and circumferences 3–7, and clique width 4 and circumferences 3–6. Its output is recorded in `direct_output.txt`. This checks 20,292,096 states and uses the graph's actual neighbor list, not the transfer definition.

The separate `check_transfer.py` builds the 36 by 36 matrix from balanced four-bit columns and forbidden equal triples, verifies exactly 90 transitions, performs exact integer characteristic-polynomial verification with SymPy and verifies trace counts for circumferences 3–12. Its output is in `transfer_output.txt`. It verifies exact rational sign intervals for all three cubic roots and an exact integer Schur-Cohn certificate placing both quartic root sets strictly inside the radius-two disk. It also approximates eigenvalues as an independent numerical diagnostic. The exact determinant identity and the local transfer bijection prove the all-length counting formula.

Limitations: finite simulation does not itself prove the infinite-family statement; the additional root-bound certificate uses an exact polynomial reduction and not merely floating-point estimation. The precise factorization can be reconstructed from the explicit integer matrix; the main exact count requires no numerical roots. Independent external validation is not performed.
