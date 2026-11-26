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

For w=y/x, w'=kxw(w−w_*); direct differentiation gives the invariant H=x|w−w_*|^ν/w^P. Below the ray w stays bounded and x is squeezed between reciprocal affine functions of time, so the solution is global and x→0; the invariant forces w→0. Integrating (1/x)'→a yields tx→1/a and the invariant gives the stated y-amplitude with exponent 1+1/P=b/a. The ray solves x'=−γx². Above the ray dt/dw=w^(−P−1)(w−w_*)^(ν−1)/(kH_+); the upper tail has exponent −1−φ and y tends to infinity, so the integrable upper endpoint is the maximal lifetime. The change to s=w_*/w reverses integration limits and yields (4). The invariant gives xy^(b/c)→H_+^(k/c), and (1/y)'→−c gives (5). Since B−B_s=(1−s)^ν/ν+O((1−s)^(ν+1)), subtracting exactly the full w_0-dependent profile in (7) gives −1/(kνw_*x_0)=−1/(γx_0); subtracting only the leading power would not in general give that finite part. ν is positive, continuous on a connected rate region, and approaches both zero and infinity on that region. The reflection formula gives B(1/3,5/3)=4π/(3√3) and substitution reproduces both constants in (8). The uploaded verification instructions and code were inspected, not executed; the analytic identities, not the claimed finite diagnostics, establish these conclusions.

## originality

FAIL

Maier's earlier exact two-dimensional integration covers the whole rate family and the original physical time, not just orbital geometry or one rate choice. The finite blow-up clock is a direct endpoint of that exact parametric solution. The ancillary latency exponent, amplitude, finite part and endpoint constants are elementary endpoint expansions of the same solution; no independent substantive remainder of the advertised calculation survives.

## value

FAIL

Correcting the concrete example's physical-time description would be useful as a clarification, and the normalization of the beta tail is well defined. But as a new mathematical finding this is the direct signed scaling and first endpoint expansion of Maier's explicit clock and trajectories. No separately motivated invariant, nonroutine extension, or other substantive surviving result was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
