---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For a real unit vector x the inactive coordinates have a strict gap at zero; the slopes of the active affine pieces give right and left derivatives max and min of sign(x_i)y_i on the active set. Convexity gives sign straddling. Rounding y (normalized first, which does not affect orthogonality) zeros some of these products, preserving straddling, and rounding x leaves its active signs unchanged. A pair rounding to the same projective ternary point has uniformly strict same-sign products, so cannot be an edge. On ternary lines the directed test fails precisely for signed support inclusion in the directed sense; the ternary graph is induced and rounding fixes it. A uniformly signed, uniformly ordered coordinate chain meets each rank uniformly modulo antipodes; the Lubell sum bounds every antichain by the largest rank, which attains equality. The rank ratio 2(n-k)/(k+1), with the tie at n=2 mod 3, gives the stated rank including n=1. Stirling at the Bin(n,2/3) mode gives the stated asymptotic. The supplied verify.py and recorded grid/chain checks were inspected and are only diagnostics; the proof requires no replay or finite-grid extrapolation.

## originality

FAIL

The distinct October 18 Resultary record states and proves the same unrestricted real projective clique number, maximizing rank and asymptotic using the same projective signed active-support obstruction and LYM bound. It is exact coverage, not merely the October 11 lower bound. Rounding as a graph retraction is directly implied, not a substantive surviving claim: apply the earlier pairwise obstruction to a two-vertex clique to get incomparable images. For incomparable ternary patterns, in each orientation there is either a zero on the active support or both product signs, which gives directed orthogonality from a constant coordinate or max(|1+lambda|,|1-lambda|) >= 1. Rounding fixes these ternary lines. The decision uses actual mathematical coverage, not ordering inferred solely from dates.

## value

FAIL

The unrestricted clique invariant would be meaningful if new. Here the exact answer and the signed-pattern reduction are already available, and the explicit retraction wording is a routine consequence of that reduction, with no additional distinct theorem of demonstrated value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
