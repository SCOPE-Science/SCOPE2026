---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The Leibniz derivation recursion is forced by D(e_1)=sum a_j e_j, giving diagonal (i a_1) and fixed upper-triangular bands. D^p=D implies a_1^p=a_1, hence a_1∈F_p; if a_1=0, D nilpotent and D=D^(p^j) forces zero. Otherwise the separable polynomial t^p−t yields a diagonalizable D and spectral projector I−(D−cI)^(p−1). Applied to e_1 it gives a c-eigenvector with first coefficient 1, whose iterated brackets form a generator basis. The resulting algebra automorphism conjugates D to cH. The quotient eigenvalue c is invariant. Automorphisms arise from generators with nonzero e_1 coefficient, and commuting generators have possible nonzero coefficients only in indices 1 mod p; this gives stabilizer (q−1)q^floor((n−1)/p) and orbit size q^(n−1−floor((n−1)/p)). Rank and odd-characteristic idempotent boundary follow from diagonal. Independently exhaustively enumerated all linear maps n=2,3,4 at q=2 and n=2,3 at q=3; these are corroborations, not infinite proof.

## originality

PASS

The classical formulas for automorphisms and toral gradings of NF_n are prior knowledge; the final claim does not reassert a new grading classification. The exact characteristic-p composition-power equation, rational conjugacy classes over every field and finite-q population/stabilizer formulas were not established in the inspected characteristic-zero grading literature. A previously published finite-field n=3 derivation-conjugacy classification may imply its n=3 special case, which is not a separate novelty claim; the all-n p-toral stratum remains a qualified best-of-knowledge addition.

## value

PASS

This natural restricted-toral equation is the positive-characteristic analogue of semisimple derivations. Its complete all-dimension orbit/rank and exact finite-field population classification, including a sharp characteristic-two idempotence jump, is an intrinsically useful algebraic invariant rather than a renamed generic grading observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
