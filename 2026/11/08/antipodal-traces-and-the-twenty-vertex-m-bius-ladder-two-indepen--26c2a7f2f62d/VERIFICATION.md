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

# Verification scope

The graph is the \(20\)-vertex Möbius ladder with cycle edges and ten antipodal rungs. Run `python3 verify.py` beside `verification_output.txt` in a Python 3.9+ environment with no extra packages. The executable independently builds all faces by both an induced-degree filter and a sixty-forbidden-triple filter, then confirms identical faces, exact matching pairs and complete reversed-incidence acyclicity. An acyclic matching with one critical vertex and twenty-three critical seven-cells proves the integral homotopy classification by discrete Morse theory.

The verified output includes `FACES nonempty=53670`, `MORSE matched_pairs=26823`, `ACYCLIC covering_relations=335460 visited=53670`, and `H7 rank=23 involution_trace=-1 rational_plus=11 rational_minus=12`, followed by `ALL_MOBIUS_DISSOCIATION_CHECKS_PASS`. The verifier is deterministic: its pivot order is explicitly embedded in the source and reported in `RESULT.md`.

The formula for the reduced antipodal Lefschetz number at every length is proved symbolically in `RESULT.md` using fixed antipodal pairs and cycle independence polynomials. The program verifies its length-ten specialization from the complete face list, but this finite check is not represented as an infinite proof. The result is a homotopy equivalence, not a simplicial homeomorphism or an equivariant homotopy equivalence. There is no claim of independent external validation.
