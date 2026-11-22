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

# Verification
The bundled `verify.py` performs exact arithmetic, without external dependencies, for every prime from \(5\) through \(211\): it forms the coefficient-normalized Hasse polynomial by independent integer multinomial expansion, constructs the proposed truncated hypergeometric \(Q_p\), checks the identity modulo \(p\), checks \(\gcd(Q_p,Q_p')=1\), and checks \(\gcd(Q_p,\lambda^4-1)=1\). The expected success line is `DWORK_HASSE_SQUAREFREE_FAMILY_EXACT_FINITE_CHECK_VERIFIED`. The bound is just a finite verification domain. The all-prime claim is supported by the symbolic proof in `RESULT.md` rather than by extrapolating these checks. Independent audit has not been performed.
