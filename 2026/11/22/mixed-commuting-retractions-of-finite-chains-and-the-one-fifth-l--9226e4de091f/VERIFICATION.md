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

An isotone contraction has interval image, and idempotence fixes the image pointwise; monotonicity then forces the unique clamp. For an arbitrary isotone retraction with consecutive fixed points at distance d, the intervening points can only map to those endpoints and admit d choices of cut. This yields B=z(1-z)^2/(1-3z+z^2) for two anchored endpoints, E_j=sum_{i<=j}B_i for one anchor, and N(z)=z/(1-3z+z^2) for unrestricted retractions by allowing two exterior lengths. The latter gives N_n=F_{2n} by the series recurrence. Commutation is equivalent to preserving the clamp interval together with the two exterior equations. On a side whose endpoint is fixed, the side restriction is any independently chosen anchored idempotent; when it is not fixed, monotonicity and the clamp equation force all exterior values on that side to be the interior image of the endpoint. The four endpoint cases give exactly the frozen per-clamp formula, including L=1, where commutation just fixes the clamp value. Summing over lengths gives B(A+z/(1-z)^2)^2 with A=(1-z)/(1-3z+z^2), hence the displayed OGF. At r=(3-sqrt(5))/2 the dominant pole has order 3 and q(z)=(1-z/r)(1-rz) with 1-r²=sqrt(5)r. Its leading coefficient, the denominator n(n+1)F_{2n}/2 and 1-2r=r(1-r) give exactly 1/5. The independent direct enumerator agrees per clamp through n=9 and with all corresponding totals. The separate exponential-decay contrast concerns the unrestricted pair count, not this normalization.

## originality

PASS

The strongest inspected exact centralizer theorem is for an idempotent clamp centralizing arbitrary contractions, whereas the strongest relevant commuting-pair theorem allows both factors to be arbitrary isotone idempotents. Neither gives the ordered class with exactly the first factor required to be a contraction, its per-clamp count, or the 1/5 limit. The exact catalogue hit is the frozen record itself.

## value

PASS

The mixed restriction is natural for a nested pair of transformation monoids, and the explicit per-clamp centralizer is finer than the total. The all-n enumeration answers a concrete probability question and shows a qualitative change from the known exponentially sparse unrestricted pairs to a positive limiting density. This is not just a low-n difference or the known clamp count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
