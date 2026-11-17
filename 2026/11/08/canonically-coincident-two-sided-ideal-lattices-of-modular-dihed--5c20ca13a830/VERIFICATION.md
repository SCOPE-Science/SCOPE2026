---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Write A_e=R⊕Rw with R=k[r]/(r^m−1), char k=2, z=r^{m/2}, w a=bar(a)w and w²=z^e (e=0 dihedral,1 quaternion). Left and right r actions have the same coefficients in both algebras, while L_w and R_w differ only in first-coordinate terms ((1+z)bar b,0) and ((1+z)b,0). For any two-sided ideal I, L_r+R_r applied to (a,b) gives (0,(r+r^{−1})b); since (1+z)=(r+r^{−1})r(r+1)^{m/2−2}, I contains (0,(1+z)b), and applying w to it on left and right yields both difference terms. Therefore stability for both left/right generators in A_e implies stability in A_{1−e}, symmetrically. This works for every characteristic-two field and m=2^h≥4. The basis map is coefficient identity, hence Hamming supports and subspace lattice structure match, without asserting algebra homomorphism. Independently multiplied polynomials modulo r^m−1 over F2 for m=4,8,16,32 and verified divisibility identity. Source checker was read; its m=4, F2 ideal counts are corroboration, not proof for arbitrary fields.

## originality

PASS

Best-of-knowledge narrow theorem is equality of all two-sided ideal SUBSPACES under an explicitly fixed coefficient identification for every char-two field, yielding Hamming-isometric group codes. Published older dihedral coding work largely catalogs left ideals; earlier dihedral/quaternion comparison proves many shared abstract ring-theoretic properties and nonisomorphism but its accessible abstract does not explicitly state canonical equality of all two-sided ideal subspaces. This is a qualified PASS, not a claim that the inaccessible 2021 article lacks an equivalent theorem.

## value

PASS

Canonical equality of full two-sided ideal lattices despite nonisomorphic group algebras and different left-ideal spectra is a natural structural invariant and a meaningful counterpoint to algebraic distinguishability. The explicit char-two generator relation proves all-field, all-2-power-order equivalence and yields entire corresponding two-sided code Hamming weight enumerators, not just an arbitrary small example. This is substantive mathematical motivation before computation; the F2 order-eight census illustrates rather than supplies the theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
