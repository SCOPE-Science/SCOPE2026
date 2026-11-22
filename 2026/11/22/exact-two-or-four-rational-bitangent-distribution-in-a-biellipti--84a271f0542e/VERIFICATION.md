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

The exact bitangent equations and elliptic-fibre proof appear in `RESULT.md`. Running `python3 verify.py --csv examples.csv` from these files reproduces the supplied CSV, compares independently generated affine bitangent lines against the polynomial radical tower over all prime fields from \(5\) to \(101\), and confirms the coefficient-frequency identities in every tested \(q\equiv2\pmod3\) prime field. The proof, not the finite checks, establishes the assertion for all permitted prime powers.

The isolated discriminant and resultant identities are \(\operatorname{disc}_z(Q_r)=-6912(r^2-4)^2\) and \(\operatorname{Res}_z(Q_r,9z^2-1)=-144(r^2-4)\). All arithmetic inverses appearing in the checker are taken only at nonzero residues.

The scientific overlap assessment is documented separately. Independent audit and independent validation have not been performed.
