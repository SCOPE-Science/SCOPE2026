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

For p>=7 and exactly three nonzero entries in each input, prime Fourier row uncertainty gives p+1-k_x surviving frequencies for each active delay. Summing overlap sizes 9 yields S >= |F-G|(p+1)-9. Cauchy-Davenport forces >=5 delays, and >=6 forces S>=6p-3. Vosper applies when |F-G|=5<=p-2, forcing two common-step 3-term progressions. On normalized supports 0,1,2 the outer STFT rows have no zeros, two adjacent linear rows each have at most one and the central quadratic at most two; the precise count 5p-1_{r_- in mu_p}-1_{r_+ in mu_p}-h follows. Vieta gives z1z2=r_-r_+, excluding three cancellations from two distinct central roots with one side root; hence the 5p-3 double-root classification. Explicit nonzero coefficient witnesses attain every 5p-4..5p and 6p-3. The finite floating-point checker was inspected but tolerance-based detections are only consistency checks, not exact or unbounded proof.

## originality

PASS

Best-of-knowledge statement-and-implication comparison: The phase-only three-tap optimizer-topology theorem uses the same 5-delay polynomial representation but enforces unit-modulus amplitudes; its support set {5p,5p-1,5p-2} and topology do not determine unrestricted amplitude low levels 5p-3 or 5p-4 or inverse geometry for arbitrary supports. Krahmer-Pfander-Rashkov Proposition 4.4 covers the numerical 5p-4 bound, and prime-order Fourier uncertainty/Cauchy-Davenport/Vosper yield ingredients; their compared statements do not enumerate all five low levels, the gap onset 6p-3, or this coefficient equality characterization. The searched phase-only three-tap and two-sparse STFT tables concern restricted coefficient classes or two supports, so none gives the requested arbitrary six nonzero coefficients. A hidden historical full table remains a priority risk.

## value

PASS

The complete low-support spectrum and growing forbidden gap, Vosper inverse support rigidity and exact coefficient-level extremizer classification answer a natural fixed-sparsity discrete time-frequency question beyond the known minimum; the two independent-window levels are not captured by phase-only/self-window results. This is an all-prime structural theorem, not a tiny negative test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
