---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The gap-run law and the perfectness dichotomy are correct. The multiplicity is a and gcd(a,2a+1)=1. Writing any non-a generator sum as B+a(B+C) with Mersenne coin total B and coin count C, a positive residue wrap B=r+ha pays h(a+1) in the quotient before coin cost; this is larger than c(r)≤r for h≥1. Multiples of a cannot improve the minimum, so w_r=r+a(r+c(r)). For adjacent residues append a unit coin, and for the reverse inequality delete a unit coin or replace one nonunit b_i by two b_{i−1}, using b_i−1=2b_{i−1}; all coins are odd so the adjacent cost difference is ±1. Membership thresholds K_r=r+c(r) are nondecreasing with jumps 0 or 2. Each row starts with a multiple of a and has at most one terminal run; exactly K_r−K_{r−1} rows have a run starting at r, of length a−r. Summing gives a−1+c(a−1). In the subfamily the last residue is the sum of two Mersenne coins, and its predecessor is a single coin for n=1 and an odd noncoin representable with three coins for n≥2. This yields the stated isolated counts and total. Independent direct generator-membership DP plus minimum-coin DP agreed at 34 distinct a, including all a=3..25, 31 and 79, and the union with all s,n=1..4 examples. The reproduction checks a full terminal block of members before truncating the gap scan. Replay: python3 /workspace/branches/7b3a8df7-c1de-4d61-95b8-88bfa89e9035/ordinal5_actual.py. This is bounded corroboration; the frozen checker was inspected, not run. There is no claim beyond this affine binary family.

## originality

FAIL

The proposed result is a direct corollary of stronger prior Apéry and greedy change-making theorems, rather than just sharing their starting methods. The cited arXiv:2306.10738v1, Lemmas 3.3–3.4 and Eq. (4), directly give the identical full monotone threshold list after specialization; arXiv:2306.03459v4, Lemma 2.6, Theorem 2.10 Eq. (8), and Lemma 2.11 explicitly provide the optimal greedy coin costs and the same list and monotonicity. A row boundary count is just the first difference of that complete known list. Parity and adding a unit coin give the zero-or-two statement immediately; the total and isolated counts are a telescope and evaluations of the last two known greedy costs. No claim is made that the earlier papers use the same histogram wording. Coverage is by implication, not an exact textual match.

## value

FAIL

The histogram and perfectness question are natural, and the short self-contained proof is useful exposition. But as a standalone mathematical finding this histogram is a routine first difference of the previously explicit monotone integer thresholds; even the support and boundary reduce to their known coin costs by parity and greedy evaluation. The total is also (F+1)/a directly since the maximal Apéry element is w_(a−1). No additional nonmechanical increment or distinct application is demonstrated. A citation or numerical certificate would not produce a surviving original result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
