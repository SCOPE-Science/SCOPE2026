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

In Dijkstra exploration with independent exponential edge lengths, active cut-edge waiting times conditional on the exploration history are independent rate-assigned residual exponentials, by memorylessness. A chosen edge has probability its rate divided by the total cut rate, and the winning predecessor gives the true shortest-path depth. Positive continuous weights imply uniqueness and a simple path; bipartite parity and cube order restrict its length to 3,5,7. I separately enumerated vertex arrival orders, expanded compatible parent assignments, and grouped all 7368 histories by their multiset of cut-rate factors and number of third-axis transmissions. Exact polynomial arithmetic verifies all three full rational identities, normalization and the derivative factorization. The derivative's positive remaining numerator coefficients prove the sign change only at 1; substitution gives (6973/7200,7/225,1/2400), and the constant and leading coefficients give the two limiting geodesic probabilities. Under the common exponential coupling, every antipodal path uses the third axis. Testing the minimizer at the old rate in the new, strictly faster environment proves strict decrease of the passage time.

## originality

PASS

Credit the established exponential first-passage representation, Richardson exploration and asymptotic interest in optimizing path length. The verified distinction is the full exact finite-cube length law and its unique isotropic maximizer of three-edge probability along the specified directional family. The inspected sources address different regimes or path measures.

## value

PASS

Q3 is the first cube with detours between antipodes; Q2 cannot separate passage speed from geodesicity this way. The exact law explains a concrete tradeoff: increasing the third-axis rate always speeds passage, but above the isotropic point it lowers the chance of a shortest-in-hops route. An all-rate sign theorem and full finite law are more informative than an isotropic census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
