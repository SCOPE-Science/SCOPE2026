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

Use `python3 verify.py` in the directory containing the embedded artifacts (standard library only) and `python3 verify_modules.py` in the same directory (requires SymPy). Both scripts construct the periodized honeycomb graph directly and use exact integer arithmetic.

The graph verifier exhaustively enumerates every simple six-cycle, verifies that the finite quotient has exactly the \(L^2\) facial cycles, reconstructs all simplices through dimension three of \(\operatorname{VR}_{\le2}(H_L)\), and checks the independent face classification for periods \(5,6,7\). The module verifier independently acts on each oriented relative black/white face triangle and compares every image of every integral homology basis element with the theoretical formula. The latter computes the exact integral Smith normal form of the matrix whose blocks are \(g-I\) for three generators at periods \(5,6,7,8\). See `verification_output.txt` for the exact recorded standard output.

For all periods the logical proof is the relative long exact sequence for \((K_L,Y)\), the one-relation cellular boundary for the torus, the signed action formula, and the integral group-generator presentation. The finite enumerations are corroboration, not an infinite proof, and have not been independently mathematically audited. These coinvariants are algebraic; integral homology of the orbit space is not asserted.
