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

# Mathematical verification

The included `verify.py` is a standalone Python 3 standard-library program and requires no repository dependencies. Run it with `python verify.py`. A successful full run prints `ALL_FIELD_BURNSIDE_CHECKS_PASSED`.

The program computes all preservation-of-operation permutations for the 4- and 9-element quandles and compares to the proposed ambient automorphism normal form. It exhaustively checks all nonempty subsets against actual multiplication in dimensions \((p,f)=(2,1),(3,1),(2,2)\). It directly constructs subquandle orbits under generators for prime-field cases \(p=2,3,5,7\) and compares coefficients with the independent affine-cycle-index calculation, itself checked for all primes \(2,3,5,7,11,13,17,19\). For extension degrees \((p,f)=(2,2),(3,2)\), it computes the full nested Burnside sum and independently obtains all ambient orbit coefficients by generator actions. It also explicitly verifies the \(6{,}144\) automorphisms over \(\mathbb F_2^2\).

The complete extension-field output totals are \(9\) and \(39\); the numbers of labeled nonempty subquandles are \(119\) and \(10{,}933\). Code is an exact finite checker; it cannot alone prove the theorem for all prime powers. That proof appears in RESULT.md. The independent mathematical audit status is not performed.
