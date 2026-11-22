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

The theorem follows from the five mathematical steps in RESULT.md. The finite programs below provide repeatable checks; they are not substituted for the infinite-family proof.

From the directory containing the embedded files, run:

```
python3 verify_transfer.py > transfer_output.txt
g++ -std=c++17 -O2 verify_direct.cpp -o verify_direct
./verify_direct > direct_output.txt
python3 compare_total.py > comparison_output.txt
```

`verify_transfer.py` explicitly constructs the sixteen-state polynomial and checks lengths \(5\) through \(80\). `verify_direct.cpp` uses bitwise adjacency tests on **all** \(2^n\) vertex subsets for each order \(5\) through \(21\). `compare_total.py` performs an unconstrained ordinary-total-domination comparison at the same orders; only the cases with \(n\equiv1\pmod7\) and \(n\ge8\) are used in the claimed exact exclusion. All three stdout outputs are included for byte-comparison after rerunning. Independent mathematical validation has not occurred.
