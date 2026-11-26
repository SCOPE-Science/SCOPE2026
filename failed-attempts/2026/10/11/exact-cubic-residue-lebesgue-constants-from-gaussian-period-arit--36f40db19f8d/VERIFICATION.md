---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Fourier inversion gives the normalized convolution kernel; the apparent sign difference in the exponential is harmless since −H=H. Its column sum gives the ℓ¹ norm (attained at a point mass), and its row sum gives the ℓ∞ norm (attained by a sign test at one output). Barcanescu §VI.2 gives the completed period polynomial with exactly this L convention. The shift by −1/3 gives the displayed depressed cubic and the cosine triple-angle formula, with max at θ and min at θ+2π/3. Negative σ₂ excludes three roots of one sign, and the sign of the nonzero constant product selects the exceptional sign: the absolute sum is 1+2ηmax or −1−2ηmin. Both advertised constants follow. A fresh bounded cosine-sum calculation over the 80 eligible primes ≤1000 gave branch counts 43 and 37, with maximum formula discrepancy 8.9×10⁻¹⁵; p=7 and p=13 give 1.28398834498 and 1.63144209781 in opposite branches. This reproduction is corroborative; the cited polynomial and algebra prove the universal statement.

## originality

FAIL

The complete multiset needed for the proposed exact invariant is already given by a classical theorem for these exact cosets, and the norm and sign split are routine consequences of that stronger data. This is a coverage-by-implication finding, not a claim that an earlier source printed the exact endpoint formula. The corpus search failed with an HTTP 503 and is not counted as negative evidence.

## value

FAIL

This is a natural subgroup and a correctly computed invariant, but the exact result is mechanically implied in this case. The entire output is an absolute sum of an already explicitly known spectrum, simplified by elementary sign and cubic-root identities. The branch presentation by itself gives no new arithmetic constraint, distribution result, extremal statement or unresolved estimate beyond that spectrum. The rejection is specific to the routine deduction here, not to the small length of a proof or to exact invariants in general.

The dated certificate retains the supplied scientific assessment, sources and limitations.
