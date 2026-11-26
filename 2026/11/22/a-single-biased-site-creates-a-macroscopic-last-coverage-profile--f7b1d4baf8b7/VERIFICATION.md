---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The defect is a persistent transition rule at vertex zero, which is also the starting site. For 2≤k≤n−1, the first of the adjacent vertices k−1,k to be hit determines which of the clockwise and counterclockwise arcs through zero has already been traversed before either absorber is hit. Thus L≥k iff k−1 wins; if k wins, every still-unvisited vertex is at most k−1. Independently derive the splitting law by excursions from zero: each attempt succeeds clockwise with probability p/(k−1), counterclockwise with q/(n−k), and otherwise returns to zero. Conditioning on the first successful attempt gives (1) and covers adjacent-to-zero absorbers (arm length one). The k=1 tail is 1, and the k=n tail is 0. Subtracting consecutive tails gives numerator (n−1)pq and D_(k+1)−D_k=q−p gives the strict mass monotonicities for unequal biases. Differentiation in p gives the positive tail derivative for nontrivial cuts. Rounding the cut at (n−1)u gives the stated CDF limit, continuous also at u=0,1. The step density obtained by multiplying each mass by n−1 converges uniformly because its two denominator factors are ≥min(p,q)>0 and the mesh width vanishes. Except at p=q, its limiting density crosses one once where p+(q−p)u=√(pq), at u=√p/(√p+√q). The absolute difference of the two CDFs there equals the claimed limiting TV. At p=q the discrete law is exactly uniform. Replay: RESULT.md §§1–5 and the excursion probabilities above. Inspected checker.py, VERIFICATION.md and the archived JSON (reports 3330 finite rational checks, including 20 visited-mask cases); did not execute the uploaded script. The proof is for fixed p∈(0,1) and does not assume reversibility or address variable defect location.

## originality

PASS

The sharp comparison is with homogeneous, time-varying homogeneous and reversible spatially varying walks. None of the inspected exact laws includes the persistent nonreversible single-site defect. The method is standard gambler's ruin; the specific response of the final location on the macroscopic scale and its quantitative separation from uniform are the distinct claims. The full Idnani–Salem paper was accessible for this review, superseding the frozen record's earlier access limitation for that source.

## value

PASS

The conclusion measures a global effect of one local perturbation: it changes the shape of the last-discovery distribution and leaves a nonzero, exactly quantified TV distance without concentrating the endpoint near the start. This separates the one-defect mechanism from fixed homogeneous drift and from uniform last discovery. The harmonic calculation is elementary, but the macroscopic comparison and explicit benchmark for spatially inhomogeneous cycle models are the substantive content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
