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

The argument in `RESULT.md` is self-contained. The critical input is the exact finite sum over \(\ell\) of elementary representation counts; the proof verifies that terms with \(\ell\ge2\) vanish in the tested symbolic range for every \(d\ge3\). The residuewise predecessors and thresholds differ by exactly the smallest generator, guaranteeing minimality via monotonicity. The maximum and sum of these thresholds yield the asserted Frobenius number and genus.

Standalone checker command: `python3 CHECKER.py` (Python 3, no third-party dependencies). The checker verifies 1,260 coprime parameter pairs, 78,178 threshold residues, and all complete denumerant counts up to a point beyond the last threshold for each pair. Separately, 1,020 small-pair cases validate the exact coefficient-count lemma by direct enumeration. It is supporting finite evidence, not a proof of an infinite claim.

Limitations: no independent audit or validation has been carried out, and unindexed equivalent literature remains possible. The general formulas apply only to the explicitly stated parameter and representation-count threshold ranges.
