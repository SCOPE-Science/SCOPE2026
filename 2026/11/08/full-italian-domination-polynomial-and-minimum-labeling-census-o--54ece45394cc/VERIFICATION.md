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

# Computational verification

`python3 verify.py` uses only the Python standard library. It independently reconstructs all vertex label assignments for \(n=3,4,5,6\), checks every coefficient against the transfer computation, checks the predicted minimum weight and number of minima for \(3\le n\le16\), and independently enumerates all minimum candidate columns for \(3\le n\le9\) including the exceptional \(B\)-column cases. Successful output ends with `VERIFY_OK`. All comparisons succeeded in the package-generation replay.

The unrestricted transfer and minimum classification are mathematical consequences of the proof in `RESULT.md`; finite checks cannot validate infinitely many orders or settle historical priority. Independent audit: not performed.
