---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For r>=2 and n>=r+2, Ind_r(C_n) forbids precisely subsets containing a cyclic run of r+1 occupied vertices; Deshpande–Singh Theorem4.6 supplies one reduced-homology degree q with rank r+1 if r+2 divides n and rank1 otherwise. The signed augmented Lefschetz sum over permutation-invariant occupied vertex orbits, cyclic run automaton, and folded reflection run-cap generating function give the stated complete rational dihedral trace formulas, including n=r+2 endpoint and the two reflection axis types. A fresh independent orbit enumerator reproduced 548 cases for r=2..5 and modest n; more decisively, an entirely separate derivation from published N(n,k) character formulas and equivariant Alexander duality agreed EXACTLY on 79,380 r,n,g samples. The infinity claim rests on the general orbit/automaton proof, not the finite checks.

## originality

FAIL

Decisively COVERED despite correct proof: the complete claimed character is already a formal corollary of a 2014 PRIMARY theorem for the full D_n action on the circular-arc nerve complex. Exact equality of the Alexander dual complex N(n,n-r-2) and standard sign-twisted equivariant Alexander duality transfer the 2014 Proposition7.2/7.3 representations to Ind_r(C_n) for ALL n,r, not just a few parameters. The new direct run-automaton derivation is another proof of an existing representation, not a new statement. This is not an inaccessible-source issue.

## value

FAIL

This is a natural complete dihedral invariant and the direct cyclic-run proof is mathematically correct, but as a NEW research finding it only recomputes the full character already determined in the 2014 circular-arc nerve representation table via a standard exact Alexander-duality/sign transfer. No independent new invariant, unknown classification or structural consequence survives comparison; it is an alternative presentation of a known result, not a new valuable contribution under the value criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
