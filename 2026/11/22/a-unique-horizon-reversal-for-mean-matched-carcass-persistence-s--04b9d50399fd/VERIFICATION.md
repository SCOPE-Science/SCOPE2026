---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For a carcass present at both visits, the two detection attempts yield one distinct record. For arrivals before t₁ the duplicate probability subtracts p²S(t₂−s); for arrivals between visits only the second attempt contributes. This integrates to C(t₁)+(1−p)C(t₂)+pC(t₂−t₁), after dividing by the positive intensity times p. Its derivative in the second date is strictly positive even at the terminal-cluster boundary, giving t₂=H. In the first date the derivative S(t₁)−pS(H−t₁) strictly decreases from a positive value to S(H)−p. This gives a unique maximum, terminal even at equality and otherwise strictly after H/2. Independent markings for Poisson arrivals justify the probability-of-any-detection equivalence. For an interior optimum set ℓ=2t₁−H and integrate the decreasing hazard over [(H−ℓ)/2,(H+ℓ)/2] to obtain L=−log p. The rate-tilted variance gives h'<0; differentiating the integral gives ℓ'=(h(a)−h(b))/(h(a)+h(b))∈(0,1). The interior skew tends to H_S at activation and to L/λ₁ at long horizons because its interval length is bounded and the hazard tends to λ₁. For M=∑w_j/λ_j the strictly convex survival ratio e^(u/M)S(u) starts at one with negative slope and diverges (λ₁<1/M), yielding one positive intersection with one. This gives H_S≥H_E iff p≤p₀. In that case there is initial equality and then the mixture always runs later. Otherwise it runs earlier after H_S through H_E; its interior skew is below H_E there and rises transversely past this comparator at exactly one H*>H_E. The two-rate example follows by factoring the quartic in z=e^(u₀/2) by z−1 and by solving exp(−(H*−H_E))=2^(4/3)−2. Replay: frozen RESULT.md lines 53–103; checker.py lines 7–44 and 103–129, inspected not executed. The result requires constant mean arrivals, no initial stock, independent equal-quality detection conditional on presence, no false positives, and distinct positive rates. If tied independent passes are forbidden, a clustered optimum is a supremum rather than an attained schedule.

## originality

PASS

The distinctive result is the detection-quality boundary and sharp one-reversal comparison of a heterogeneous persistence calendar with its mean-matched exponential calendar. The single-rate optimizer and terminal separation criterion are explicitly covered by a same-day published record; the survival/counting framework is also established. Neither is treated as the novel claim. No inspected comparator states or implies the full sign and equality classification for the mixture-versus-exponential dates.

## value

PASS

A mean-matched disappearance model can move the same optimally scheduled first visit in opposite directions as the observation window grows. The exact detection-quality boundary shows when that risk exists, and the monotone hazard-skew relation proves a single reversal rather than an isolated simulation pattern. This is useful for interpreting reduced-model calendar bias while not claiming field validation or an optimal mortality-estimation design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
