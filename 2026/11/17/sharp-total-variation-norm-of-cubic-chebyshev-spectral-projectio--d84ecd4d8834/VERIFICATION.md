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

The reproducer is `CHECK.py`, executed with Python 3 standard library only. The checker computes rational Sturm variations 3 and 2 at \(4/9\) and \(1\), validates exact polynomial identities, proves the complete lower-parameter grid enclosure strictly less than \(49/20\), and verifies the strict analytic witness above \(49/20\). The complete-range conclusion depends additionally on the proved global derivative bound \(|H'|<80\) and the analytic two-root integral formula. Decimal prints are informational and do not certify an infinite statement.

The input class is the real bounded-variation space on \([-1,1]\); input point values do not affect the weighted integral, whereas any endpoint spikes are accounted for on the right side by ordinary variation. Certificate and mathematical proof establish the claim for all such inputs, not just tested samples.

Self-review: passed. Independent audit: not yet performed.
