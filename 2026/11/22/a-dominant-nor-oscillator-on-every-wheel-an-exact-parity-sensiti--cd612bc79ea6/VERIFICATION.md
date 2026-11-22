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

# Reproducibility

The included `verify_bruteforce.py` independently constructs each wheel from an edge set, computes every synchronous update, and for each \(3\le n\le13\) examines all \(2^{n+1}\) initial states. It verifies the one-update cutoff, the two-point designated orbit, the exact basin count, the total-domination count, and the Lucas formula.

The separate `verify_transfer.py` uses a two-state matrix product to count cyclic words without adjacent zeros, checks direct cyclic-word enumeration for lengths 2 through 18, and checks the Lucas identity and mod-four correction through length 60.

Run using Python 3: `python verify_bruteforce.py` and `python verify_transfer.py`. Neither script requires third-party packages. They each print a final PASS line after all assertions. Computations are corroboration only; the infinite family is established by the proof in `RESULT.md`.

The reported review is a scientific self-review. No independent external validation has been performed. Historical uniqueness is not certified.
