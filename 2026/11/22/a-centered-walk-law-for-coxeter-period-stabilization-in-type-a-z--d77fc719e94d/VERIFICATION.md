---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Reassessed the complete corrected RESULT.md in repairs/4. Reduced products that use each generator once give exactly the orientations: all directed paths are acyclic, two extensions of one orientation differ by commuting moves, and different orientations cannot be related by the reduced-word moves without repeats. Lex-first inclusion in c^∞ is precisely the length-increasing greedy rule because each length-increasing reduced prefix can be completed to w₀ by a finite word embedded in the remaining tail. Its last occupied round is the first Demazure absorption round. CLS counts in type A obey φ_i−φ_(i+1)=(ε_i+ε_(n−i−1))/2 and φ_i+φ_(n−i)=n, yielding φ_i=(n+H_(n−i)−H_i)/2; the greatest count is the last occupied block. Independently, thresholding commutes with the descending comparators. In 0^a1^b each zero-one crossing (i,j) uses comparator a−i+j; the two predecessors suffice because these crossings leave the two labels adjacent. A round penalty is (1−ΔH)/2 along each grid edge, so the sum to (a,b) is independent of the path and gives (n+H_a−H_b)/2. Maximizing gives the same formula including parity. Centered sums are formed by adding disjoint sign pairs, producing independent steps −1,0,+1 with weights 1,2,1. The single odd-rank sign shifts the even walk by ±1/2, producing the odd interval [−k−1,k] or its reflection and the factor 2. Both widths and the zero-step n=3 case are included. With m−1∼n/2 steps and variance 1/2, normalized paths converge to B/2, and the supremum is continuous; Brownian exit from [−2x,2x] gives exponent denominator 32x². Independent bounded replay `python /workspace/review_replay.py 4` directly checked all 5912 generator orders for n=3,…,8, including commuting-order agreement and deduplicated counts. The supplied checker and output were inspected, not executed. No finite computation is used as a substitute for the limits or the all-orientation proof.

## originality

PASS

In the actual corrected files the pointwise threshold is derived and explicitly credited as a consequence of Ceballos–Labbé–Stump, not asserted novel. The claim is narrowed to the exact finite all-threshold counts and the centered Brownian limit for the uniform distinct-element ensemble. The comparable primary results give deterministic profiles, ordinary powers or minimum cases. No examined theorem gives the distribution of the full random profile or its finite survival counts and absolute Brownian limit. This is bounded credit, not a priority certification.

## value

PASS

The narrowed claim gives a natural probabilistic invariant of periodic sorting under uniform distinct Coxeter elements. It identifies the full nonextremal finite law including parity, and resolves whether the typical excess duration is bounded, linear in rank, or diffusive: the scale is √n with a specific nondegenerate law. This requires analyzing the joint centered profile over the orientation ensemble and is not the restatement of a fixed-word formula, a fastest-case lookup, or novelty attributed to Donsker's theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
