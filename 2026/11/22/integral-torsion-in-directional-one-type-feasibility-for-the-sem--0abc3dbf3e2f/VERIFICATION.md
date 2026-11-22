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

The theorem has a deductive integral-lattice proof in `RESULT.md`. The independently implemented finite checker `VERIFY.py` requires Python 3 and SymPy 1.13 or later. Run `python VERIFY.py` in the folder containing the files. Its final line is `VERIFY_OK`.

Checks executed: exact Smith forms of compressed matrices for \(k=1,2,3,4,5\); direct enumeration of all admissible one-point extension patterns over eight finite named examples; \(4130\) exact directed pair-feasibility tests against the parity definition; exact Smith forms of all eight corresponding uncompressed feasibility matrices. The listed tests do not replace the all-size proof, and do not survey the mathematical literature exhaustively.

No independent mathematical audit or external proof certificate is asserted.
