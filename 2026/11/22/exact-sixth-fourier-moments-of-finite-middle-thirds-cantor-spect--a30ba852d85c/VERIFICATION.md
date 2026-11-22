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

# Verification

The proof gives a complete correspondence between ordered six-tuples of integer digits and length-\(k\) closed carry paths through the three states \(-1,0,1\). Its exact two-state transfer has characteristic polynomial \(t^2-26t+90\). The standalone `CHECK.py` independently enumerates all triples for \(0\le k\le8\), compares the resulting squared histograms with the transfer recurrence, and checks complete sumset intervals, carry weights and 30 additional recurrence values.

The observed independent enumeration result was: `PASS: 9 independently enumerated levels; carry matrix; 30 recurrence steps`.

The all-depth proof is mathematical rather than based on finite enumeration. Literature comparison is limited to the identified materials; the exact continuous \(q=2\) spectral root was established previously, and independently audited priority has not been established. This artifact does not assert any external certification.
