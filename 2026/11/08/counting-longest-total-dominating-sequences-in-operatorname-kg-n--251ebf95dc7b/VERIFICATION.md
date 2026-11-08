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

This package includes three standard-library-only Python 3 programs and their recorded stdout text. Run `python3 verify_canonical.py`, `python3 verify_endpoint_partitions.py`, and `python3 verify_labelled.py`. The first two are exhaustive for the all-order six-term theorem because they enumerate all equality patterns on at most twelve endpoint slots; they are not empirical sampling. `verify_labelled.py` tests the original graph adjacency and domination predicate independently for \(n=5,6,7,8\). The labelled checker was additionally exercised through \(n=9\) in extended mode, although the included deterministic reference output is the shorter default run.

`verify_canonical.py` records 2,200 valid six-edge first-appearance patterns, a complete support/paired-birth histogram, and the exact coefficient list. `verify_endpoint_partitions.py` independently records 51,776 valid oriented endpoint partitions and the identical coefficients. Both check the complete remaining two-cover predicate before accepting a leaf; both report zero six-edge patterns with support above nine. The dynamic finite-graph test reports 36,720; 466,560; 3,175,200; and 14,968,800 ordered maximum sequences. The code and expected counts are included here and do not depend on external scripts or data.

The published six-step extremal length is also reproved by exterior algebra in `RESULT.md`. Reproducibility is same-package algorithmic reproducibility, not independent scientific certification. Historical novelty remains unverified outside the inspected sources.
