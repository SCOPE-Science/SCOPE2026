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

# Verification

Execute `python3 verify.py` from the directory containing the attached files. The program uses only the Python standard library, enumerates the graph and all perfect matchings, constructs every simplex and every Morse pair, and tests the entire directed Hasse graph for acyclicity. Its complete expected output is included as `verification_output.json`; its finite pair list and critical faces are reproduced in `MORSE_CERTIFICATE.json` and its group character in `SYMMETRY_TABLE.json`.

The critical-cell profile is one zero-cell, one one-cell and seven two-cells. The exact signed Morse boundary is `[-1,-1,0,0,-1,0,0]`; the unit coefficient is the substantive integral proof ingredient that removes the one-cell and one two-cell. Exhaustive signed fixed-face traces for all twenty dihedral symmetries independently reproduce the rational character values. Run `python3 direct_check.py` for an independent simplicial boundary-rank computation modulo two, three and five; the recorded output is `direct_check_output.txt`.

This finite verification proves only the stated ten-vertex complex. Neither execution transcripts nor numerical modular checks replace the integer Morse proof, and no mathematical review by an independent party is asserted.
