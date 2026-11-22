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

The uniform result is proved by the three steps in `RESULT.md`: the clique-exhaustion argument, a stabilizer-compatible equivariant nerve equivalence, and the relative collapse of one triangle quotient chamber. The proof requires no computer enumeration for large parameters.

The standalone finite sanity script (a reproducibility check, not an independent mathematical audit) is `verify_critical_dihedral.py`. Run `python3 verify_critical_dihedral.py` with Python 3 and no third-party dependencies. It enumerates all cliques for \(m=2,3,4,5\) and compares them exactly with the proposed decomposition. It then constructs the ordered-chain barycentric subdivision of each complex, takes genuine dihedral orbits of those cells, and checks the resulting boundary-map ranks over \(\mathbb F_2\) and \(\mathbb F_3\). This avoids falsely treating orientation-reversing unsubdivided simplex orbits as ordinary simplices. The expected final message is `FIRST_CRITICAL_DIHEDRAL_CHAIN_CHECKS_OK`.

These calculations confirm only the four stated finite cases and two finite coefficient fields. They do not rule out higher-parameter counterexamples or torsion at other primes. The general proof, not the finite output, establishes contractibility for all \(m\ge2\). No external or independent validation has been performed.
