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

The executable symbolic check is `checker.py` (Python with SymPy); `checker_output.txt` is its recorded output. It constructs the two variable-step BDF2 companion matrices directly from the difference formula, separately obtains the claimed trace and determinant, expands the complex Schur--Cohn difference as an exact polynomial identity, verifies the neutral root and limit formulas, and tests finite representative complex values. It reports 115 passing assertions.

The proof for all ratios and all points in the closed left half-plane is the exact factorization into positive expressions and the strict Schur--Cohn criterion. Finite numerical tests alone do not imply that theorem. No external review or independent scientific validation has been performed. The theorem is restricted to a constant scalar coefficient, exactly two-periodic positive step lengths, and the standard fully variable-coefficient BDF2 formula.
