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

# Verification of the exact coordinate-cross lifting theorem

The argument has two independent rank checks: the exact self-ambiguity support in the Weyl basis, and the free-dimension count of the row/column-sum kernel. The key nonstandard step is that the ratio of any two character values has odd order, so two such values cannot sum to zero. The resulting loss of only axial-coordinate matrix information is explicit.

Run `python check_cross.py`. The script enumerates every ambiguity coefficient in prime orders \(p=3,5,7\) and independently constructs an \(81\times81\) complex lifting matrix at \(p=3\), verifying all singular values. Observed ranks/nullities are \((57,24)\), \((465,160)\) and \((1897,504)\).

Run `python check_odd_groups.py`. It enumerates all character sums for factors \(\mathbb Z_3\times\mathbb Z_5\), \((\mathbb Z_3)^2\times\mathbb Z_3\) and \(\mathbb Z_9\times\mathbb Z_3\), yielding the predicted nullities \(68,228,228\). The scripts are included completely; `check_cross.py` requires `numpy` as noted in `requirements.txt`.

All numerical comparisons use explicit floating tolerance. They are only corroboration; the statements for infinitely many odd groups and prime fields rest on exact character orthogonality, the four overlap cases, and elementary graph connectivity. Independent mathematical validation is not provided.
