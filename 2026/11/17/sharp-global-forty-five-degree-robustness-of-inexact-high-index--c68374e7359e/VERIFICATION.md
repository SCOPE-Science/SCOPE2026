---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Let J=I-2P0 and R=I-2P. For every symmetric orthogonal projector P, the exact algebraic identity sym(RJ)=I-2(P-P0)^2 holds. The separability assumption gives J grad E=grad F, F=f+g, so dot F=-beta grad F^T RJ grad F <=-beta(1-2delta^2)||grad F||². Global mu-strong convexity implies the gradient-PL bound ||grad F||²>=2mu(F-F*); integrating gives the stated exact rate and a state-norm exponential estimate. Its compact sublevels prevent finite-time blowup for classical locally Lipschitz projectors. A rank-one planar projector rotated phi gives RJ a planar rotation by twice phi, so a quadratic achieves equality; at phi=pi/4 the flow is a pure rotation, at larger phi it expands. Embedding one mixed pair proves sharpness for all 1<=k<n. Exact rational projector identities, critical matrix and above-critical trace were checked independently, rather than treating the finite checker as proof of uniform dynamics.

## originality

PASS

Best-of-knowledge PASS within the explicitly separable, fixed-eigenspace class: global arbitrary state/time-varying projector tolerance and sharp critical counterexample are not obtained from the inspected local perturbative or discrete-time results. The algebraic reflector identity and the number pi/4 alone are classical/simple, not the claimed novelty. Closest arXiv 2611.09049 full text was inaccessible; uncertainty remains.

## value

PASS

A sharp global robustness margin independent of the upper curvature bound is useful in high-index saddle computations, especially as it distinguishes global guarantees from local condition-number estimates. Explicit periodic and expanding counterexamples prove genuine necessity, not just a sufficient inequality; separability is a natural but material restriction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
