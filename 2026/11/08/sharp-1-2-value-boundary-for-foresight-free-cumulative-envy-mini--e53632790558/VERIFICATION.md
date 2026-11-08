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

# Reproduce the finite tests

Run `python3 check.py` from the directory containing `check.py`. Python 3 standard library suffices; the checker uses exact integer arithmetic and a fixed random seed. The independent exact state recursion stores, for every attainable absolute discrepancy, the best cumulative sum; a second direct allocator enumeration checks the recursion for all words through eight goods over values \(\{1,2,3\}\).

Observed success: 9,841 direct-enumeration comparisons; 65,535 positive \(\{1,2\}\) sequences through fifteen goods; 960 seeded longer sequences; 156 short nonnegative sequences; both minimal length-four counterexamples. These exhaust **only** the stated finite test domains and do not prove an unbounded claim. The analytic suffix induction in `RESULT.md` proves the universal assertion.

The proof's critical bounds are the parity-class monotonicity of \(F_W\) and \(0\le F_W(2)-F_W(0)\le2\); both are checked separately in the written induction. The zero-valued counterexample explains why the positivity restriction is essential. No independently performed audit is claimed.
