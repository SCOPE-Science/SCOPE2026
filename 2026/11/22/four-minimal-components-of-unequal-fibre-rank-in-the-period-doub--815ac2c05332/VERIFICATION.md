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

A base sequence and six initial bits give a unique bilateral lift, with all coordinates depending on only finitely many base coordinates and those bits. The four shifted second-substitution images cover the minimal base: their union is nonempty, closed and shift invariant. Their forced zeros and ones distinguish different-parity phases and distinguish equal-parity phases by exclusion of the alternating point from the minimal base. Thus the phase normalization is continuous. Its only change under a left shift is zero or a four-step shift of the normalized lift; the latter acts on the even triple by R(e)=(e_2,e_0+1,e_1+1). The even triples have orbit sizes 1,1,3,3, yielding disjoint clopen invariant parts of the stated ranks. The two concatenation parities and the offset state repeat at levels 2 and 6, so deterministic iteration proves period four from level 2 rather than just a sampled repetition. In the two even level classes the resulting prefix maps have the same even action R. Their quotient and its conjugates give all even-weight odd-coordinate translations, while cubing P gives the odd-weight translation (1,1,1). These operations give full transitivity on each part of the reference fibre. The bilateral valuation base is realized by shifting a bilateral extension of the fixed right tail by the even powers of two in the level exponent; each fixed coordinate with j+1 nonzero eventually has unchanged valuation, and j=-1 is fixed by the even valuation parity. Both return families therefore converge back to that base. A minimal set in each clopen part maps onto the base and contains a point over the reference base, hence contains the entire orbit class of its reference fibre by the convergent returns. Shifting transports these whole fibre subsets over a dense orbit, and their closure is the full part by the local product coordinates and clopenness. This directly checks minimality and exhaustion, also without needing to assume pointwise almost periodicity. The fresh /workspace/branches/2d9c2d30-8e81-4445-a821-2d253863ee5b/recur_check.py reproduced explicit residue parities through level 10, recurrence states through level 30 and both permutations on all 64 prefixes. The uploaded checker was inspected, not executed; the computation is bounded and does not replace the topological argument.

## originality

PASS

Nonminimality at this very lag and the general return-permutation approach are established prior work. The distinct result is the specific invariant partition, transitive returns within each fibre class, and the resulting heterogeneous ranks at lag six. The inspected closest published results do not compute or mechanically imply that partition and those ranks. Match by stride rather than by name or source date; the same-day finite cyclic comparison covers another setting. This is a best-of-evidence assessment.

## value

PASS

Six is the first nondyadic even lag, and prior nonminimality alone leaves its topological decomposition and the way the fibre splits unknown. The binary example produces two genuinely different ranks in the same extension, in contrast to the uniform ranks in the neighboring dyadic cases. The clopen invariant and exact return permutations explain the difference and determine the components over every base point, not just over a sampled periodic approximation. This is a natural test case for rank heterogeneity, without asserting a law at all nondyadic lags.

The dated certificate retains the supplied scientific assessment, sources and limitations.
