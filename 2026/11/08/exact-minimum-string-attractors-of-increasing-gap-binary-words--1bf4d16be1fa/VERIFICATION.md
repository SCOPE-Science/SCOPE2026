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

# Verification record

The accompanying standalone `verify_attractors.py` was run under Python 3 and completed successfully. It checks: (i) each gap tuple from the 465 increasing tuples of lengths 1 through 6 chosen from 1 through 9, with complete distinct-factor/attracted-factor comparison (118,977 total distinct-factor cells); (ii) exact minimum hitting-set sizes for 11 small words, computed independently by examining every position subset in increasing cardinality; and (iii) 19 further instances with larger strict gaps and up to 19 runs. Output ended `PASS`.

The mathematical proof in RESULT.md establishes the claim for arbitrary positive increasing gap values and arbitrary finite \(k\), beyond these tests. The verifier does not establish infinite quantifiers by itself. The key proof obligations are the classification of one-marker factors, uniqueness of the \(1\,0^{g_j}1\) factors, and the odd-\(k\) incompatible-factor argument. Every such step is explicit in the proof.

The comparison to published work is a self-review, not an independently certified absence of previous results. Independent scientific audit has not been performed.
