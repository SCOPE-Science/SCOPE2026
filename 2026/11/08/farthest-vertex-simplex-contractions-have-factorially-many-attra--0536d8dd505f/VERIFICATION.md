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
# Reproducibility checks and limits

Run `python3 check_simplex_greedy.py` with Python 3, using only the standard library. The program compares rational periodic candidates and their exact return iterates for \(3\le N\le7\), tests \(\lambda=1/4,1/2,2/3,4/5\), examines regular and tied initial configurations, and checks post-transient rank rotation with an explicit uniform time bound. The recorded execution passed **15,580 exact-rational assertions**.

The argument for all \(N\ge4\) and every real \(0<\lambda<1\) is the sorted-map contraction and separation proof in `RESULT.md`, rather than a finite computation. The code checks special rational parameter values and finitely many initial points only; it does not independently establish exhaustive dynamics or publication priority. It carries no independent audit status.
