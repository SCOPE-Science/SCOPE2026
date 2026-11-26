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

Reassessed the corrected RESULT.md and SLOGAN.txt. The frozen formulas are mathematically sound; the repair narrows the finding, not the graph scope. The two projector equations and complement bound b<=N give positive edge and diagonal entries and the stated common nonedge entry. The ratio of exponential defects strictly decreases from (b/a)^alpha to one, so it equals b/a just once for alpha>1; t=0 is separate. For the optimizer the gap a>1 follows because the adjacency quadratic at k-1 is at least mu k-1>0 and its lower root is nonpositive. With q=b/a and z=a^alpha T, h(z)/z increases from q to infinity and T=z^(1+delta)/h(z)^delta. The strictly increasing logarithmic derivative of h' implies h'(u z)/h'(z) strictly decreases in z for u<1. Its integral is h/(zh'), decreasing from 1 to 0 by dominated convergence at the finite singularity. Thus the logarithmic delay derivative changes from positive to negative once, establishing the repaired theorem, including strict increase and decrease on opposite sides; both endpoint delays vanish. Independently, h=z-log[1-(q-1)(exp(z)-1)] gives a positive-coefficient series on 0<z<c, for which the derivative of zh'/h with respect to log z is the strictly positive variance of the power index under the normalized series weights. In the frozen norm context, row sums and the signs give the absolute row norm, the unique minimum of the nonedge entry gives the peak, and expansion after division by t and the large-alpha scaled root give the stated boundary formulas; these are now credited background. Read the supporting checker without executing it. Independently solved F=0 and partial_alpha F=0 in physical coordinates at a=2, b=5, giving alpha*=1.6364352345084135 and T*=0.1317910588199445; the corrected RESULT includes the reproducible equations. Assumptions and fixed-graph scope are unchanged; no finite numerical test is used as a universal proof.

## originality

PASS

PASS for the repaired optimizer finding only. The frozen attribution of novelty beyond the optimizer and its characterization is not supported: a distinct same-date result gives the exact same all-SRG positivity law, norm, peak-time and endpoint statements. The corrected finding explicitly credits that full overlap and removes it from the contribution. The inspected comparisons do not give the strict global fractional-order optimization or the required elasticity monotonicity. Same-day mathematical overlap is demonstrable; within-day priority is not.

## value

PASS

The repaired worst exponent answers a structural question the sharp per-exponent horizon leaves open: whether two orders can share the worst restoration delay or whether there is exactly one, and how to find it from measured graph eigenvalues. The proof supplies a certified monotone scalar solve across an entire natural graph family and shows strict ordering on either side, not merely existence from the endpoint limits or a grid sample. The already-covered peak amplification and sign formulas are useful context but carry no weight as independent contributions in this verdict.

The dated certificate retains the supplied scientific assessment, sources and limitations.
