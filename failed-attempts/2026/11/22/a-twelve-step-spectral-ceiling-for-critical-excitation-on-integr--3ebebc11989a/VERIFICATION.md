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

Excitation sets two steps apart are disjoint. Between E_t and its two disjoint adjacent-time sets the two lower contact bounds add to r(|E_t|+|E_(t+1)|), while the degree budget is 2r|E_t|. Periodicity forces equality at each time. At every excited vertex both adjacent-layer counts must then equal r, and it has no other neighbors; equally, from the other endpoint, vertices outside the two layers have no contact into E_t. Thus the displayed pointwise vector recurrence is valid even at those vertices. At a supported temporal root of unity ζ, r(ζ+ζ^−1) belongs to the adjacency spectrum, so integrality implies that ζ+ζ^−1 is both rational and an algebraic integer. The values −2,−1,0,1,2 give orders 1,2,3,4,6; full states are recovered from two consecutive excitation sets. Refractory exclusion rules out a nonzero orbit of period dividing two. Under the spectral avoidance only ±1 temporal roots survive, forcing all-rest on every recurrent trajectory, hence eventual extinction on a finite graph. The strongly regular quadratic gives exactly the stated spectral values and exclusions for the two examples. The three cycle witnesses are direct rotating words, with lcm(3,4)=12 for their union. The three supplied scripts and output logs were inspected, not executed. The extinction argument retains spectral integrality and does not give a bound on transient length.

## originality

FAIL

The central theorem is not scientifically distinct from demonstrable existing catalogue coverage. A distinct same-day arithmetic-extinction text reproduces the exact critical contact identity and Fourier period-divisibility proof. Although its headline conclusion has extra connectedness and vertex-order assumptions, the proof of divisibility uses neither the vertex-order hypothesis nor its later signed-kernel argument; it applies to each component and hence to the arbitrary regular graph. Its same spectral formula implies the proposed avoidance criterion just by removing the three corresponding eigenvalues. This verdict is about verified mathematical coverage, not which of the two records came first: the arithmetic paper's wording is compatible with its being a downstream application, and no chronological or attribution claim is established by the shared date or by that wording alone.

## value

PASS

Independently of attribution, this is a strong structural conclusion for a natural critical threshold. The contact-budget linearization explains why an adjacency spectrum constrains every recurrent trajectory, and yields critical extinction on natural triangle-free graphs where neither a triangle-coverage characterization nor an above-half threshold argument decides the dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
