---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For fixed skew A with 0<a_ij<1 above diagonal and iid fair signs, each coordinate X_{n,i} is a bounded martingale. Its exact conditional square increment is Xi²(A X)_i², so the sum of expected increments is finite and the almost sure limit Y obeys Yi(A Y)_i=0. In any support with ≥2 positive coordinates, its smallest index has strictly positive row interaction, contradiction; therefore Y is a simplex vertex. Martingale expectations give P(I=i)=x_i, even from boundary starts. For initially all-positive x, factors remain in [1−ρ,1+ρ]; log increments converge in Cesàro to iid log(1+σ a_{ji}) at a realized vertex, and a common SLLN event gives loser exponent 1/2 log(1−a_{jI}²). The use of signs from the original iid sequence is legitimate even conditioned on I since the SLLN is an unconditional probability-one event. Exact rational one-step checks and small sign-word enumeration corroborate but do not prove the infinite result.

## originality

PASS

Generic bounded martingale convergence does not force vertex limits, and published random Volterra vertex-convergence theorem requires support containing a map with a squaring coordinate; the two strict-amplitude opposite maps lack such a map. Exact initial-weight fixation and pairwise extinction exponents are a distinct natural transitive subfamily.

## value

PASS

The exact fixation law equal to starting fractions and pathwise pairwise loss exponents under a natural unbiased environmental switch yield an interpretable general-dimensional theorem. It separates stochastic coexistence uncertainty from deterministic transitive advantage, going beyond routine martingale convergence by proving vertex support collapse.

The dated certificate retains the supplied scientific assessment, sources and limitations.
