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

The public theorem follows from the transfer identity \(C_j(n)=u^\mathsf TH^np_j\) on the semigroup of four-state maps. `verify.py` generates all \(41\) states, constructs transitions and their fixed-point classes, checks the two rational generating-function identities exactly through the degrees required for \(41\) consecutive residual zeros, and invokes the finite-dimensional Cayley–Hamilton argument described in `RESULT.md` to cover all positive lengths. It also verifies the factor-three periodic exceptional target directly from the generator for output bit one.

Run `python3 verify.py` and expect `VERIFY_OK: 41 states, full all-length rational fiber spectrum`. The coefficient vectors for lengths \(1\) through \(6\) must be \((1,0,1,0)\), \((1,2,1,0)\), \((3,3,1,1)\), \((5,6,5,0)\), \((6,20,6,0)\), and \((12,41,10,1)\).

Run `python3 independent_check.py`. It separately evaluates the eight-entry Wolfram truth table on *every* indexed input up to length \(12\), counts the actual output fibers, and independently multiplies four-by-four labeled de Bruijn adjacency matrices for every output, comparing their traces with each directly enumerated predecessor count. Expect `INDEPENDENT_OK: all indexed rings through length 12`.

The second check is finite corroboration, not the proof of the all-length claim. Both scripts use only the Python standard library and hold no external dependencies. The research conclusion remains unverified by an independent scientific audit; source-priority risk is discussed in `REVIEW.md`.
