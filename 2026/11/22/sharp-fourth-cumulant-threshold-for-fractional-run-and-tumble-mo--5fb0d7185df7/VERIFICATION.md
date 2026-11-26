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

Reversibility identifies the one-time law with the forward power-weighted integral. At four ordered times the sign-increment parity gives the adjacent-pair product as the fourth moment; subtracting the three pairings cancels that one and leaves twice the negative of either crossing pairing. The cumulant prefactor is consequently −2·4! v₀⁴/Γ(n)⁴. Write the three gaps as x,y,z and the base time as s. The gap kernel e^{−2γ(x+2y+z)} has total mass 1/(16γ³). After factoring s^{4n−4}, expansion of ∏(1+partial gap sum/s)^{n−1} has a gap-integrated O(1/s) error by the mean-value theorem with a polynomial gap majorant. Local ordered integrability follows from n>0 and the exponential controls remote gaps. For n≥1, on the excluded strip s+x+y+z≥t, its s-width is at most x+y+z, and the power product is bounded by t^{4n−4}(1+x+y+z)^{4n−4} for t≥1; the resulting error is O(t^{4n−4}). For n<1 use s≥t/2 for the same power bound and strip width; for s<t/2 use x+y+z≥t/2 and peel off an exponential tail, retaining an integrable weight locally and at most polynomial growth in t. Thus the finite-time truncation cannot alter the leading cumulative tail, and at n=3/4 the remainder is bounded. Integrating s^{4n−4} gives the exact finite negative limit, critical logarithm, and power regimes and their amplitudes. The variance repeats the argument with two times and mass 2∫₀∞e^{−2γx}dx=1/γ, yielding its 1/2 boundary and all five excess-kurtosis limits/rates. In particular Γ(1/2)^2=π and (2n−1)^2=1/4 at n=3/4, giving the stated critical prefactors.

## originality

PASS

The supported distinction is the all-real-order fourth-cumulant threshold, exact amplitudes and standardized rates, not the telegraph model, its variance localization, filtered-cumulant negativity, or previously solved integer-order examples. Available exact-family and catalogue statements do not supply the all-index tail classification. Primary passage access was incomplete and an older direct general asymptotic specialization remains possible.

## value

PASS

The same physically motivated family has a gap between width delocalization and divergence of the connected fourth moment. The exact n=3/4 threshold, including its logarithmic coefficient and the change in kurtosis rates, resolves that distinction quantitatively and gives benchmarks for non-Gaussian corrections. Negativity alone would not provide these rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
