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

# Reproducible verification

Run the included scripts with ordinary Python 3 from their containing directory:

```sh
python3 check_exhaustive.py
python3 check_transfer.py
python3 check_maxplus.py
```

The files `exhaustive_output.txt`, `transfer_output.txt`, and `maxplus_output.txt` capture successful executions of these exact scripts.

`check_exhaustive.py` evolves all \(\sum_{n=1}^{12}3^n=797160\) labelled three-state configurations on open paths of lengths 1–12. For each configuration it checks extinction by \(n+1\), agreement of the first-extinction time with the strict-endpoint-record criterion, and agreement of the resulting population with the square-root coefficient recurrence. Its terminator is `EXHAUSTIVE_OK`.

`check_transfer.py` evolves letter-labelled strictly positive height paths via an independent boundary-aware transfer. It compares right-end strict-record counts through path length 101 against the differential recurrence for the square-root series. Its terminator is `TRANSFER_100_OK`.

`check_maxplus.py` compares every transition's original excitation events with closed-neighborhood maximum-height increments on all \(9840\) labelled initial words of lengths 1–8 through \(n+3\) rounds. It also checks the color-gradient invariant. Its terminator is `MAXPLUS_OK`.

These computations establish only their specified finite checks. The all-length theorem, the exact kernel solution and the sharp probability constant rest on the argument in `RESULT.md`; the runs do not independently certify historical priority or constitute an external review.
