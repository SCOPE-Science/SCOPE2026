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

# Reproduction of finite checks

Run `python verify.py` with Python 3, NumPy and SciPy. It builds full adjacency Hamiltonians for seven explicitly identified regular bases, compares full-state original-layer probabilities with quotient probabilities at three independent times, verifies the reduced characteristic polynomial, and checks residue signs, zero-sum identities, spectral upper bounds and approach of the scaled bound at larger sizes. The program reports 33 passed cases and a maximum discrepancy of approximately \(4.44\times10^{-16}\).

These tests are nonexhaustive; the algebraic proof in `RESULT.md` establishes the uniform-in-time limit for the entire infinite family. The classical layer equations admit exact elementary integration and their quantitative error bound is proved directly. No independent scientific audit is claimed.
