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

# Reproducible checks

Run `python3 verify.py` with Python 3 and the standard library. The program exhaustively checks every support on complete Cartesian grids with \(1\leq p,q\leq4\), comparing the literal trace definition to the bipartite star-forest criterion. It independently computes the labeled-component recurrence and the closed formula \(\Phi_{2,q}(z)=(1+2z)^q+qz^2\), and it computes the defining Littlestone minimax recursion for ten smaller shapes.

The completed run ended with:

`CARTESIAN_RECTANGLES_PASS 74954 supports 10 online_ranks`

The verifier tests 74,954 supports, including all 65,536 supports of a four-by-four grid, and ten online dimensions. The full captured stdout is in `checker_output.txt`. The proof in `RESULT.md` is all-parameter; these finite checks are diagnostic, not a substitute for that proof.

All source comparisons remain bibliographically bounded. No external independent audit or expert certification is represented by these checks.
