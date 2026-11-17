---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

PASS: With normalized uniform measure on k-subsets, the first-degree harmonic kernel is K(S,T)= n(n−1)[|S∩T|−k²/n]/[k(n−k)], and its L∞ row norm is n(n−1)E|J−k²/n|/[k(n−k)] for hypergeometric J. Telescoping q_{t−1}−q_t=n(t−k²/n)p_t with q_t=(k−t)²p_t gives exactly Λ=2(n−1)(k−j)² p_j/[k(n−k)], j=floor(k²/n). The sparse k/√n→c limit is Poisson mean c² and profile 2e^{−c²}(c²)^{floor(c²)+1/2}/floor(c²)!, while k/√n→0 gives zero and k/√n→∞ yields √(2/π). Piecewise log derivative puts each Poisson maximum at integer+1/2; strict descending maxima make first peak √(2/e) uniquely largest at c=1/√2. Subsequential compactness forces all maximizing ranks to that scale. Independently computed 8008 exact hypergeometric identities and sample global maximizers; infinite asymptotics rest on the analytical proof.

## originality

FAIL

The earlier November 1 Resultary result is mathematically identical on every nontrivial slice, even includes the complementary k>n/2 and complex-valued generality. This is decisive earlier full-family coverage.

## value

FAIL

FAIL: The exact endpoint norm, Poisson crossover, sharp √(2n/e) global maximum and unique asymptotically maximizing k~√(n/2) were already proved in a November 1 full finding. The assigned November 8 result contains no distinct motivated invariant, new scale, sharpened error, or additional equality theorem beyond that existing result; algebraic proof rearrangement does not confer scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
