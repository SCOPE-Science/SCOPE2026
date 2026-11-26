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

Nontrivial additive-character orthogonality gives the exact polynomial Gram kernel ∏ᵢ(1+z(q·1_{xᵢ=yᵢ}−1)). Under torsor translation it is convolution on H₁. Inserting the product-one constraint by multiplicative-character orthogonality yields the one-site multipliers Q+z (trivial) and qz (nontrivial); averaging over diagonal shifts gives the claimed F_[e], one eigenmode per orbit. The rational coefficients are integral by the integral Gram kernel (or by reducing the numerator mod Q, where each of the Q terms reduces to z^d). Each summand has a positive coefficient at every degree from d−m through d, so shell and band have exactly the same supported character modes. Counting excluded occupancy words and dividing by the free diagonal action proves the rank formula including the empty-sum case; balanced occupancies attain the pigeonhole bound. At k=d−1 subtract the top coefficient from q^d; integer transfers and strict convexity of q^(−m) give concentrated maxima and balanced minima of the omitted coefficient. Counting their orbits proves both spectral edge multiplicities, with Q=1 giving the single 2^d−1 value separately. The proof uses field-character orthogonality, not a prime-field-only argument. Independent direct replay at /workspace/branches/6ee37c19-4ac8-46e6-9d38-3b7adc500732/independent_check.py corroborated the rank-58 case and last-band extrema 156 and 500 in F₅,d=4, and 21 and 48 in F₄,d=3. The submitted checker was inspected, not executed; its broader recorded run is self-review evidence.

## originality

PASS

Credit only the weighted additive-frequency multimode spectrum and its sharp last-band spectral consequences, not the diagonal quotient or the previously covered occupancy rank threshold. The closest same-variety and same-checksum results inspected do not already evaluate this weighted operator.

## value

PASS

The all-degree character law gives exact small and large singular levels on a natural finite-field multiplicative observation variety, not just identifiability. At the last proper band it identifies both worst and best stability modes, with exact condition number and extremal multiplicities. These are meaningful sampling invariants across all q and d; the known occupancy threshold is not counted toward this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
