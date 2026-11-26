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

Every step in a path for (AB)^r advances by at least 2. The common choice of A and B with only unit first superdiagonals realizes the sharp bound (no cancellation). In odd dimensions exactly one all-two path can contribute to the last nonzero power, and the required 2N coordinates are independent. In even dimensions only the two all-two products U,V and a single corner sum W are relevant. The latter uses one jump of size three; its j-th linear term survives the t-products exactly for R≤j≤L when U=V=0. If R<L, choose j=L: b_(2L+1) is nonzero because t_(2L) is nonzero (L>R), and the surviving second-band coordinate of A is unique to that term. If R=L, the two endpoint coefficients have independent conditional zero probabilities q/(2q−1): each is the zero component of a pair of independent uniform scalars conditioned on product zero. Thus the conditional probability of nonzero rank is η there, zero when R>L, and one when R<L. A nonzero linear form in independent uniform second-band coordinates hits nonzero with probability 1−1/q, accounting for field cancellation. Independence of odd and even t-products gives the weights f²s^(L−1+N−R), which sum to the displayed even formula. Summing the geometric series at fixed q yields C_q and C_2=s=1/4. Independent `python3 /workspace/reproduce_reviews.py` multiplies matrices and finds exact agreement at (n,q)=(4,2),(4,3),(4,4),(5,2),(6,2), including 927/1024 over F_4 represented by the binary polynomial x²+x+1. Only coordinates on the first two bands that can enter a product path are enumerated. The path argument proves the universal claim, not the finite replay.

## originality

PASS

The sharp filtration bound, odd single-path observation, and small exact counts are not separately novel. The supported distinct contribution is the all-dimension factorization-weighted extremal law, in particular the even cancellation term and resulting fixed-field linear parity factor for independent radical products. Checked results with matching graph/filtration structure, extremal terminology, or small n do not imply this law.

## value

PASS

Maximal index is a natural extreme statistic of a nilradical product. The formula separates the effect of a unique length-three detour from field cancellation and finds a parity enhancement of linear relative order at equal maximal index. It quantifies a rare-event law not recoverable by treating the product as one uniformly sampled nilpotent matrix. This does not claim the whole product Jordan distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
