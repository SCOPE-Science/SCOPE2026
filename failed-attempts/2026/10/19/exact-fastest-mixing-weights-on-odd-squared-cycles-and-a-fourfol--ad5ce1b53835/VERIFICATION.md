---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Averaging over the cycle symmetries reduces the value, not the optimizer classification, to two orbit weights. On a=Rb, the Fourier drop is bF(c_k) and F is a strictly concave quadratic with vertex (c_++c_-)/2; equal endpoint values are its strict minimum on the grid. With y=π/(2n) the vertex is −sin(3y)sin(y). For n≡1 mod 4 the proposed d=sin(y) is separated from the lower neighboring cosine by the midpoint −sin(y)cos(2y), strictly below the vertex; its upper neighboring midpoint is positive. For n≡3 mod 4, d=−sin(y) is separated from the lower neighbor by −sin(3y)cos(2y), again strictly below the vertex, and the other midpoint is positive. These comparisons use 0<y≤π/14 and include n=7, so d is the unique grid maximum on the nonconjugate half-grid. Feasibility follows from E+M−4(1+R)=4(1−C)[1/2+2C+2C²−(1+2C)d], with C=cos(π/n), |d|<1/2, making the bracket positive. After balancing the extreme drops, the difference from any other circulant multiplier, divided by 1−c, is affine in c. It cannot be nonpositive at the two positive contacts and nonnegative at the interior negative contact unless identically zero; this proves the lower bound and invariant uniqueness. With t=π/n, E=16t²+O(t⁴), M=4+5t²+O(t³), R=3t²+O(t⁴), giving the stated weight and gap expansions. The step-two-only graph is isomorphic to a cycle because n is odd; balancing its extreme nonconstant Fourier modes yields the stated SLEM and gap ∼2t², hence the sharp limiting ratio four.

## originality

FAIL

The earlier indexed all-size theorem 68c871d2f31e already gives this exact optimization, invariant uniqueness and three-mode contacts on the full odd range, including the fourfold gap gain versus the one-hop cycle. On odd n the one-hop and two-hop cycles alone are isomorphic. Coverage is exact, independently of the unavailable thesis and not because of similarity to the separate even-cycle record.

## value

FAIL

The quantified spectral benefit of a vanishing edge weight is valuable in the exact all-order result. The frozen odd-only record adds no independently useful new extremal statement: it specializes those weights and their asymptotics, and replaces the earlier comparison cycle by an isomorphic one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
