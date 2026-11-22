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

The standalone `verify.py` script uses only Python's standard library and independent direct enumeration of increasing partial injections: it does not construct these maps from the proposed fixed-point gap formula. It directly computes composition squares for every map in each size from zero to nine, groups the maps by their actual square targets, and compares each of the \(2^n\) target fiber counts against the predicted product of central trinomial coefficients. It independently generates coefficient arrays from \(T(z)^{k+1}\), verifies rank sums, and recomputes the logarithmic target-fiber moments via a separate weighted-renewal recurrence up to degree 100. The captured `verify_output.txt` records the counts and both `VERIFY_OK` and `ENTROPY_RECURSION_OK`.

The all-size fiber formula is proved by fixed-point separation and a unique disjoint-domain/image matching. The logarithmic Gaussian law is proved using the analytic family \(B_t(z)/(1-zB_t(z))\), its unique simple pole near \(z=1/2\), and cumulants from the differentiated renewal equation. No finite computation is treated as proof of an infinite family or limiting distribution.

The scalar coefficient triangle and its row-sum asymptotic were already published in OEIS A111960/A111961 and are not credited as newly discovered. The full text of a closely related 2015 enumerative semigroup paper remained unavailable for complete historical-priority comparison. Independent audit has not been performed.
