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

# Verification record

The claim is proved for all integers \(n\ge2\) by the frontier-tour induction in `RESULT.md`. Finite computation is a cross-check, not a substitute for the infinite argument. The attached C++ source was previously compiled and executed for every initial spine rotor configuration at \(2\le n\le12\), with reported maximum delays \(3,10,21,36,55,78,105,136,171,210,253\) and unique maximizers in each size.

The check represents each rotor by an index into a fixed, ordered neighbor array and advances the rotor before moving the chip. It recognizes recurrence only when there is exactly one directed two-cycle and the chip occupies one of its endpoints; this is equivalent to the unicycle criterion on a tree. There are \(4\cdot3^{n-2}\) initial spine rotor assignments for \(n\ge2\). The complete-state dynamics is finite, so the traversal terminates; the proof provides an upper bound without relying on the program's timeout threshold.

The scientific conclusion is restricted to the specified graph, starting vertex and cyclic orders; the independent audit has not been performed. Historical-priority gaps remain possible.
