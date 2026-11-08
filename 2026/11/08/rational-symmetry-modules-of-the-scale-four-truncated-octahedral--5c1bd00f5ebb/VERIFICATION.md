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

The standalone `verify.py` requires only Python 3 standard-library modules. From this directory run `python3 verify.py`; the bundled `verification_output.txt` records the resulting data and terminates in `ALL_CHECKS_PASS`.

The verifier independently rebuilds all graph distances from adjacent-position swaps and enumerates every allowed face. The augmented matching pairs \(8,682\) lower/upper cells and leaves six critical four-cells and three critical five-cells; a complete directed Hasse-graph topological sort checks acyclicity. Exact integer gradient projection and lift recover the primitive boundary vector \((0,1,1,0,-1,1)\) on the third critical five-cell. The chain maps and their orientation signs are composed with all \(48\) symmetries, and ten conjugacy-type character pairs are independently cross-checked by signed fixed-face sums over all simplices. Direct action on the two degree-five cycles confirms that character separately.

The character decomposition uses the standard rational irreducible character table of \(S_4\). The comparison literature already supplies the nonequivariant homotopy type, not the new equivariant module. This is an exact computation for one finite graph and one metric threshold, not a theorem for all Archimedean polyhedra; integral group-ring lattice classification, equivariant homotopy and integral quotient homology remain unproved.
