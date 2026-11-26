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

The frozen version conflated the minimum 2-adic valuation with the minimum magnitude: at n=5 the empty coefficient is 5 but a singleton coefficient is 1, and the gcd is 1. Taking the empty frequency also left odd common factors unaddressed. The replacement distinguishes these facts and proves the full gcd: the exact ear profile A={1,n−1} has multiplicity one by inclusion–exclusion over the independent subsets of a path on L=n−5 vertices. The resulting coefficient of z^(L+1) in C(z(1−z)) is 1 since C(z(1−z))=1/(1−z) by the formal Catalan recurrence. Walsh inversion implies the gcd divides 2^n. The core theorem follows independently: prescribed independent ears can be cut off yielding C_(n−k−2) extensions (with n−k≥3), and the signed product expansion gives the stated Walsh identity. For N=n−1 the k≥2 prefactors have valuation k+s_2(N−k)−1≥s_2(N), by k−1≥s_2(k) and subadditivity. The singleton prefactor has valuation s_2(N−1), at least s_2(N) in odd polygon size and exactly s_2(N)−1 in even size. This proves both laws, and the character basis gives the asserted determinant and rank bounds. It also shows the already dyadic gcd has exact valuation v_n.

## originality

PASS

The existing full-diagonal modulo-four theorem already covers the restricted odd cases with v_n=0 or 1; the repaired statement assigns that credit explicitly. The supported distinct core is the sharper odd-order congruence for v_n≥2 and the even-order all-frequency parity stratum. Known Catalan valuations and ear-count ingredients are not claimed as new, nor is independent priority claimed for the repaired gcd proof's auxiliary counting identity.

## value

PASS

The natural short-diagonal observation sector admits all-frequency invertibility, even when the entire diagonal observation space can have cancellation. The higher-dyadic modulus settles the nontrivial infinite family of even Catalan counts beyond what unweighted parity or modulo four proves, and the even-order law gives a guaranteed nonzero half-spectrum without pretending to settle the rest.

The dated certificate retains the supplied scientific assessment, sources and limitations.
