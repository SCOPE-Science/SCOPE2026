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

# Verification of the cyclic period-three zeta factorization

Run `python3 checks/exact_transfer.py` and `python3 checks/parity_projection.py` from this package root. Both programs use the Python standard library only and were run successfully on these exact embedded sources.

The first generates the independent 32-state de Bruijn automaton from the eight forbidden six-bit patterns, checks 56 allowed directed transitions, computes its entire 32-by-32 characteristic polynomial with an exact-integer Faddeev–LeVerrier algorithm, and verifies the claimed degree-24 determinant polynomial and eight zero eigenvalues. This is an all-length exact matrix identity, not a sampled recurrence.

The second constructs the signed two-bit-state transfer matrices from scratch, recomputes the parity decomposition for 72 lengths, and brute-force verifies every binary marked word through length 17. The resulting first 18 counts are \(0,2,0,14,20,56,70,134,216,442,814,1592,2756,5070,9080,17158,31552,58664\).

These checks support the stated finite linear-algebra identities and their independent finite cross-checks. Neither script provides an independent human mathematical audit; the formal all-length proof is the cyclic difference kernel/image argument together with the determinant identity.
