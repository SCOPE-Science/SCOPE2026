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

# Verification and limits

The proof uses the classical Erdős–Wintner existence-and-continuity theorem, Mertens' product theorem, the prime-counting bound \(\pi(y)\ll y/\log y\), and elementary Chinese remaindering. It does not rely on a computer to establish an infinite statement.

Run `python CHECK.py` in the same directory. The test program checks exact fractions for \(w(n)/n\) up to index \(4500\), exact local valuation frequencies on finite prime-power periods, and independent-cylinder upper-product inequalities. Passing results test implementations and finite identities, not infinite correctness or priority. The pointwise density limit is taken before the small-threshold limit. No independent external audit or validation has been performed.
