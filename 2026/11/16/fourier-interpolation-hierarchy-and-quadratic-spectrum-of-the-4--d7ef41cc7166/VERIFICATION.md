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

# Reproducibility

The attached `verify_krawtchouk.py` uses 90 deterministic row-pattern configurations and exact SymPy characteristic polynomials for each degree 0 through 4; its asserted results give the rank sequence and quadratic eigenvalue multiplicities. The separately constructed `verify_direct.py` scans all 65,536 binary 4-by-4 matrices, evaluates all characters through degree four and verifies modular ranks; it also computes the quadratic characteristic polynomial independently in exact integers. Both scripts were executed successfully from the embedded versions, without approximate rank heuristics.

Python 3, SymPy and NumPy are required. Run both scripts from the same directory. Modular rank establishes a rational-rank lower bound; the exact characteristic polynomials in the first script establish the complete rational ranks. The result does not extend to other margins or larger matrices by these finite checks. No independent external audit has been performed.
