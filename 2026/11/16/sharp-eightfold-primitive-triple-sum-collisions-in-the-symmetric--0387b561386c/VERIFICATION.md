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

# Reproducible checks

Execute `python check_a.py` and `python check_b.py` with a standard Python 3 interpreter. Both programs use only the standard library, enumerate unordered triples, discard opposite pairs, and independently verify sharpness and the exact closed formula over their stated finite ranges. Recorded successful outputs: `PASS exhaustive 4096 all nonzero integers; positive max 8 exception_count 10`; `PASS formula / independent exhaustive sums 8192 max 8`.

To make the finite enumeration mathematically complete for each examined nonzero target, the programs use \(\max|a_i|\le4|D|\). Any primitive triple has no pair of equal magnitude with opposite signs. If its largest magnitude is \(P\), the two other terms either fail to offset it by at least \(P/4\), or are both the opposite half-sized power and make sum zero. Hence the cutoff contains every primitive triple for each examined nonzero target. The full theorem for unbounded targets is established by valuation analysis, not extrapolation from finite checks. No independent audit has been performed.
