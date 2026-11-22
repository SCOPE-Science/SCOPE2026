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

# Verification record

The proof derives finite-length coefficient identities directly from the residue-rank stratification and unit-coordinate lifting. Its critical independently checkable parts are: \(q^4\) zeros of the cubic modulo \(\pi\); exactly \(q^2\) rank-at-most-one points; smoothness of every rank-two zero; the quadratic recurrence; and the cubic recurrence.

Execute `python3 checks/check_hankel.py` from the package root. The standard-library program obtains coefficients from the rational function with exact `Fraction` arithmetic and compares them against direct exhaustive enumeration of all five-entry Hankel matrices. Its saved output appears in `checks/verification_output.txt`. The tested rings are \(\mathbb Z/2\), \(\mathbb Z/4\), \(\mathbb Z/8\), \(\mathbb Z/16\), \(\mathbb Z/3\), \(\mathbb Z/9\), \(\mathbb Z/5\), \(\mathbb F_2[t]/(t^2)\), \(\mathbb F_3[t]/(t^2)\), and \(\mathbb F_4[t]/(t^2)\); the last test exhausts \(16^5\) inputs.

The finite computations are not proofs for all \(m\) and \(q\). The symbolic recurrence, valid in every characteristic and ramification type, is the basis for the unbounded theorem. Originality remains qualified by potential unindexed literature and by the known topological counterpart. No external or independent audit was performed.
