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

# Reproducibility and limits

Run `python3 verify_direct.py` and `python3 verify_power3.py` with standard Python 3, no third-party dependencies. Their captured stdout files are included. Direct enumeration constructs all length-\(3^k\) windows from the nine ordered supertile pairs at \(k=0,\ldots,6\), totaling 264513 direct window comparisons; every pair occurs in the fixed point. The separate exact-rational affine checker derives the finite recurrence for pair-boundary prefix extrema and verifies all twelve recurrence types symbolically for every real parameter \(T\ge1\), with base classes tested through \(k=36\). Its symbolic proof depends on the displayed max/min recurrence, established by splitting each substituted block into three pieces. The included scripts are supporting reproducibility and not a replacement for the complete human-readable infinite proof in RESULT.md.

The supplied scientific review is not an independent validation or historical-priority certification. Neither arbitrary-length Abelian complexity nor the full regularity question is determined by the theorem.
