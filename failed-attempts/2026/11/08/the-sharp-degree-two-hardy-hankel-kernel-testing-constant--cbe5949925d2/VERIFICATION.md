---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The standard Hardy rank-two matrix [[bar a,bar b],[bar b,0]] has norm (|a|+sqrt(|a|²+4|b|²))/2. Normalizing to norm 1 gives s=1−t² for 0≤t≤1. Independent exact SymPy polynomial expansion verifies BOTH displayed identities F_t(t/2)−25/27=(8−3t²)(3t²−2)²/432 and the positive factorization of 25/27−F_{sqrt(2/3)}(r). Their signs and equality cases yield the exact 5/(3√3) ratio and |a|/|b|=1/√6. Complex phases are optimized via w; monomials alone attain the norm via kernels. Finite numerical sampling not used for universality.

## originality

FAIL

Decisive direct coverage by full previously published same-object theorem: Same H_{bar(az+bz²)} and Szegő kernels, proves exact N/G=3√3/5, optimal equality |a|/|b|=1/√6 and radius 1/√6. Inverting inequality yields new record exact 5/(3√3). This is a mathematical implication comparison, not a search absence or guessed chronological priority. No independent novel precise claim survives.

## value

FAIL

The optimal quantitative reproducing-kernel testing bound for all quadratic Hardy Hankel symbols is mathematically natural, but its exact constant, global minimax and equality family already appear in the earlier full same-family theorem. The alternative single-test polynomial certificate is a short proof variant and not a separate substantive discovery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
