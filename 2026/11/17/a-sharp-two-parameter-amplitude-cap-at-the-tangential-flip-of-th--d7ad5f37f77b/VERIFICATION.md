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

For f=x²exp(r-x)+k and q=2+sqrt2, r_c=q-log(2+2sqrt2), exact evaluation gives f(q)=q, multiplier -1, f’’(q)=0, f’’’(q)=2/q. The symmetric equations H1=[f(m+A)+f(m-A)]/2-m=0 and H2=[f(m+A)-f(m-A)]/(2A)+1=0, analytically extended in U=A², have nonsingular (m,U) Jacobian diag(-2,1/(3q)). Implicit differentiation gives U_r=3q,U_k=0,U_kk=-3/2, hence the quoted parabolic two-parameter cap and unique local cycle. Independent symbolic derivatives, independent two-cycle numeric roots across detunings and multipliers confirm the local attracting branch. The critical iterate f²(q+z)=q+z-(2/(3q))z³+O(z⁴) forces n(x_n-q)^2→3q/2 for sufficiently nearby nonfixed orbits. Claimed effects are local; excluded outside |t|>2sqrt(q) follows from U<0. Boundary parameter t=±2sqrt q is deliberately not covered by the fixed-t interior/exterior assertions.

## originality

PASS

Bounded PASS for the new evaluated coefficients of a two-parameter tangential flip normal form, suppressed mean displacement and n^{-1/2} critical relaxation for nonzero bias. The exact flip curve and generic supercritical existence are established by Llovera Trujillo et al. and explicitly excluded from novelty.

## value

PASS

At the minimum of the physical reduced-map flip line, the oscillatory regime has a two-parameter amplitude cap whose width is sqrt(r-r_c), with an unusually small mean offset and a computable slow-relaxation constant. These coefficients quantify a mathematically motivated degenerate flip rather than an arbitrary numerical parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
