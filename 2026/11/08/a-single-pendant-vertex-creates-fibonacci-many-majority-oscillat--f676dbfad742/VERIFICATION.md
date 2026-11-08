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

# Reproduction and mathematical limits

For all labelled one-leaf cycles \(n\ge3\), the proof reduces the two-time periodicity equations to a 16-state exact transfer. Run `python checks/check_symbolic.py` with Python 3 and SymPy to regenerate the 16-state matrices, verify the explicit matrix annihilator by exact integer arithmetic, factor the two local transfer characteristic polynomials, and compare the six necessary starting traces. A linear recurrence then proves the closed formula for all lengths; the finite program does not by itself certify the infinite statement without that induction argument.

Run `python checks/check_direct.py` with Python 3 (standard library only) to enumerate all \(2^{n+1}\) initial states on each one-leaf cycle for \(3\le n\le13\), perform the actual graph updates twice, check fixed and primitive-two states, and independently verify the bare-cycle comparison. Captured outputs are at `checks/symbolic_output.txt` and `checks/direct_output.txt`. Both were reproduced from the supplied scripts and matched exactly.

The sole nontrivial computational certificate is the exact polynomial annihilator for the fully defined 16-by-16 transfer matrix. Its complete definition and a program checking every matrix entry are included. No floating-point approximation, truncation of a search tree, timeout, probabilistic test, or unidentified external dependency enters the proof. The formula does not claim information about transients, basin volumes, or other update conventions.
