---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and proof checks

Run `python3 verify.py` alongside `RESULT.md`. This self-contained standard-library script checks the finite model with rational parameters \(q=1/2,2/3,1/4\), by enumerating every ordered two-parent history for two through six vertices. It independently computes finite expectations of triangles and centered triples using exact parent probabilities, then compares the two computations. It also checks stationary geometric-sum identities at rational parameters, exact derivative polynomial identities, and isolating signs giving distinct positive critical roots. An unmodified run prints `PASS 58 exact/direct enumeration, limit-sum, algebraic and root checks`.

These finite computations cannot establish an infinite strong law. For that, inspect the stationary two-sided geometric-age coupling and finite-range truncation argument in `RESULT.md`. Its critical conditions are: independent with-replacement choices, fixed \(0<q<1\), summability of \(q^j\) for couplings at the initial boundary, finite moments of stationary degrees, and Birkhoff's theorem for the shift of independent geometric-age pairs. Rational polynomial signs plus Descartes' rule prove global uniqueness rather than merely locating numerical maxima.

Only self-review have been conducted; no independent mathematical audit or certification is asserted.
