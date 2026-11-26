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

PASS for the corrected RESULT.md under /workspace/repairs/2/. The frozen proof at line 63 wrongly claims nc_n<=S_K for any active rank K: already for n=3 and weights (1,4/5,16/25), c_n=2/5 and ranks 1 and 2 both contact, so choosing K=1 violates it. This is a defect in the original asymptotic argument, not a counterexample to its findings. The repair explicitly covers the lower rank of a tie and replaces the macroscopic optimizer-step argument with a compactness proof excluding both endpoint ranks. Independent reconstruction: for a generic linear objective, order the positive coefficients, discard the negative coordinates and use Abel summation and the prefix constraints to attain the unique optimum at the rank-prefix vector. This recovers the vertex list. Strict convexity in either point restricts diametral pairs to vertices; coordinatewise (u_i-v_i)^2<=max(u_i²,v_i²), strict if both entries are positive. At most n of two copies of each squared weight can contribute; attaining the sum of the largest n forces complementary supports and balanced ranks. Counting each unordered pair once gives n!/2 for even n and n! for odd n. The maximum squared-distance objective in the center is strongly convex and symmetric, forcing a unique multiple of the all-ones vector. Adjacent branch differences a_k(a_k-2c) give exactly the stated active ranks, stationary candidates, breakpoints and contacts. For any active K, a_K>=2c_n>=a_(K+1) with endpoint conventions, nc_n is in the convex hull of active S values, and |nc_n-S_K|<=a_K for K>=1. This verifies the repaired bound and handles ties. For fixed t, c_n=O(1/n) forces K→∞, then c_n~1/[n(1-t)] and the weight bounds exclude K=n and force t^K of order 1/n. Completing the square yields Q_K-S_K²/n+n(c_n-S_K/n)² and the claimed O(n^(-2)) expansion. For h=λ/n^β, c_n→0 forces hK→∞, so S_K~n^β/λ and c_n~n^(β-1)/λ; the weight at n is exponentially smaller, excluding K=n. The adjacent-weight bounds then give the stated rank scale, the geometric squared tail and center terms are negligible after scaling by n^β, and the balanced-rank squared sums yield the diameter. For h=λ/n, any limit x of K/n satisfies c=A(x); the weight bounds contradict x=0 or x=1, then exp(-λx)=2A(x) gives the unique claimed rank and center limit. Direct substitution gives R_n²/n→1/[2(λ+2)], and the balanced-rank geometric sums give the diameter limit. The logarithm of the total contact count differs from that of the larger active rank by at most log 2; the falling-factorial estimates in the repaired proof establish all three entropy scales. Replay: python3 /workspace/branches/independent_checks.py 2, exact enumeration from active linear constraints for four n=3 profiles, including the counterexample to the frozen proof inequality. The original checker was inspected but not rerun, and its large-size tests cover fixed and macroscopic profiles, not the intermediate or entropy results.

## originality

PASS

The corrected result explicitly credits exact prior overlap on consecutive-label partial permutohedra rather than presenting it as just an analogy. The credited distinct part is the exact diameter equality classification for general strict weights and the geometric-family rank and full contact-count asymptotics in three regimes. The ball method and one/two-rank structure in the prior specialization are not independent novelty. The repair does not change the headline mathematical scope.

## value

PASS

The same rank-orbit combinatorics can support quite different Euclidean extreme-pair and contact behavior. The exact diameter pair classification provides metric data not supplied by vertex enumeration, and the three rank/count limits quantify changes in the number of extremal contacts as the same natural discount approaches one. They are worthwhile independent of the short finite radius formula and of the prior consecutive-label specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
