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
# Verification and scope

Run the embedded executable `verify.py` with a standard Python 3 interpreter. The unmodified executable was run from the embedded source, and its stdout is saved as `verification_output.txt`.

The verifier independently builds the cellular boundary of the doubled complete graph and the multidegree-local three-term cochain complex from the Lü–Panov cellular model. It checks the exact rational ranks, the vanishing of the composite differential, and the positive cohomology ranks \((k-1)^2\) at each support size. It then tests signed, oriented cellular graph action; signed exterior Koszul action; the cycle-index trace formula; and invariant dimensions under all permutations for every \(2\le n\le6\). The standard-library script uses exact rational arithmetic and integer combinatorics.

The finite exhaustive tests do not verify the infinite theorem; the proof depends on the explicit all-size cellular decomposition, sign-representation multiplicity, and rational orbit-space transfer. No external independent audit or computational formalization was performed.
