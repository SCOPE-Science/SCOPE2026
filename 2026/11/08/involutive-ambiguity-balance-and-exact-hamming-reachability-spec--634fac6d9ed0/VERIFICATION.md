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

# Reproducibility and verification

Run `python3 check_reachability.py` with Python 3 standard library. The checker evaluates the defining four-by-four truth-meet and warrant tables on every ordered pair of \(n\)-coordinate states for \(1\leq n\leq5\). The tested pair count is \(16+256+4096+65536+1048576=1118480\). It independently tests the source-conditioned Hamming-count formulas and aggregate counts; through \(n=4\), it checks the explicit source-preserving involution on all \(69904\) ordered pairs. It checks the number and form of universal sources through \(n=5\).

Expected final output is `ALL CHECKS PASSED`. This was obtained by executing the included checker. The analytical arguments in RESULT.md, not finite experiments, prove the statements for all \(n\geq1\).

The study treats potential ordered pairs on the full four-valued product; without specifying actual move edges, it does not count a particular game's physical transitions. No independent mathematical or historical-priority audit has been performed.
