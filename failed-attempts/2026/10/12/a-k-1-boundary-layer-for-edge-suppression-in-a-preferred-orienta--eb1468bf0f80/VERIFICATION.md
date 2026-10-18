---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

From the pinned scattering S(k) and exact boundary equation, solving first two rows yields rational a/c,b/c with denominator D. The triangle estimate |D|>=2k²|sinδ|-4k-8 proves O(1/(k|sinδ|)) when k|sinδ|→∞ after cell normalization. For q=s exp(iδ), kδ→ξ and sξ≠2sinθ, D/k→2isz(sξ−2sinθ) and a/c,b/c→(s−e^{iθ})/[i(sξ−2sinθ)], d/c→1; cross terms give the stated norm ratio. Independently evaluated exact ratios for ± parity at k=10^6 and confirmed ~10^-6 errors. The pole and spectrum-realization limitations are explicit.

## originality

FAIL

FAIL decisively: an already published Resultary scientific record dated 2026-10-04 entitled Critical 1/k boundary layer for edge suppression in a preferred-orientation rectangular strip states the same local suppression regime, the same R_{s,theta,xi}, the same pole sξ=2sinθ, and precisely the same edge mass-ratio formula. Its full pinned RESULT.md was read and compared equation by equation. Rephrasing sinδ versus δ does not change the restricted δ→0 critical result; the wider non-resonance suppression follows by the same denominator estimate. This prior record directly covers the assigned final claim.

## value

FAIL

FAIL: the asserted refinement and complete transfer profile are scientifically motivated but are already established in the earlier same-object, same-scale, same-Floquet-parameter work; repeating them with a different denominator representation adds no independently useful new theorem, boundary or certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
