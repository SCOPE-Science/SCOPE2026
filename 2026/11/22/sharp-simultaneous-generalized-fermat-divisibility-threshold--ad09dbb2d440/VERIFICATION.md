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

The symbolic proof checks the exact factorization at the attaining coefficient and examines all low residues of the orbit modulo \(b^d+1\). The reduction is exhaustive because \(b^d\equiv-1\) and the coefficient bound is strictly below twice the larger modulus. The excluded high-representative branch and the three smaller branches each receive a separate inequality or congruence contradiction. No machine output is used to close an unproved infinite step.

The bundled `verify.py` computes the complete coefficient residue orbit over all \(2d\) exponent classes for 300 families (even bases \(2\)–\(20\), exponent pairs up to \(d=60\)) using integer modular inverses. It also directly brute-forces all smaller coefficients for a finite selection of small parameter cases. The test has no external dependencies. These finite experiments corroborate but cannot certify the infinite theorem or publication priority.

The theorem applies to arbitrary integers satisfying the stated congruences, not necessarily Carmichael numbers. A complete independent mathematical review and priority verification have not been performed.
