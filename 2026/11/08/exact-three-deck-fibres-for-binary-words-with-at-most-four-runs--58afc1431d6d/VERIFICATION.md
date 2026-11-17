---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For any n>=1 with at most four positive constant runs, symbol totals and mixed 2-/3-subsequence counts distinguish <=3 run types and each same-start four-run word. For w=0^a1^b0^c1^d, p=N10=bc, N010=ap and N101=dp recover a,d and then b,c. Comparing an opposite-start source with the same deck forces t=p/(AB-p)>0 and ad t(t-1)=0; positive a,d force t=1, so its unique possible partner is the reversal and requires 2bc=(a+c)(b+d). Pair-subsequence double counting shows fairness suffices for all triple-pattern equality. The fourth-deck difference N0010-N0100=abc(a-c)/2 is nonzero because fairness forces c>a; thus order4 is injective within this source family. Counting unique zero-start fair pairs with A=a+c and b gives the displayed divisibility sum F_n; all fibers have one or two elements and count T_n-F_n. The direct independently implemented DP exhaustively verified n=1..12 and F7=2,T7=84, 82 restricted distinct decks. That finite check corroborates but does not prove the all-length identity.

## originality

PASS

The restricted 4-deck bound and fair-word concept were already published; they are not new. The claim that every restricted three-deck fiber is singleton or exactly one fair reversal with necessary-and-sufficient equation and the complete all-n divisor census is not provided by those papers or by the relevant indexed results. Best-of-knowledge originality with a residual risk of unindexed 3-binomial restricted-class fiber results.

## value

PASS

Bounded-run binary words are a natural reconstruction class. The theorem identifies every source ambiguity, its unique reversal mechanism, the exact integer-divisibility census, and the optimal number of codewords when encoder and decoder both restrict to that class. This is a complete all-length natural classification not mechanically implied by the previously known order-four upper bound or the known fair-word examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
