---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The precise sampling is two independent arclength-uniform boundary endpoints per chord; same-side boundary segments do not intersect properly. For fixed distinct-side chord, exact conditional crossing polynomial 2[p_i p_j((1-x)(1-y)+xy)+p_i p_k(1-x)+p_j p_k y] has expectation e2. Summing over edge pairs gives E(g)=2e2^2 and E(g^2)=20 e2^3/9-4 e3^2/3. Shared-chord conditioning yields Var(C3)=3q(1-q)+6 Var(g). Viete reconstruction recovers positive e2,e3 and all normalized side lengths; exact distinct triangles (4/15,4/15,7/15) and (2/5,2/5,1/5) share e2=8/25, establishing two-chord nonidentifiability. Independently checked symbolic second-moment identity and rational ambiguity. No claim of statistical finite-sample identification.

## originality

PASS

Best-of-knowledge novel relative to inspected specific priors and primary literature; residual source-access risks as recorded.

## value

PASS

A sharp minimal-observation inverse-geometry theorem: two moments of the crossing graph of three independent perimeter chords determine the triangle similarity class, although a complete two-chord law cannot. This is a natural geometric-inference invariant rather than an arbitrary small computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
