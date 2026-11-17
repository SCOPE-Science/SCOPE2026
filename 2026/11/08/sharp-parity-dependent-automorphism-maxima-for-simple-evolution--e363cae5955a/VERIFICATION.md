---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Read the full proof and checking source. For invertible binary structure matrix, squares form a basis, so any algebra automorphism has monomial natural-basis columns; over F2 all nonzero scalars are 1, hence automorphism order equals binary directed graph permutation automorphisms. Simplicity corresponds to invertibility and strong connectivity. For even n, I+J is invertible over F2 and S_n-invariant. For odd n>=3, S_n invariance forces a diagonal/off-diagonal two-orbit matrix, which is singular whenever strongly connected. For odd n>=5, a subgroup H with order>(n-1)! would have index<n in S_n; its coset action has nontrivial normal kernel, necessarily A_n, whose 2-transitivity forces the prohibited two-orbit matrix. The hub-and-leaves B_n has determinant 1 in F2 for odd n and stabilizer S_{n-1}; n=3 attains 3 using a directed triangle and n=1 trivial. Independently recalculated binary ranks for full-symmetric even n<=8 and hub odd n<=9; source exhaustive enumeration only n<=4 and is not an all-n proof.

## originality

PASS

Full symmetric-group automorphism characterization and the general monomial theorem are previously known and credited. The surviving theorem combines the odd-dimensional strict small-index bound, odd hub attainment and n=3 exception to give exact maximum over all simple F2 algebras; inspected primary 2022 full-S_n paper and distinct 2026 complex maximum do not imply this F2 order formula. Best-of-knowledge only, with historical group-theory priority risk.

## value

PASS

Exact maximum group size and parity switch for simple binary evolution algebras is a natural representation/invariant problem, beyond the previously established feasibility of full S_n. The all-n sharp odd bound and point-stabilizer construction, plus the n=3 exceptional behavior, provide a reusable classification boundary; no broad general theorem or paper-sized contribution is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
