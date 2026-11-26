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

At c=1/r both branch values are 1; 0 and 1 map to 0. The right branch is decreasing on the stated range, with derivative magnitude bounded below by r(2−r)/(r−1)>1 exactly up to φ on the monotone range. Both inverses contract. Their nested cylinders partition the interval up to endpoints, generating the dynamics; the full two-shift codes them. The only multiple codes belong to preimages of c, which are countable transient points eventually sent to 0, and thus null for any invariant law. The fair Bernoulli pushforward has entropy log 2, and uniqueness follows by lifting other invariant laws via the itinerary (defined off those null ambiguities) and using the unique full-shift maximal-entropy law. The all-left cylinders are precisely [0,r^(−n)], of mass 2^(−n); floor-bracketing gives log μ_r([0,t])=(log 2)log(t)/log(r)+O(1) with bounded rounding error. This proves both the fixed-t limit as r↓1 and the local dimension at 0 as t↓0 for fixed r. For typical dimension, each branch has half the measure. The derivative bounds give χ_r=(1/2)log(1/(r−1))+O(r−1). For each fixed r, summable distortion of inverse cylinders follows from expansion and Lipschitz log derivative on each branch; Birkhoff gives cylinder length exp(−nχ_r+o(n)). To verify the ball comparison independently, the left endpoint mass is bounded by a power of the radius; the right endpoint also has such a bound by mapping its small neighborhood via the right branch into a left endpoint neighborhood of radius at most a times as large. Invariance and Borel–Cantelli then put typical f_r^n(x) at distance at least exp(−εn) from both endpoints eventually. Distortion transfers this to the cylinder about x, so both a containing ball of cylinder size and an inscribed ball of radius at least a constant times exp(−εn) times that size give the local dimension log 2/χ_r as ε↓0. This is measure dimension, not support dimension. It tends to zero while the exceptional dimension at x=0 diverges, and the endpoint mass bounds give weak convergence to δ_1.

## originality

PASS

The piecewise linear/logistic family, the exact boundary-crisis curve and its trapping interpretation are prior. Full-branch coding and entropy-over-Lyapunov dimension are also standard. The qualified distinct claim is the explicit joint parameter degeneration for the maximal-entropy (not physical) law on the expanding portion of this specific curve, with sharp spatial-threshold concentration and opposite typical and exceptional dimension limits.

## value

PASS

This is a natural boundary of a known crisis family rather than a sample parameter. The canonical invariant law has unchanged full entropy, yet its mass outside any fixed neighborhood of 1 has a computable exponential rate, and the typical and exceptional dimension limits go in opposite directions. The two different geometric mechanisms (many weak left iterates versus the rapidly expanding right branch) give a useful quantitative example of what full symbolic entropy does not control.

The dated certificate retains the supplied scientific assessment, sources and limitations.
