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

Differentiating the symmetric Gaussian interval probabilities gives a positive prefactor times a sum of 2m distinct exponentials at t=1/(2σ²). Rolle induction bounds distinct critical points by 2m−1, including at least one intervening stationary point for each consecutive pair of strict maxima. A remote [R,2R] band preserves the old derivative signs on compact windows and creates a new change from + to − in the rescaled window; analyticity makes the resulting maxima strict. For the tie, the two isolated band optima have strictly negative second derivatives; the near perturbation and its q derivative are exponentially small, and the far perturbation is √(2/π)/(Ru)+O(R⁻³) in C² on the necessary compact window. The two resulting peaks exhaust global possibilities by the mode cap, analyticity and vanishing tails. The envelope derivative of the far-minus-near gap is M′(q)+O(1/R)>0 uniformly in the closed q interval, and the endpoint gaps have opposite signs. The first-order root shift is −φ(0)/[Rφ(2/s(2))]=−2^(4/3)/R. Separately replayed the concrete witness with integer numerator signs +,−,+,− at the four stated rationals (python3 /workspace/branches/review_replay.py 1); the count follows exactly from the analytic bound, not a numerical root scan. Inspected but did not execute the supplied checker.

## originality

PASS

The distinct content supported here is the sharpness construction in the centered Gaussian band family and, most substantively, the two-scale exact global-tie theorem with uniqueness in the specified interval and a first-order width shift. The exponential-sum zero bound and general observation of an intermediate optimum are not new.

## value

PASS

The sharp count relates a geometric input (number of separated bands) to the number of competing scale optima; the exact degeneracy boundary answers when two very different dispersal scales can be equally optimal. Its nonzero first-order shift is analytically useful because it quantifies the failure of treating widely separated bands as independent optima. These are structural features of a natural Gaussian benchmark, not evidence for a particular management recommendation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
