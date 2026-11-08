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

# Reproducible finite checks

From the directory containing both included scripts, execute:

```bash
python verify_direct.py
python verify_independent.py
```

`verify_direct.py` exhausts all \(65{,}536\) labeled binary arrays for each of the fifteen four-site masks, checks all sixteen translated windows, computes the four translation orbits and two classes under row and column translation, complementation, and column reversal, and verifies the alternating row-XOR property.

`verify_independent.py` independently builds both rows as length-eight tuples, evaluates four-bit tuple windows for all fifteen masks, and checks the orbit-generated classification. Neither program calls a remote service or assumes a random sample.

Observed outputs: `DIRECT_OK` and `INDEPENDENT_OK`. The programs prove the stated *finite* classification when their exhaustive loops and exact equality predicates are inspected; they do not establish an infinite family or historical priority. No independent scientific audit was conducted.
