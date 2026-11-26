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

For finitely many distinct marked vertices, each parent choice contributes a linear factor, because a new vertex can be a direct child of at most one mark. On the prescribed compact rescaled ranges away from 0, the all-zero product differs from the product of the individual i_k/n by a relative 1+O(1/i_min), using the summed squared reciprocal denominators. After removing that product, each coefficient is the independent-draw product of the log(n/i_k) powers over r_k!, times the probability of distinct parent-choice steps. Pair collisions are O(1/(i_min log^2 n)) for the fixed number of requested children, uniformly. Thus the joint probabilities factor relatively, not just with an additive error that could overwhelm rare events. Since log(n/i_k) is asymptotic to (log n)/2, the marginal weight is i_k/(2^r r! a_{n,r}^2); summing gives the stated intensity. For mixed factorial moments, different degree ranges are disjoint eventually away from 0; removing repeated indices within one range costs o(1) since its individual weights tend uniformly to zero and its total weight is bounded. Tightness and higher moment bounds permit passage to subsequential moments; the independent Poisson law is moment determinate. For i>=2 the one-node zero factor is (i-1)/(n-1) and the remaining degree coefficient is bounded by the corresponding harmonic sum power divided by r!. The root has compulsory child 2 and then zero factor 1/(n-1), giving a negligible fixed-degree contribution. This yields O(delta^2) mass near zero, extends vague convergence to [0,infinity), and bounds any lower-degree arrival before T a_{n,K} by O((log n)^(r-K)) for r<K. The joint first-arrival and at-most-K statements follow. The frozen finite-enumeration checker was inspected, not executed; it would not prove the joint limit.

## originality

PASS

The oldest-leaf process is explicitly covered by an earlier indexed record and is not credited as new. The distinct supported claim is the full fixed direct-degree hierarchy, product Poisson laws at separated logarithmic birth scales, and the resulting earlier onset of degree K among degrees at most K.

## value

PASS

Direct-child count is a natural local mark, but finding the oldest such marks probes a different rare-event regime than computing global degree frequencies. The logarithmically separated onsets and independence show both where each fixed degree first occurs and why the degree cap is attained by the earliest admissible vertex. The relative joint estimate handles real finite-tree dependence, so this is not just recovery of the oldest-leaf law or a first-moment scaling prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
