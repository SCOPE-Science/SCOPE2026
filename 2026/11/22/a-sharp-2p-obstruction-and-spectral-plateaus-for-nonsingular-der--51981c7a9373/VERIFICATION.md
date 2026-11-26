---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Substituting arbitrary generator images via the derivation rule extends uniquely and preserves the ideal of lengths greater than c. The length filtration is triangular; fixed degree-one matrix A has q^{2(N_c−2)} lifts, all with the same invertibility. Over an algebraic closure triangularize A and filter each degree by the count of its second basis vector: off-diagonal substitutions move that count in only one direction, whereas the multidegree (i,j) diagonal acts by iλ+jν. This closes the nonsemisimple case without assuming both basis vectors are eigenvectors. Every mixed multidegree is nonzero in every characteristic: (ad x)^{i−1}(ad y)^{j−1}[x,y] has coefficient (−1)^{j−1} on x^i y^j in the tensor algebra. Pure degrees above one vanish by alternation. Thus (p,p) is an unavoidable zero weight from class 2p, and below it the only mixed obstructions for invertible A are the stated slopes, closed under inversion. For irreducible roots λ,λ^q, a ratio in F_p would equal its own reciprocal; equality to 1 is impossible and equality to −1 is trace zero, already forbidden by degree two. The irreducible trace-zero polynomials are counted by the trace-zero subspace of F_{q²}: q−1 non-base-field elements for odd p and zero for p=2, divided by 2. For trace t, determinant d, counting off-diagonal pairs via bc=a(t−a)−d independently yields q(q−1+r) matrices, where r is the number of distinct F_q roots of X²−tX+d; r=0,2,1 gives exactly the irreducible, split and repeated sizes, respectively. The split allowed ordered-pair count is (q−1)(q−2−e+δ) and the repeated count contributes only if 1 is not forbidden. For c≥p every nonzero prime-subfield slope already occurs using i=1. The Witt dimension and lift factor then give the normalized plateau. Independent trace/determinant replay over p=2,3,5,7,11 through class 2p, testing ij t²+(i−j)²d for every mixed weight, reproduced the prime-field boundary cases, positivity, plateau and vanishing.

## originality

PASS

The class-two boundary is already covered by an exact Heisenberg derivation table, and generator-image parametrization and multigrading are known. The frozen higher-class result couples a modular weight cutoff with an all-field matrix census. The inspected structural results do not implement that count, supply the all-class criterion, or yield it by an existing explicit specialization. This is a bounded literature judgment, not historical-priority certification.

## value

PASS

Nonsingularity is a natural test on the full derivation space of free nilpotent Lie algebras. Beyond the already covered class-two case, the count diagnoses exactly when a free multidegree forces failure, how prime-subfield slopes remove split choices, and why the density stays positive and constant across a whole class interval before becoming zero. The family is unbounded in fields and classes and the mechanism is not numerical enumeration or arbitrary slicing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
