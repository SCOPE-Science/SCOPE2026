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

# Verification of sparse repunit semigroup formulas

The attached standalone `checker.py` uses exact Python integers and no external packages. Run `python3 checker.py` in a directory containing the script. Its printed output is recorded as `checker_output.txt`; the last line is `ALL CHECKS PASSED`. The script covers 18 cases: \(b=2\) through \(n=15\), \(b=3\) through \(n=11\), \(b=4\) through \(n=9\), and \(b=5\) through \(n=7\), with odd indices starting at three.

The code reconstructs the numerical semigroup's residue-shortest representatives by Dijkstra shortest paths over all residues modulo \(a=R_n\), independently from the proposed coin-cost representatives \(W(t)\). It compares the complete sorted Apéry sets, largest gap, Apéry-sum genus, and pseudo-Frobenius elements tested by generator additions. It also checks the predicted type and symmetric criterion.

The unlimited-parameter proof has separate necessary ingredients: a quotient/remainder optimal coin representation, strict positivity under coefficient wraps by \(a\), the exact terminal positions of the Apéry order, and comparison of its possible maxima using the three residue classes of odd indices modulo six. The verification code is supporting finite evidence, not a substitute for those arguments. No external independent audit is claimed.
