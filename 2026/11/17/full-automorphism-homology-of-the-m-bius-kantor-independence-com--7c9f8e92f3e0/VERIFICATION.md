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
# Verification

Run `python verify_mobius_kantor.py` with Python 3, NetworkX and SymPy. The script constructs the graph and complex with no external data, and checks all signed simplicial identities, exact rational boundary ranks, graph automorphisms and the full two-generator group.

Degree-four homology characters are calculated independently modulo \(101\) and \(103\). Exact rational ranks and agreement of both modular ranks ensure that the one-dimensional top rational action is detected without an unverified characteristic assumption. The rational character in degree three follows by the signed Lefschetz identity; group character inner products establish an absolutely irreducible rational three-dimensional complement.

The captured exact output is `verification_output.txt` and ends with `COMPLETE_MOBIUS_KANTOR_AUTOMORPHISM_CHARACTER_PASS`. The thirteen class sizes sum to 96. No equivalence is asserted between the three ordinary quotient spaces and any actual spheres: only their graded rational cohomology rings have been calculated.

The computations constitute complete finite verifications for the explicitly specified graph and its 96 automorphisms, not infinite-family calculations, integral quotient computations, or independent external certification.
