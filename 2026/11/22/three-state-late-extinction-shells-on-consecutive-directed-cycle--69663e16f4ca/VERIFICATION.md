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

# Reproducibility of the late extinction shells

The mathematical proof in `RESULT.md` is complete for all integers \(a\ge2\); finite calculations are supporting checks rather than a proof by enumeration.

Run `python check_direct.py`. It constructs the directed hub bouquet from explicit arcs, applies the AND rule to every labelled configuration and reports PASS for \(2\le a\le7\), covering 21,840 initial states including the distinguished all-one states. Each late extinction shell is checked by its first-entry time and the number of initially zero vertices.

Run `python check_walk.py`. It independently propagates predecessor sets along directed arcs and enumerates nonempty missing-source subsets, verifying the full polynomial coefficients at every time \(E-k\) for \(1\le k\le a\), as well as extinction at \(E\), for all \(2\le a\le40\). This is a separate representation of the graph dynamics.

Both commands were executed successfully from the packaged source files. The tests are finite and cannot, by themselves, establish the universal quantifiers, which are proved via the semigroup argument in `RESULT.md`. No independent external audit has been performed.
