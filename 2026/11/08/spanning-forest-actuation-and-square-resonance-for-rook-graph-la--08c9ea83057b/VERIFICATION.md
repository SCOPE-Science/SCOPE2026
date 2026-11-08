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

The exact all-parameter argument is in RESULT.md. The included `verify_rook.py` independently checks the PBH eigenspace ranks and the combinatorial forest/component criterion, using modular ranks which equal rational ranks for all tested matrices by Hadamard's bound. Execute `python3 verify_rook.py` in the directory containing the extracted files.

The verifier exhausts all actuator subsets of boards \(2\times2\), \(2\times3\), \(2\times4\), \(3\times3\), and \(3\times4\), and all 11,440 minimum-size candidates of \(4\times4\). Expected minimum counts are respectively 4, 12, 32, 36, 432, and 3,936. These finite computations do not prove the infinite family; the stated proof does. No independent external audit has been carried out.
