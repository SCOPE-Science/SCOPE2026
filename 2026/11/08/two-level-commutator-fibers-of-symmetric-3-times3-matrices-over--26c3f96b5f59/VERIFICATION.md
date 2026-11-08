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

The result is proved algebraically in RESULT.md. Computational checks are supplemental and do not establish the unrestricted parameter range by themselves.

Compile `check_symmetric_commutator.cpp` with `g++ -std=c++17 -O2 check_symmetric_commutator.cpp -o check_symmetric_commutator` and run `./check_symmetric_commutator`. Its output must match `verification_output.txt`; the final marker is `SYMMETRIC_COMMUTATOR_ALL_CHECKS_PASS`. Over \(\mathbb F_3\), the checker directly multiplies all ordered input pairs. Over \(\mathbb F_5\) and \(\mathbb F_7\), it enumerates every first input and reconstructs all target fibers from the exact linear image and kernel size for the second input.

Run `python3 check_fourdim_boundary.py`. Its output must match `fourdim_output.txt` and end with `FOURDIMENSIONAL_NONUNIFORMITY_WITNESS_PASS`. The latter program uses matrix multiplication and modular Gaussian elimination rather than a hand-entered rank table.

Unproved by these finite experiments alone: extension-field cases, all higher dimensions, and the absence of an equivalent theorem in the literature. The proof in RESULT.md covers every odd prime power in dimension three and the specified dimension-four boundary; no independent audit is asserted.
