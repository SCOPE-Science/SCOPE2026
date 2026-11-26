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

Independently checked by a velocity-resolvent calculation. With F(v,s)=∫ exp(−rt) E[v_t | v,s, no resets] dt, first-reset conditioning and telegraph relaxation give D=E[vF(v,s)]+r E[vs]F(0,+)/(2λ). The reset age A is exponential and |v|≤aA. Coupling nonlinear and linear zero-start excursions to the same orientation path gives a velocity difference O(t⁴) uniformly (variation of constants and |g(v)−γv|≤C|v|³). On a no-flip excursion it is −κs a³t⁴/4+O(t⁵); the flip event has probability O(t) and therefore changes the expectation only by O(t⁵). Thus the changes in F(0,+) and in E[vs] are −6κa³r⁻⁵+O(r⁻⁶) and −6κa³r⁻⁴+O(r⁻⁵). The same coupling bounds the change in the short-excursion product integrand v₀v_t by C(A+t)⁵, so its discounted integral is O(r⁻⁶). In the long term E[vs]~a/r and F(0,+)~a/r², producing two equal fifth-order contributions. The linear generator gives E[vs]=a/(r+γ+2λ), E[v²]=2aE[vs]/(r+2γ), and D=(E[v²]+aE[vs]/(2λ))/(r+γ). Compactness, odd symmetry and coupling after orientation coalescence and a reset justify the integrable centered covariance. The tan/tanh coefficient and sign follow from their cubic coefficients ±1/3. The result is for fixed λ>0, and fifth order distinguishes drags only if their cubic coefficients differ. The frozen rational checker corroborates a first variation; it is not the proof for arbitrary fixed κ.

## originality

FAIL

A distinct indexed record states the same fifth-order fingerprint, exact linear reference and tan/tanh comparison under the same reset protocol. The frozen result allows weaker regularity and dissipativity than the indexed theorem, but does not identify a distinct coefficient or a materially new regime: matching the local expansion to a smooth locally monotone reference makes the drag discrepancy O(v⁵), and the same age and resolvent estimates give O(r⁻⁷) in diffusion. The central fingerprint is therefore already covered. This is an assessment of coverage, not an attribution of historical priority based on catalogue dates.

## value

PASS

The fifth-order law itself answers a physically motivated question left by the shared leading r⁻² scaling. It gives a signed, quantitative discriminator and explains why earlier orders cannot separate these two drag laws. This scientific significance does not make equivalent catalogue coverage original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
