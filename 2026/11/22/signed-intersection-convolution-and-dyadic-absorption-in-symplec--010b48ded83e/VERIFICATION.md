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

# Verification notes

Run the embedded `check_symplectic.py` with Python 3 using `python check_symplectic.py`. No external packages are required. The accompanying `check_output.txt` records an actual completed replay. The checker constructs every admissible-domain and admissible-image partial injection by choosing signed subsets and all bijections between them. For the rank-pair experiments, it computes each ordered product directly and checks each resulting individual fiber, not merely a rank histogram. For maximal proper-rank iterates it checks exact rank distributions through lengths \(6\) at \(n=1\), \(5\) at \(n=2\), and \(4\) at \(n=3\). For the all-arity theorem it checks all \(27\) three-factor rank profiles when \(n=2\) and three mixed three-factor profiles when \(n=3\). No floating-point probability is used.

The exhaustive computations cover only those finite cases. They do not independently establish all dimensions or long-time asymptotics; these follow from the proof in RESULT.md. Historical uniqueness and independent mathematical audit are not certified by the checker.
