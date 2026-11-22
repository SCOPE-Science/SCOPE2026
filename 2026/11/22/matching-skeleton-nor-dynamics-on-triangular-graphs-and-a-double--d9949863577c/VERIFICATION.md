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

`verify_symbolic.py` is a standalone Python 3 program using only the standard library. Run `python3 verify_symbolic.py`; it computes component-clean counts from an EGF recurrence, enumerates all matchings and admissible clique partitions, and independently checks the entire orbit/basin map against direct open NOR updates for every initial state at \(n=3,4,5,6\).

`verify_independent.cpp` is an independent C++17 implementation using open-neighbor bitmasks and its own theoretical matching recursion. Compile with `g++ -std=c++17 -O3 -Wall -Wextra -pedantic verify_independent.cpp -o verify_independent` and run `./verify_independent`. It checks every state at \(n=3,4,5,6,7\), including the complete orbit-key basin dictionary and the general one-step periodic-entry identity. The largest case is \(2{,}097{,}152\) states.

`symbolic_output.txt` and `independent_output.txt` contain the actual successful outputs. The proofs of the exact image and basin identities and the asymptotic rare-defect law are symbolic and all-size; finite verification does not establish an infinite statement. The full public claim is restricted to synchronous open NOR on \(L(K_n)\), \(n\ge3\). Historical-priority certainty and external independent review are not asserted.
