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

# Verification

Run `python3 verify.py` in the same directory as the result. The script uses the standard library only and is an exact finite-state decision procedure for all output word lengths, not a simulation with a cutoff. It enumerates the complete 17-state synchronized subset graph of the two-step de Bruijn machine and the forbidden-pattern automaton. Every reachable pair must reject exactly the same letters, and every successor pair must already belong to the closure. Additionally, independent raw-input enumeration checks output lengths one through eleven and the linear recurrence through length seventeen.

The proof of the entropy uses the explicit six-state integer adjacency matrix, the exact polynomial identity \(\det(I-zA)=1-2z+z^4+z^6\) and a standard Perron–Frobenius argument. Numerical approximations identify roots but do not prove polynomial identities or all-length language equivalence.

No independent external mathematical audit has been performed, and the analysis does not cover further iterations of the automaton.
