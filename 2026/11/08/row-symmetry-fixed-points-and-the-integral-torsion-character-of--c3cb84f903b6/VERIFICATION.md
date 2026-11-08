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
# Reproducibility and limits

`verify.py` contains three standalone computations. The first enumerates all faces of the ordinary five-by-five chessboard complex, constructs its signed integral boundary matrices reduced modulo three, checks the chain-complex identity, finds a non-boundary cycle in degree two, and verifies the signs induced by selected row and column transpositions. It finds face numbers `(25, 200, 600, 600, 120)`, differential ranks 176 and 423 in the relevant degrees, and one-dimensional degree-two homology over the field with three elements.

The second calculation independently generates all faces of the fixed-point chessboard complexes for `m=5,6,7` and `k=0,1,2`, computes exact reduced mod-two homology by bitset elimination, and compares with the formulas from the proof. The nine homology checks pass. The third calculation builds the two-family modular quotient presentation in the 2026 source for each `m=5,6,7,8,9`, verifies that the chosen order-three-class representative survives mod three, and confirms the relations giving the row-swap and column-swap negative signs. These last computations test the finite presentations as algebraic consequences of the source, not as substitutes for its integral classification.

Run in a Python environment with NumPy available: `python -m pip install -r requirements.txt` and `python verify.py`. The observed stdout is included in `verify_output.txt`. No network or external data is required for these checks.

These finite computations do not prove the infinite-family theorem or the integral uniqueness of torsion; those are established by the cited integral presentation, its explicit natural symmetry action, and the shellability/face-count argument. No independent audit was performed.
