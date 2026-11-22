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

# Verification scope

Run `python3 check_words.py` and `python3 check_partition.py` using Python 3 with its standard library. Their frozen expected stdout is in `check_words_output.txt` and `check_partition_output.txt` respectively. The first program directly selects positions, counts pattern pairs/triples and checks every fixed-composition class and unique endpoint through \(a,b\leq7\). The second program computes joint generating coefficients via gap-by-gap multiplication and independently counts bounded partitions through \(a,b\leq10\). It checks all joint multiplicities, not just first moments or extrema.

The infinite claim does not follow from these tests. Its proof uses the unique word-to-gap bijection, the identity \(T=at-\sum_i x_i^2\), strict balancing and strict transfer to boundary entries. The cases \(t=0\), \(t=ab\), \(a=1\), \(b=1\), and both remainder-zero situations are covered by the same proof. An external scientific audit has not been performed, and literature priority beyond the inspected material is unverified.
