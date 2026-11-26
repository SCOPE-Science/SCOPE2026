---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The three prime classes have union pq+pr+qr-p-q-r+1 by CRT inclusion–exclusion. A pair class meets the omitted prime class in one point, so the additional contributions are at most r-1, q-1, p-1, plus one singleton. With the prime coordinates set to zero, the choices (1,1) on pq, (2,1) on pr, and (2,2) on qr make the residual pair classes disjoint: their shared-coordinate values differ for every pair. The point (1,2,1) lies outside all six. Values 0,1,2 are distinct even for p=3. Hence the uniform optimum is attained. An independent bit-mask exhaustive check of pair-class choices with normalized prime classes and an optimized singleton returned uncovered minima 35, 63, 219 for M=105,165,385. Replay: python3 /workspace/branches/independent-reproduction/arithmetic_review.py; finite check only. Frozen scripts were inspected, not executed.

## originality

FAIL

The exact seven-class formula is a boundary consequence of a distinct indexed four-prime exact theorem, despite the different moduli. Fix p,q,r and let h be the three-prime optimum before the singleton. Add a fourth prime s. The original six classes lift identically to all s slices of Z/(pqrs), leaving at least s h holes; the new classes s,ps,qs,rs can cover at most K=pqr+qr+pr+pq in total, independent of s. Conversely lift a six-class optimizer and add any four allowed classes. Therefore sh-K <= H(p,q,r,s) <= sh. The four-prime formula has a bounded-in-s defect (q+2 or 3) and its coefficient of s is (p-1)(q-1)(r-1)-[(p-1)+(q-1)+(r-1)] = pqr-pq-pr-qr+2. Thus H/s tends to h with exactly this value. It is positive (at least 36 at the smallest triple and increasing in the three core sizes), so the final singleton subtracts one, recovering the frozen formula. Both results are indexed on the same date; this proves coverage, not chronological priority. The unavailable conjecture passage is not the basis for rejection.

## value

FAIL

The invariant is natural and the direct three-coordinate proof is economical, but the submitted contribution is the exact deficit itself. It is mechanically extracted from the indexed uniform four-prime theorem by a bounded fourth-slice correction and a singleton. The record does not isolate a further independently useful result beyond that covered classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
