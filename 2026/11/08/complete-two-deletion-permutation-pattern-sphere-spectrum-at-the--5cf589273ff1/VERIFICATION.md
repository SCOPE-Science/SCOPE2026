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

# Verification instructions

Run `python3 checker.py` with Python 3. It uses only the standard library, iterates all 5040 elements of \(S_7\), builds the complete set of 21 standardized five-pattern descendants by each of two implementations, compares the sets for every permutation, and checks the full published frequency table and exceptional equality cases.

The table covers exactly two deleted positions, and the code exhausts all 21 possible choices without sampling or randomization. Assertions check the total count, the forbidden size 20, the two maximizers, and the summed sphere size 55116. This constitutes a finite exhaustive mathematical certificate; it is not a theorem for other lengths, and it is not an independently audited verification.
