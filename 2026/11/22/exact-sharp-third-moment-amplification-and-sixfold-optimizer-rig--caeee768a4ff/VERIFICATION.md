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

# Verification and limitations

The Fourier and generalized-eigenvalue proof is written in `RESULT.md`. Running `python checker.py` in a Python environment with SymPy produced: PASS 16020 assertions; root z*=0.417702187780093, sharp coefficient K6=2.366495837333408, and squared coefficient 5.600302548116345. Assertions cover exact elimination identities and root brackets, 4,000 deterministic direct six-site Fourier evaluations (four checks per sample), and twelve signed, shifted equality profiles. Numerical checks are not a proof for all signals; the universal result rests on the symbolic polynomial, Descartes' rule and Rayleigh reduction. The available full-text literature check covers Chen–Lam–Lu Section 6.1 and the six-cycle example; Xie–Zhang was compared from its public abstract and the later paper's cited descriptions. An older equivalent claim might remain unindexed. Independent audit has not been performed.
