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

# Reproduction and scope

Run `python3 verify.py` using Python 3 standard library. The program checks modal color-refinement partitions computed directly from relational successor sets against the exact predicted depth zero, one, two and three profiles for every atomic valuation in the stated small parameter cases. It also checks the characteristic support probes against direct relational evaluation and closes the one-variable modal term algebra under Boolean operations and \(\Box\) independently, with operation counts \(4,16,64,64\) for \(k=0,1,2,3\).

The exact successful program terminator is `VERIFY_OK 24686 pointed valuation cases`. These finite comparisons are software-supported sanity checks and cannot establish an infinite quantified theorem. The accompanying mathematical proof establishes the full formula and the sharp boundary over all nonnegative integers in scope.

The originality comparison is limited to the named inspected material and a database search; it is not an exhaustive priority certification. Independent mathematical and historical-priority assessments have not been performed.
