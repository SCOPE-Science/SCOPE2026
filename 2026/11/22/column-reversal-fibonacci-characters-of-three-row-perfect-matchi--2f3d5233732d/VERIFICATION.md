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

# Reproducible verification

Run `python3 verify.py` in this directory using Python 3.8 or later; no third-party packages are needed. `verification_output.txt` records the actual standard output from the package's checker.

The checker constructs all fourteen reachable nonzero bitset states from the explicitly specified domino/monomer selection rules, computes the weighted integer transition matrix and terminal vector, constructs the residual \(r=(T^4+T^2-I)w\), and verifies all fourteen exact scalar moments \(e_1^{\mathsf T}T^jr=0\) for \(0\le j\le13\). Cayley–Hamilton extends these finite equalities to every later moment, proving the all-length recurrence. The checker compares traces against the Fibonacci formula for \(1\le n\le30\).

As a separate finite cross-check, the same program enumerates **all** domino tilings of the original \(3\times2n\) rectangle for \(1\le n\le6\); it directly lists every reflection-invariant face as a union of edge orbits, verifies that each such face extends to a reflection-invariant full matching, and computes its alternating orbit count. This verifies the transfer interpretation for these six widths but is not a replacement for the total-unimodularity extension lemma or the infinite recurrence proof.

The nonequivariant homology concentration and Fibonacci rank are supplied by a published primary theorem (arXiv:2611.18058, Theorem 3.5). The checker does not independently prove that source theorem. No independent expert validation, full integral equivariant homotopy identification or worldwide priority certification is asserted.
