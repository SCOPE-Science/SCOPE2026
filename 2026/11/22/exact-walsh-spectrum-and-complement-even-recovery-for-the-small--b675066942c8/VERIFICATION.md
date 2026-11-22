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

# Reproducible checks

Run `python3 verify_witt.py` with Python 3 and no third-party dependencies. The program constructs all 729 words from a six-row matrix over \(\mathbb F_3\), retains distinct weight-six supports, checks the 792 five-subset incidences, and independently computes the 4096 Walsh values by direct summation and the Walsh--Hadamard transform. It also verifies the stated signed histogram and Parseval. All calculations use exact integers. The displayed generator is reproducibility data; the paper's abstract proof uses only the Steiner incidence property. The historical comparison is bounded, and no independent audit has been performed.
