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

# Reproducible verification

The attached script `verify_joint.py` implements the \(2\times2\) matrix Lie bracket in coordinates \((a,b,c)\) representing \(\begin{psmallmatrix}a&b\\c&-a\end{psmallmatrix}\), and verifies every prescribed pair of adjacent Engel outputs. Field arithmetic is implemented directly for the prime fields of orders \(3,5,7\) and the quadratic extension of order \(9\).

Run `python verify_joint.py` with a standard Python 3 interpreter in the extracted package directory. The expected exact standard output is `verify_joint_output.txt`. It checks respectively \(729\), \(15625\), \(117649\), and \(531441\) distinct output pairs against the closed formula, and also checks total mass and support cardinality. A self-contained algebraic proof establishes the all-odd-prime-power theorem independently of these finite tests.

No formal external proof-assistant validation or independent mathematical audit has been performed. The checks do not test characteristic two.
