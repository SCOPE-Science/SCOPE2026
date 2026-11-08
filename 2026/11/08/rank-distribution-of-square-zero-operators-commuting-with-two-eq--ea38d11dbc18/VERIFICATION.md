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

# Verification of the stated rank-generating polynomial

The standalone Python file `verify_centralizer.py` enumerates the original nonlinear equation \(X^2=0\) in \(M_2(\mathbb F_q[t]/(t^m))\). Its rank algorithm builds the induced \(2m\)-dimensional linear map and performs field Gaussian elimination, independently of the counting proof. It checks the **entire** rank histogram coefficient by coefficient.

All nine selected cases passed: \((q,m)=(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(4,1),(4,2),(5,1)\). The cases \(m=1,2\) are boundary checks; the two cases \(m\ge3\) validate the first genuinely longer truncated rings. The file `VERIFY_OUTPUT.txt` records the actual output from the checker. It ends in `ALL_EXACT_SQUARE_ZERO_CENTRALIZER_RANK_CHECKS_PASS`.

Explicitly, the \(q=2,m=3\) histogram of ranks \(0,1,2,3\) is \((1,9,30,72)\); for \(q=2,m=4\) it is \((1,9,78,168,384)\). For \(q=3,m=2\) the histogram is \((1,32,120)\), and for \(q=4,m=2\) it is \((1,75,420)\).

The checker depends only on the Python standard library. From a directory containing the file, execute `python verify_centralizer.py`. It does not attempt to certify the universal statement; that depends on the ring-theoretic proof in `RESULT.md`.

The analysis assumes no independent audit, external mathematical certification, or proof-assistant check.
