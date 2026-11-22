---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Character orthogonality gives M4=Σ_h |C_h|² with C0=7 and each of seven nonzero autocorrelations a sum of three paired real phase products. Dividing out the common root-of-unity scalar gives exactly q^6 arrays. Independently enumerated all 67,170 q=2,3,4,5,6 normalized arrays with exact integer and Q(√5) representation: minima 109,67,61,66-3√5,61 and counts 56,168,224,336,2688 match. The inspected verify_fano.py enumerates every 168 GL(3,2) coordinate relabellings, checks the reported orbit partitions and recomputes the moment by direct eight Walsh samples for every minimizing array; that orbit implementation was inspected but the current independent enumeration checked minima/counts, not reimplemented all orbit partitions. Finite exhaustion is mathematically sufficient for this fixed finite claim.

## originality

PASS

The punctured Walsh spectrum of seven nontrivial F2^3 characters is different from full eight-tone Fourier or planar aperture groups. Fan–Xu gives broad group-action bent Fourier tools but not q=2..6 constrained minimum fourth moments or GL3 minimizer orbits in the inspected sections. The published co-singleton Λ(4) result maximizes a norm with variable amplitudes, not the fixed-modulus minimum. Searches did not find an earlier exact Fano-plane constrained phase table; publisher-only later Fan–Xu material and specialist Walsh arrays remain risks.

## value

PASS

The canonical Fano-plane punctured Walsh aperture has a concrete phase-quantization extremal problem. Sharp finite-alphabet minima and complete minimizer orbit types show a nonmonotone engineering-relevant phenomenon: 5 roots outperform 4 and 6 roots in the integrated fourth moment. This exact finite invariant and orbit census are motivated and not a mere normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
