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

# Verification of the marked-query double-star polynomial

The all-parameter proof is the complete centre-profile case analysis in `RESULT.md`; empirical tests are supplementary checks, not a replacement for the proof. Run `python3 verify.py` with Python 3.10 or later and no third-party dependencies.

The actual script was executed against eleven double stars with leaf-count pairs \((1,1),(1,2),(2,1),(1,3),(2,2),(1,4),(2,3),(3,2),(1,5),(2,4),(3,3)\). It enumerated all proper three-colourings of each tree and all supports containing either zero or one named target per vertex. This covers \(256256\) support configurations in total. For each, it computed the entire binary trace and separately tested the two-hub feasibility criterion, with no disagreements. It checked every exact polynomial coefficient in each case and the highest coefficient independently. It also performed exact-integer arithmetic checks of polynomial nonnegativity, length, initial coefficients and highest coefficient for \(121\) parameter pairs with \(1\le a,b\le11\).

The checker's summary was: `PASS 11 trees, 256256 complete query-support profiles; full traces, centre profile, all coefficients, and top coefficient agree.` The subsequent arithmetic checks passed. Exact traces were checked for finite trees of at most eight vertices; neither this finite range nor the arithmetic checks certify all positive integer parameters. The unbounded theorem follows from the general proof. No Lean or external certification is claimed, and independent mathematical audit is not performed.
