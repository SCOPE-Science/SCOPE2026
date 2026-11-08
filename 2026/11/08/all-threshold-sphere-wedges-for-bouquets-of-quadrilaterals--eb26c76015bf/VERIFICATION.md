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
Run `python3 verify.py` with Python 3.9 or later; no third-party packages are required. The supplied `verify_output.txt` is the actual captured output of the included checker.

For every integer parameter pair \(1\le m\le6\), \(2\le k\le6\), the checker independently derives each induced independence number by graph-vertex dynamic programming; generates the entire face set; applies the prescribed matching; checks the critical zero-cell and every expected critical \((2k-3)\)-cell; and topologically sorts all oriented Hasse incidences to prove acyclicity in that finite complex. For \(m\le3\) and \(k\le5\), it also directly tests each vertex subset against independent \(k\)-subsets. The final line is `ALL_VERIFY_OK 30 parameter pairs; complete face-poset acyclicity`.

Representative output: \((m,k)=(5,4)\) has 3,201 nonempty faces, 1,595 matched pairs and ten critical five-cells; \((m,k)=(6,6)\) has 99,747 nonempty faces, 49,870 matched pairs and six critical nine-cells. The checker is finite; its success is not an exhaustive proof for unbounded parameters. The symbolic face formulas and all-parameter directed-acyclicity argument are in `RESULT.md`. No independent mathematical audit has been performed.
