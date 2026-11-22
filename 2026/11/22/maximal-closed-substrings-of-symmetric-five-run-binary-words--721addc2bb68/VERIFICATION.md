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

# Verification of the symmetric five-run MCS classification

The files `check_by_closed.py` and `check_by_next_occurrence.py` are standalone Python 3 programs. Both enumerate exact positional MCS sets independently of the displayed formula; each compares every computed endpoint set against the classified families. They require only the Python standard library and have no external data dependencies.

`python3 check_by_closed.py` directly counts proper border occurrences inside each factor and checks its available one-symbol extensions, for all positive parameters at most six. The recorded result is `DIRECT_BORDER_ORACLE PASS cases 216 MCS_occurrences 2886 max_length 30`.

`python3 check_by_next_occurrence.py` instead computes a longest-common-prefix table for all suffix pairs and checks the first-next occurrence and left-character mismatch criterion, for all positive parameters at most eighteen. It also verifies the sharp lengthwise extremum for lengths five through eighty. The recorded result is `NEAREST_LCE_ORACLE PASS cases 5832 MCS_occurrences 171774 max_length 90 extrema_lengths_through 80`.

The scripts' outputs are stored in `check_by_closed.out` and `check_by_next_occurrence.out`. The infinite statements are proved by the run-pair argument and geometric series in RESULT.md; neither finite enumeration nor successful execution certifies an infinite property.
