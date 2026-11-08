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

# Verification record

The included `verify.py` uses independent algebraic checks and a numerical diagnostic. It expands the squared pair distance from two independent uniform barycentric-coordinate vectors, evaluates all monomials by the exact Dirichlet factorial identity, and checks the three symbolic moment polynomials for orders two, four and six. It then checks the exact inverse equations, the Heron area formula, both isosceles endpoint expressions, and the noncongruent example with identical second and fourth moments.

The second verification route samples point pairs directly from eight coordinate-defined triangles, with 180,000 pairs per triangle, and compares the resulting moments to their exact expressions using seven empirical standard errors plus a small numerical tolerance. This sampling check neither establishes the identities for all triangles nor certifies the algebraic endpoint classification. The exact polynomial and geometric arguments are the mathematical proof.

The verifier was run successfully with output:

`PAIR_TRIANGLE_INVERSE_OK exact_polynomials=3 inverse=3 conditional_envelope=2 isosceles_pair=2 monte_carlo_shapes=8 samples_each=180000`

Reproduction: execute `python verify.py` with Python 3, NumPy and SymPy. No external files are needed. The accompanying `RESULT.md` gives the mathematical definitions, domains, boundary cases and independent symbolic proof.

Known limits: the archived 2013 distance-distribution manuscript could be inspected only partially in available online form. General moments from the 2017 Proposition 4 are expressly prior art. Numerical simulation is supportive only. Independent audit remains not performed.
