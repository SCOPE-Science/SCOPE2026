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

`verify.py` is a standalone, standard-library-only Python 3 checker. From the directory containing this file, run `python3 verify.py`. The expected complete output is saved as `verify_output.txt`.

The checker implements the pair-pattern partition independently of the mathematical exposition and compares it to direct exhaustive averaging of quadratic forms over every sign assignment. It uses exact rational arithmetic for all variance and distance comparisons. It checks tensor factor dimensions \((2,2)\), \((2,3)\), \((3,2)\), \((2,2,2)\), \((2,3,2)\), and additional coefficient-rank examples in \((3,3)\). It confirms coefficient independence, group sizes, orthogonal-projection distances, the zero-variance projected family, the signed off-diagonal witnesses, and their independent-sign variance. The checked execution passed 247 assertions with no warnings.

The general theorem is proved by orthogonal Walsh characters, disjoint pattern supports, and Euclidean projection; exhaustive finite enumeration is not a proof for unbounded dimension. The experiment does not verify uniqueness in the literature, does not test Gaussian or complex tensor probes, and does not imply a practical sample-cost advantage.
