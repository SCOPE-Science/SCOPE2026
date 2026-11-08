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
# Reproduction and limits

Run the two standalone Python programs from this directory with `python3 weakorder_verify.py` and `python3 weakorder_spectrum_verify.py`. Their text outputs should exactly match `weakorder_logic_checks.txt` and `weakorder_spectrum_checks.txt` respectively. Both programs require only standard Python 3, no downloads or nonstandard dependencies.

The logical verifier independently constructs finite strict weak orders, computes stable non-counting tuple-extension color refinements on \(k\)-tuples, and compares the resulting theory signatures with the truncated ordered level words. The comparison counts by width are 7140 at width two, 3486 at width three, and 435 at width four, totaling 11061 pairs. It also checks minimum-representative composition counts through order twelve.

The separate size-spectrum verifier enumerates every positive-integer composition through the displayed ranges, counts distinct capped words realized at each exact total size, and compares those counts with coefficients derived from the proposed rational series. These are separate finite checks of examples; only the proof in `RESULT.md` covers all possible heights, level sizes and unbounded quantifier depths.

Self-review: passed. Independent audit: not yet performed.
