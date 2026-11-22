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

The standalone `check.py` uses exact symbolic transition-matrix calculations and independent rational microscopic-path enumeration. Execute with Python 3.10 or later plus SymPy (`python check.py`). It checks all six four-word reversal pairs, the stationary current, and the two sharp optimization factors, then separately tests 46 rational parameter choices by enumerating all four-state paths of length four. Its output is a single PASS line on success.

The exact analytical proof in `RESULT.md` establishes the entire-observed-process reversibility iff criterion and the three-hidden-state lower bound; the finite computations alone would not prove those statements. The published references were compared by object, measurement channel, and conclusion. The result remains a self-reviewed mathematical claim without independent audit or a verified publication-priority determination.
