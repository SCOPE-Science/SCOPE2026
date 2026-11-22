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

# Reproducible checks and their limits

The companion standalone `verify.py` uses only Python 3's standard library. Run `python3 verify.py` in a directory containing this extracted file.

The symbolic checker creates every triple of nonempty color supports \((S,T)\) and a pointed color \(c\in S\), reconstructs the exact list of successor descriptors and exhaustively performs one-step modal partition refinement. Its printed counts are:

- Two colors: `2,4,6,6,6` over 12 color-support states.
- Three colors: `3,15,51,51,51` over 84 color-support states.
- Four colors: `4,48,356,356,356` over 480 color-support states.

In addition, the checker directly compares every pair of color-support states with the claimed depth-two descriptor, rather than merely comparing the resulting cardinalities.

A second independent routine enumerates all labelled finite valuations of \(K_{m,n}\) for \(1\leq m,n\leq3\) on alphabets of sizes two and three, builds each concrete graph's neighbor sets, and computes the semantic refinement from vertex truth vectors. This independently checks 196 two-color models (952 pointed worlds) and 1521 three-color models (7956 pointed worlds), with depth profiles `2,4,6,6` and `3,15,51,51`. It cross-checks the entire depth-two partition with the predicted descriptor.

These are actual finite checks rather than proofs for arbitrarily large alphabets. The structural induction in `RESULT.md` is the evidence for the universal theorem. No proof assistant or external mathematical audit is claimed; historical priority is provisional.
