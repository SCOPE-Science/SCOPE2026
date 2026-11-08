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

# Verification and limits

Execute `python3 verify_heawood_two_ind.py` from the same directory as this file. The program needs only Python's standard library; no external datasets or output artifacts are read. Its first checks reconstruct the graph and all \(16384\) possible vertex subsets, comparing independent connected-component and induced-degree membership tests. It then constructs the complete discrete-Morse matching and verifies acyclicity by topologically sorting every covering relation of the nonempty face poset. It also computes separate mod-two boundary ranks and all \(336\) automorphism traces by two unrelated finite formulas.

The included `verification_output.txt` records the complete output of the program from the final assembled scientific files. The successfully checked lines are `nonempty=2256`, `morse_pairs=1121`, `hasse_covers=10150`, `aut_group=336`, the trace histogram, and `ALL_CHECKS_PASS`.

The finite checks certify the mathematical statements only conditional on the stated graph encoding, standard discrete-Morse and Lefschetz theorems, and correctness of the readable script. Homotopy and rational module deductions are explained in `RESULT.md`. No independent external audit or infinite-family proof is claimed.
