---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Direct composition of f0 and f1_delta produces the four affine branches with thresholds a=delta/2, t=2/3−a, b=1−delta. For a<x<b, normalized z=(x−a)/(b−a) obeys Q(z)=z/2 for z<2/3 and 2z−1 otherwise, strictly decreases to zero; outside the gap P is identity. Bounded convergence implies every P-invariant Borel measure lives on the fixed set; the half-interval exchange reconstructs exactly all h-invariant and ergodic measures and pointwise empirical limits. Exact inverse-branch lengths give 4−6delta; at 2/3 P=id and every basin is null. Expanding first-hit tails give P(K>=k)=1/(3·2^(k−1)). Verified four-branch substitution for 5 rational delta values on 1000-point exact grids; this does not substitute for the all-real proof.

## originality

PASS

Nakamura–Nakano–Toyokawa–Yano define the same maps and prove the special endpoint delta=1/2 invariant cycle, which is already covered. Their arcsine-law theorem concerns random iterations rather than all deterministic-core invariant measures. The explicit nonuniqueness threshold, physical-basin length law, collapse at 2/3 and geometric transient are additional statements not implied by the cited random-process result.

## value

PASS

A complete physical-versus-invariant phase diagram for a published concrete core distinguishes proliferation of invariant measures from loss of a physical measure; the exact basin length and transient law supply natural, reusable dynamics diagnostics beyond a parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
