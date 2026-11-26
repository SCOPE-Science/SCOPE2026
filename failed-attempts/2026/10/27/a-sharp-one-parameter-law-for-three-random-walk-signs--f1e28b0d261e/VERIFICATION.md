---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independence and symmetry separate fair signs and iid positive magnitudes, and conditioning on all but one magnitude removes ties even for singular atomless laws. Persistence +++ sums the four eligible increment-pattern conditionals 1,1−t,1/2,t with weight 1/8. Also P(T1>0,T2>0)=3/8. The alternating output +-+ requires exactly the +-+ increment signs and the magnitude event A1<A2<A1+A3, with probability 1/2−t; reflection and normalization then determine the other words. Disjoint dominance events give 3t≤1; iid samples have positive probability of landing in one positive interval with ratio less than 2, ruling out equality. Log-uniform magnitudes give t=0 for small spread, continuously approach 1/3 by the gap between the largest and second-largest log samples, and realize every intermediate value by continuity. The triangular torus map preserves the independent uniforms and telescoping integer carries give the odd-time sign correspondence. An independent simplex-monomial calculation and enumeration over all 5040 seven-symbol permutations and 32 five-step paths give 19/90 and TV 7/720, with the two stated tables; run `python /workspace/replay_frozen_reviews.py 3`. This finite replay does not prove the continuum result.

## originality

FAIL

The closest earlier sign-persistent result does not print the ordered table, but its exact early-time laws and conditional probabilities, including the same sharp dominance parameter, mechanically give that table at independent signs. Its proof also establishes the entire feasible range by the same log-uniform family. The permutation representation and count were established by Tang, and the exact numerical specialization is explicitly not the distinct contribution asserted by the frozen result.

## value

FAIL

Distinguishing occupation marginals from joint signs is a sound motivation, but the claimed classification adds no independent mathematics beyond the previously given conditional law and sharp dominance range. The particular numerical contrast is not presented by the frozen finding as independently novel, and here is a straightforward evaluation of the known triangular embedding using that law and five fair coin flips. It does not provide a separate valuable repair of the covered main claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
