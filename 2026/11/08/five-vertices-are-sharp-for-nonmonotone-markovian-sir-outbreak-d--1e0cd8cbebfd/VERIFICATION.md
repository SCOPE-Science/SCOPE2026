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

# Reproducible verification

Execute `python verify.py` with SymPy installed. The program constructs all connected labeled simple graphs for 1–4 vertices, forms exact graph-isomorphism classes by all vertex permutations, and evaluates the exact Markov first-event recursion. It differentiates every rooted duration rational function and proves the nonnegative-polynomial certificate symbolically for every positive infection rate. It verifies the exact five-vertex seven-edge rational witness and its strictly positive difference from the exact high-rate limit.

Execute `python verify_matrix.py` with NumPy installed for a structurally separate generator matrix calculation at transmission rate 100. The independent 146-state numerical evaluation agrees with the exact rational value. The finite numerical test does not replace the rational proof.

Run results observed: 44 labeled connected graphs on up to four vertices; connected isomorphism counts 1,1,2,6; 33 rooted symbolic derivative checks, all passed; exact rational witness positive gap; independent matrix check passed. The proof of the unbounded positive-rate derivative sign rests on exact symbolic polynomials; the large-rate expected-value limit is independently justified by uniform integrability. General graphs of five or more vertices are not exhaustively classified. No independent audit has been performed.
