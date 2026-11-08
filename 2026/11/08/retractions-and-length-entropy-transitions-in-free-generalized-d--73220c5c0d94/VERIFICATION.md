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

# Reproduction and limits

Run `python3 CHECKER.py` with Python 3 and no third-party libraries. The script enumerates all allowed generator-image tuples for each indicated pair \((n,L)\), reconstructs their images using the binary algebra operations, directly tests idempotency, and groups idempotents by the number of fixed free generators. It separately calculates the closed rank-profile formula and asserts agreement. It additionally tests that identity substitution returns every enumerated element unchanged and checks the strict exponential sparsity inequality for ranks two through twenty.

Expected final line: `VERIFY_OK`. The recorded complete output is `CHECKER_OUTPUT.txt`. The seven checks comprise ranks one through four, image bounds one through four as indicated by their printed parameters. In particular, \(n=3,L=2\) involves exactly \(9261\) endomorphisms and yields \(58\) idempotents, while \(n=2,L=4\) involves \(28900\) and yields \(31\). The program does not enumerate every rank and length and does not verify analytic asymptotics: those are proved in `RESULT.md` by elementary inequalities, finite maximum comparison, and calculus.
