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

For any admissible kernel, the norm squared of the sum of the leaf Gram vectors is d+T, where T is the ordered sum of nonnegative off-diagonal leaf entries. Cauchy–Schwarz against the unit center vector gives S≤√(d+T). Thus the form is at least d+1+T−2√(d+T)≥d+1−2√d. For the upper bound X=√d−c_d with 2<c_d≤6 exists by the half-open length-four congruence window, r=(d−X)/2 is even and ε=−κ₂/(1−κ₂) lies in (0,1) for large d. The nonnegative Fourier weights of the cosine products give positive definiteness. At a Boolean vertex the layer average is κ_v by counting intersections of a uniform r-subset with the v minus signs; complement symmetry follows from even r. The sampling identities yield κ₁=X/d, κ₂=(X²−d)/(d(d−1)), and κ₃=X(X²−3d+2)/(d(d−1)(d−2)). Hence κ₃−κ₂=2(c_d−1)d^(−3/2)+O(d^(−2))>0 uniformly. The degree-r average has squared L² norm 1/binom(d,r) by Walsh orthogonality. Stirling gives binom(d,r)≳2^d/√d, so for 4≤v≤d−4, binom(d,v)≥binom(d,4) implies |κ_v|=O(d^(−7/4))=o(|κ₂|). The low weights and their complements are thereby all checked and κ₂ is the minimum. Cube interpolation proves global pointwise nonnegativity, not just positivity on the sampled star. The leaf pairs give zero and the center–leaf value is (κ₁−κ₂)/(1−κ₂)=(X+1)/(d+X), so d(X+1)/(d+X)=√d+O(1). The comparison benchmark differs from d+1 by 4d/(d+1), yielding the second limit.

## originality

PASS

Credit the former Loewner conjecture, the finite seven-dimensional violation and the symmetric multiaffine positive-Fourier construction framework. The supported distinct contribution is sharp first-order optimization over all admissible kernels at the one-negative star, using an explicit family of globally nonnegative near-central layers that achieves the unrestricted Gram bound to O(1). The material compared does not establish equivalent coverage of this asymptotic.

## value

PASS

The fixed signed star is a natural test of the historical lower bound. The result determines the largest violation at that star to leading order and separates a universal Gram obstruction from the real extension problem of constructing a globally admissible Fourier kernel. An explicit layer reaches the leading coefficient in unbounded dimension, rather than providing just another isolated counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
