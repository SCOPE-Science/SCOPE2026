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

# Verification and limitations

The public reproduction program `verify_cycle_mis.py` uses only Python standard-library arithmetic. Execute with `python verify_cycle_mis.py`. It reconstructs maximal independent sets directly from independence and domination, and does not rely on the forbidden-gap classification to create those concept families.

For each cycle length \(3\le n\le18\), the program independently forms the trace family on every one of the \(2^n\) vertex supports, compares its size with \(2^{|S|}\), compares that result to the proposed cyclic-gap test, and checks every coefficient of the closed sum. The total number of individual supports inspected is \(524280\). Additional formula and dimension-boundary checks cover lengths \(19\) through \(90\).

Observed output: `MAXIMAL_CYCLE_SHATTERING_PASS supports= 524280 direct_lengths=3..18 formula_boundary_lengths=19..90`.

These computations are finite consistency checks, not a proof for unbounded lengths. The unrestricted conclusion rests on the private-neighbor witness lemma, gap-block construction, and cyclic-rooted enumeration in the proof. Historical priority remains conditional on available literature. Independent review has not been conducted.
