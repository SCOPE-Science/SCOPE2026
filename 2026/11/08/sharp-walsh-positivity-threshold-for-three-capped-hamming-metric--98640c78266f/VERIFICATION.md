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

The proof establishes the result for **every** integer \(n\ge4\) using exact Walsh shell sums and one-dimensional sign comparisons. The finite checker uses only the Python standard library and independently evaluates character sums in dimensions \(4\) through \(10\), tests the spectral sign margin and critical nullity through dimension \(14\), and compares second-order asymptotics in dimensions \(1000\), \(1001\), \(2000\), and \(2001\). Run `python3 capped_hamming3_checker.py`. Successful output ends with `CAPPED_HAMMING3_WALSH_CHECKS_OK`.

The checker does not certify all dimensions, historical priority, or independent review; the analytical proof carries the infinite quantifiers. The result concerns the clipped metric \(\min\{\operatorname{wt}(x-y),3\}\), not graph powers or arbitrary radial transforms.
