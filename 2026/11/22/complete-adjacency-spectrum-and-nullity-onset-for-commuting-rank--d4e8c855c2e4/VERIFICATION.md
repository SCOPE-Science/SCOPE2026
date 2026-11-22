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

The proof is a uniform, exact calculation. `checker.py` is independent supporting code: it constructs each partial composition directly, tests equivalence with the forbidden-index criterion for distinct arrows, computes the complete adjacency matrix for \(n=3,4,5,6\), and uses SymPy's exact characteristic polynomial and rank. `checker_output.txt` records four successful exhaustive finite cases. Run `python3 checker.py` with SymPy installed. No numerical spectral approximation, probabilistic hypothesis or extrapolation from finite cases is used in the proof. General correctness rests on the linear algebra in `RESULT.md`. No independent audit or expert certification is claimed.
