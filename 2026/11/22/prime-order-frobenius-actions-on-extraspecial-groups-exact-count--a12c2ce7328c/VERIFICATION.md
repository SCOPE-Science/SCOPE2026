---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The central multiplier of an exact prime-order fixed-point-free automorphism is nontrivial and has order ℓ, so ℓ divides p−1, and for p=2 the center already obstructs freeness. For odd p of exponent p² the p-th power map induces a nonzero linear functional λ on the quotient V: well-definedness uses the central order p, and linearity uses the class-two power formula and p|binom(p,2). Write λ(v)=ω(u,v). Equivariance λ(Mv)=μλ(v) and the similitude identity yield M⁻¹u=u. For μ=1 the center is fixed; otherwise in the fibre over u there is exactly one central correction to make a fixed element since μ−1 is invertible. This works without an order hypothesis. For exponent p, the alternating Heisenberg coordinates (with 1/2) give maps (Mv,μz+τ(v)), where τ is any linear functional; for μ≠1 the same fibre argument equates freeness with the absence of a fixed quotient vector. Since ℓ|p−1, M of order dividing ℓ is split semisimple, and ω pairs the μ^i and μ^(1−i) spaces perfectly. The absent i=0 forces absent i=1. The sole self-pair is symplectic of dimension 2b; the other m=(ℓ−3)/2 indexed pairs have equal dimensions a_j on each side. Every tuple is realized by assigning scalars to a symplectic direct sum of standard blocks. Matching symplectic bases and dual bases proves transitivity for a fixed tuple; the stabilizer is Sp(2b,p) times the product of GL(a_j,p), since maps on paired eigenspaces must be contragredient. Thus its Sp-orbit size is the stated symplectic group order quotient. Conjugating by a central shear changes τ by s(M−μI); absence of i=1 makes this an invertible operation on V*, so all p^(2n) lifts are conjugate to the shift-free lift of exact order ℓ. The quotient multiplier and indexed dimensions are invariant even under full automorphism conjugacy, so no classes merge. Stars and bars and the ℓ−1 possible multipliers give the claimed class count; summing sizes gives the automorphism count and both reductions. The ordered norm identity follows by writing g=h⁻¹α(h), since this map of h is injective for a fixed-point-free automorphism of a finite group. Primality makes all nonidentity powers of the chosen generator fixed-point-free. Independent replay `python3 /workspace/review_calculations/small_cases.py extraspecial` uses the Cayley–Hamilton remainder to test order for all rank-one quotient matrices, separating scalar matrices, and reproduces 0,2,532,2,10446 and the corresponding quotient stratum sizes. The lift counts and all-rank statement rely on the group proof, not this rank-one calculation.

## originality

PASS

Accept the exact-order fixed-point-free census and conjugacy spectrum on extraspecial groups, with the exponent-type exclusion, not the underlying automorphism normal forms or symplectic centralizers. An exact-order restriction of an all-orders Heisenberg count is not a parameter substitution. Classical split symplectic conjugacy applies to the quotient after scalar normalization, so the orbit factor alone is not independently original. The exact extraspecial strata require the fixed-point reduction, forbidden eigenvalues, full central-lift conjugacy/order test, and the exponent-type comparison. No checked same-object theorem covers that group-level result.

## value

PASS

The two extraspecial types and the specified generator of a cyclic prime-order Frobenius complement define a natural uniform classification question. The exponent-type obstruction rules out a whole group family even at other orders, while the closed mass and class-size formulas give every conjugacy stratum for the admissible type in all ranks. An all-orders or existence statement does not tell researchers which exact orders and oriented actions are realized or how many maps occur. The result does not claim to count unmarked semidirect products.

The dated certificate retains the supplied scientific assessment, sources and limitations.
