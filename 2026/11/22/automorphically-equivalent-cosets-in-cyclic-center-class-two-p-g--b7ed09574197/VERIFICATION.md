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

Conjugation on the order-p derived group is trivial by coprime orders, and [x^p,y]=1. The pairing on G/Z is nondegenerate alternating, so |G|=p^(2n+k). The pth-power map modulo Z^p is linear because the commutator correction in the pth power vanishes for odd p. Its kernel consists precisely of the classes with order-p lifts (except the zero class can lift to identity), and its complement has order p^(k+1) lifts. The symplectic lift presentations follow by correcting powers in Z^p; the displayed bilinear and carry terms are genuine cocycles and give the specified center and commutator, hence realize both types. Noncentral G' cosets are conjugacy classes; the indicated center-unit automorphisms realize the central external G' cosets. A larger central N changes the order of y_1 in an external coset. Noncentral N must contain Z by the central/noncentral obstruction; a subspace in the central quotient other than ker(lambda) admits an external coset with distinct orders, and no subspace works when lambda is zero. Finally for any generator-order g outside Omega_k, c'=g^p generates Z and [g,y_1]=(c')^(p^(k-1)). In the complementary plane decomposition take the symplectic basis normalized using the commutator generator (c')^(p^(k-1)), i.e. rescale the original pairing by the inverse of the nonzero value lambda(gZ). This makes the lifted generating frame satisfy the same presentation and proves transitivity. The checker.py was inspected, not executed; it enumerates the two order-81, rank-one examples and does not prove the unbounded-rank statement.

## originality

PASS

The novelty assessed is the full two-exponent classification of qualifying proper nontrivial normal subgroups for k>=2, not the definition, the order obstruction by itself, or the extraspecial k=1 orbit theorems. No compared source establishes that classification. The distinct sufficiency work is the central lift and generator-order orbit in this class.

## value

PASS

Resolves the motivating coset question for an unbounded-rank nonabelian class. The answer gives the exact subgroup list, not just necessary orders, with a sharp exponent-controlled appearance of a characteristic maximal subgroup. The higher-center case is not just a smaller or renamed extraspecial instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
