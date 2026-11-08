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

# Reproduction instructions

With Python 3 (standard library only), save the embedded files `verify.py` and `CENSUS.csv` in the same directory and execute `python verify.py` there. The expected final output line is `DEBRUIJN_SUBSEQUENCE_CENSUS_VERIFY_OK`.

The verifier independently enumerates all binary de Bruijn cycles of orders two through five by rooted Eulerian tours and by invertible shift-register feedback maps. It verifies exactly one occurrence of every length-order window in each cycle, compares canonical representatives, checks the complete distribution of minima and maxima over all cuts, checks the shortest-absent-subsequence dynamic program against the greedy factorization at each cut, reconstructs the reversal-and-complementation orbit census, and matches every row of the saved 2,048-cycle table.

The procedure is a complete finite enumeration, not a proof for larger orders. It does not establish independent review or exhaustive historical publication priority. No external software beyond Python 3 is required.
