---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

A zero start fails exactly upon including the next 1, if any. At a 1 start, two completed blocks first disagree at the next 1 of the shorter gap; a terminal 1-block is smaller than a block with a following 1 whether it ends before that following 1 or still has a zero. Hence reversed integer gap order with a bottom terminal represents full suffix order, independently of the trailing gap. For a greater later suffix j and code LCP h, both unequal symbols are interior gaps, so the expanded common prefix is the sum of the h equal block lengths plus 1+g_{j+h}. The next-greater correction can also be seen directly: in the suffix at p, let d be the least displacement of a lexicographically greater suffix, and H its LCE. A shorter failure cutoff c=e+LCE(p,p+e)<d+H with e>=d would give a greater suffix at displacement e-d: equality under a shift of d holds at every tested character through position c, since c<d+H. Repeat to reach a positive displacement <d (impossible) or 0 (impossible mismatch). Less than or equal to the first failure cutoff, no truncated suffix wins, and any first winning mismatch persists at larger prefix lengths. This proves the correction and the no-greater case. Comparison sorting the gap-index pairs, radix prefix doubling, linear Kasai and stack, and O(log(r+1)) per LCP range query give the claimed preprocessing/space bounds in word operations. There are at most r+1 nonempty zero runs and r singleton ones; query is by binary search, with the all-zero query constant time (uniformly O(1+log(r+1))). Independent all-length direct prefix testing over all 8,190 nonempty binary words through length 12 agrees (python3 /workspace/reproductions/3.py; 3.txt). These checks do not replace the proof or time analysis.

## originality

PASS

The supported distinct contribution is the compressed full-array algorithm on binary zero gaps with complexity in the marked-one count, not the published NGS/LCE identity, ordinary Lyndon factorization, or the expanded inverse array. The closest inspected claims do not supply this reduction with the terminal block and border correction.

## value

PASS

Exact random access to an entire inverse array without enumerating arbitrarily long zero runs is a useful output guarantee. The nonzero border correction at the marked positions is computed without character-level expansion, not just a bound on the number of segments. The gain needs actual sparsity for the preprocessing to beat expanded linear time; no claim extends to arbitrary alphabets or explicit expansion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
