---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Independent analytic reconstruction: on input degree k the weight numerator is h! binom(k-j+h,h) for k≥j and zero otherwise, with denominator sqrt((k+2h)!/k!). Pascal's identity, also at k=j with the cutoff, gives (−1)^r h! binom(k-j+h-r,h-r) for k≥j, r≤h, then (−1)^(h+1) h! at k=j only. Thus the normalized matrix unit has the stated sign and scale. The lower differences have absolute tail weights asymptotic to h!/(h-r)! times k^(−r). Orthogonality makes singular values their decreasing rearrangement, which preserves the power asymptotic by tail counting. Summability and the endpoint logarithmic coefficient follow. The units span the finitely supported weights; their closure is c0, and one generator differs from the constant-weight shift by a c0 sequence. Finite rank requires the tail polynomial to vanish, hence all moments through h vanish by triangularity, which excludes at most h+1 distinct indices by Vandermonde. The finite frozen checker was inspected, not executed; the analytic check suffices.

## originality

FAIL

The distinct earlier-indexed Resultary moment-filtration record states the exact same-family rank-one formula and a stronger theorem for arbitrary finite combinations. Every other headline conclusion is explicit there or mechanically implied, including the norm closure. This is demonstrable mathematical coverage, not a judgment about provenance.

## value

FAIL

The exact finite-rank and spectral structure is intrinsically useful, but the proposed addition to it is only the immediate closure of known coordinate units and a known convergent weight sequence. There is no distinct substantive addition warranting a repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
