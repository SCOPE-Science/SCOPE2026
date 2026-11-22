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

# Verification protocol

Run `python3 verify.py` using a standard Python interpreter. The script requires only the standard library. It builds an independent direct diagram enumerator by iterating over both new vertices' old-pair link bits and the set of old points forming triples with the two new vertices, rejecting diagrams violating any tetrahedron clause. It separately computes the predicted count using the core-restricted allowed-pair-state formula and checks agreement.

The verified core families have one old triple, two old triples sharing a pair, three old triples on four vertices, or no old triples. For all of them, exact finite inequalities and the rational second-order coefficients are checked through twenty named old vertices. Each selected core with at most four vertices is also directly enumerated at every admissible base order through four. A further exact third-factorial-moment inequality bounds the difference between the count ratio and the first two terms of its expansion for all tested sizes.

Expected final output lines are `EXACT_FORMULA_AND_STRICT_INEQUALITY_OK` and `THIRD_MOMENT_REMAINDER_BOUND_OK`, both recorded in `verification_output.txt`. These tests do not establish the full infinite proof: that proof uses free amalgamation, a one-coordinate monotone coupling inequality, exchangeable finite-subset inclusion probabilities, and explicit uniform tails of successive binomial weights as stated in `RESULT.md`.

The calculation is exact integer/rational arithmetic. No stochastic samples, numerical integration, proprietary dependencies, or external certifications are used. The scope is the specified tetrahedron-free three-hypergraph; replacing it with the stricter \(K_4^-\)-free age changes the admissibility rules.
