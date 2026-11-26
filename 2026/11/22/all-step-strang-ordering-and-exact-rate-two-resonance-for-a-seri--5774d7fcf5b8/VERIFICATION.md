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

For one exact-subflow step with row probabilities and a,b>0, both Strang products and the unsplit chain agree in the rows for starts in 1 and 2 and have the same state-0 survival e^(-ah) from 0. Thus the TV error for an initial distribution p is p_0 times the absolute signed error in the terminal probability from 0. Multiplication gives T_A=(1-r)(1-s^2), T_B=(1-r^2)(1-s), with r=e^(-ah/2), s=e^(-bh/2); their difference (1-r)(1-s)(s-r) has the sign of a-b. The unsplit T is the convolution CDF of the two waits. In the comparison with (T_A+T_B)/2, the same-side half-squares cancel; in each cross half-square reflection (u,v) to (h-v,h-u) pairs the positive triangle with the negative triangle. Both coordinates increase from the positive to its negative partner, and the strictly decreasing exponential densities give strict net positivity at every h>0. The larger approximation is therefore closer in absolute error even if it overshoots. Subtracting the convolution CDF gives T_A-T = bh exp(-(a+b)h/2) times the difference sinhc((a-b)h/2)-sinhc(bh/2), with the swapped formula for T_B-T. Evenness and strict increase of sinhc with its nonnegative argument give sign(a-2b) and sign(b-2a), including the equal-rate continuous case. The zeros give full matrix exactness, not just one statistic, since the remaining rows and survival entry already agree. At h=0 both are trivially exact; at a=b, h>0 the errors are equal and nonzero. The large-step equivalents for a>2b follow by retaining the e^(-bh) term in T_A-T and the e^(-bh/2) term in T_B-T. A signed terminal-probability bias for an arbitrary initial row scales by p_0 and is zero when p_0=0. Inspected the supplied high-precision verifier, not executed: its 3937 cases include 12 resonance cases and are finite corroboration only.

## originality

PASS

The supported distinct contribution is the joint all-positive-step worst-initial-state TV ordering, strict midpoint bound and signed threshold classification for the irreversible serial chain. The fast-outside rule in a different splitting setting and the invariant-commutator mechanism for exactness are antecedents, not independent novelty claims here. No retrieved distinct result covers the whole serial-chain comparison.

## value

PASS

This minimal irreversible cascade isolates a genuine practical choice between two symmetric schemes with identical substep budgets. The preferred order is uniform over the whole timestep range, which is not a conclusion of a local-order calculation; the bias thresholds and exact cancellation locate a sharp exception to the generic splitting error. The result gives a benchmark for checking kinetics splittings without claiming an ordering on arbitrary reaction graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
