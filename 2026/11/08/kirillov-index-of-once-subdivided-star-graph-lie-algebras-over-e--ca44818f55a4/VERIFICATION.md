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

# Verification details

The proof in `RESULT.md` establishes a global upper bound on an arbitrary functional's Kirillov form using the mixed block's column structure and alternating rank parity. An explicit functional attains that bound; the proof of its rank uses the restriction of the vertex-edge form to the mixed-block kernel and works over every field.

To check calculations independently, run `python3 check_index.py` with Python 3.8 or newer. It constructs the graph vertices and edges and finds every length-two path without using any precomputed Lie matrix. It then constructs the Kirillov matrix from the defining path brackets and computes exact ranks in four prime fields for each of the first ten arm counts. It also tests all coefficient functionals over the binary field for one, two and three arms. The expected output is recorded in `check_output.txt`. The checked package includes all dependencies (Python standard library only).

Replay output: `VERIFY_OK witness_cases=40 exhaustive_binary_functionals=4232 m_range=1..10 prime_fields=2,3,5,7`.

The exhaustive binary checks cover precisely 2^(2+1)+2^(4+3)+2^(6+6)=4,232 functionals, not arbitrary arm counts or larger fields. The remaining 40 matrices certify finite instances of the explicit witness, not all possible functionals. The unrestricted theorem is justified by the written argument, not by these finite tests.

No independent audit has been performed.
