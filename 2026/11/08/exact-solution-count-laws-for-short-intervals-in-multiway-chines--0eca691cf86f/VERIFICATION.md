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

The generalized CRT gives exactly one solution modulo the lcm per compatible tuple. All pairwise compatibilities are equality modulo g, and a cyclic interval of length at most g injects under that projection. Hence H is the common arc intersection size and each reduced start tuple has the same product of lift counts. Nesting gives the upper endpoint; laying the complementary arcs consecutively projects an integer interval of total length sum(g-a_i), giving the lower endpoint. A move of one start by a single step changes the count by at most one (one point enters and one leaves), and the start space is connected, so no count between the endpoints is missing. For a nonempty r-subset with gaps d_j, a complementary arc of size g-a fits into d_j-1 empty points in max(0,d_j+a-g) ways. When a=g all g starts are possible, consistently with the same formula by summing the d_j. Marking a point of the subset counts each r-subset r times among g choices of first marked point and ordered gap compositions. This proves B_r=sum_starts binom(H,r), including the separate r=0 term; binomial inversion gives the histogram. Ordered-pair indicator summation gives the stated second moment, including displacement zero, and the expectation follows from single-point inclusion probabilities. Independent exact replay (python3 /workspace/review_replay.py, section 1) used bit masks of actual residues modulo the lcm at every original start in four chosen cases, including g=1, a zero-length interval, a full projected interval, and a four-modulus case. It corroborates the extrema, gap moments and ordinary moments on those cases only. The frozen verifier was inspected but not executed.

## originality

PASS

Distinct result on current evidence is the full discrete varied-length common-gcd law together with its interval of attainable counts. Generalized CRT, coverage moments/inversion as a method, and the two-modulus density problem receive prior credit. The older random-coverage full-text gap limits historical confidence, not the mathematical verdict.

## value

PASS

The common gcd is a natural tractable noncoprime regime of the multiway interval problem. The result tells when every placement is solvable, gives every possible solution multiplicity, and evaluates the full finite law under a natural random-placement model rather than only its expectation or a lower bound. The solution provides a reusable heterogeneous coverage law on a discrete cycle, even when direct enumeration over the original larger moduli is undesirable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
