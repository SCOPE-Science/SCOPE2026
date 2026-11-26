---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Both finite permutations preserve principal two-sided ideal classes: iterate first the inequality for the output around its cycles, then the inequality from the input to its image around the mapping cycles. The intervening powers force s^2 J s for every s when k>=2. Independently, write s=a s^2 b in S^1; iterating s=a s(sb) and s=(as)s b with idempotent powers of a and b gives s in s^2 S^1 and in S^1 s^2. Thus every positive power is H-equivalent to s, including an idempotent power, so s lies in a group. For even k, at most two residues are excluded at odd primes and only zero at 2; an exponent coprime to the exponent of each group induces a permutation even without commutativity. For E=1 the constraints are vacuous. In a Clifford semigroup the group-index map to the semilattice identifies each principal ideal with the fibers below its index, so both permutations preserve the fibers, and disjoint union gives the converse. For odd k the kth power is invertible on abelian 2-groups; the abelian Hall–Paige criterion applies there, while the CRT argument works on odd-order factors. The unique involution obstructs the remaining case by multiplying the mapping equations. The inspected verifier uses the exact finite definition (42 advertised table/exponent combinations and a separate k=1 contrast); it was not rerun and the universal decisions do not depend on it.

## originality

FAIL

Distinct catalogue records already cover the principal obstruction and every even-power equivalence, including the same power-map witness, as well as the odd abelian criterion and the group-fiber argument. The inverse-semigroup formulation follows by applying the first overlap to get Clifford and then the elementary group-fiber decomposition. This is a coverage decision, not a claim about authorship or publication priority.

## value

PASS

As a mathematical statement the all-even-power characterization addresses the natural finite-semigroup existence problem and cleanly separates semigroup obstructions from group existence. Its intrinsic value does not overcome duplicate coverage in the originality axis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
