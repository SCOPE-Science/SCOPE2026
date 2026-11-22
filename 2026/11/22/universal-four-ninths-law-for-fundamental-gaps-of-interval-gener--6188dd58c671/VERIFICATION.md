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

The exact two-band set and count are proved in RESULT.md, including endpoints, the two tests \(2n\in S\) and \(3n\in S\), and the uniform error inequality. The independent implementation in `check_fundamental_gap_bands.py` uses unbounded-coin reachability rather than the residue membership shortcut.

Successful verification command:

```sh
python3 check_fundamental_gap_bands.py
```

Observed: 5,886 parameter pairs, 2,793,328 gap candidates, and 566,195 fundamental gaps were checked without mismatches. The checks are finite diagnostic evidence; the unrestricted conclusion follows from the proof, not from extrapolation. A separate external audit has not been performed.
