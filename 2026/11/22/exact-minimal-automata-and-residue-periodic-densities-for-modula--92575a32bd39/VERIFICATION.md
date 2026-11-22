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

The all-parameter proof is in `RESULT.md`. Its crucial nonstandard step is the **left** stabilizer calculation for the Boolean accepting set; a right stabilizer would not by itself prove Myhill–Nerode minimality. The group law, commutators and period are checked algebraically in the proof.

Run `python3 check_group.py` to enumerate the actual counting DFA and minimize it through partition refinement for seven small parameter pairs, then compare direct word enumeration through length eight. Run `python3 check_stabilizer.py` to compute the full left accepting-set stabilizer by finite group multiplication. Run `python3 check_asymptotics.py` to propagate exact counts of accepted words to length forty and display the prime-modulus density convergence. These programs require Python 3 and the standard library, and their recorded outputs are embedded beside them.

Finite tests do not establish the claim for arbitrary alphabet sizes or moduli, nor do numerical proportions establish a limit. Those assertions rely on the general proof and standard finite periodic Markov-chain convergence. No independent external audit has been conducted.
