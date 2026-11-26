# Independent mathematical audit

## correctness

PASS

The unit-trace four-mode Choi state's sixteen Pauli branches are orthonormal by maximal entanglement and Pauli trace orthogonality. Write U=VδG with G Gaussian up to phase and η=|sin(δ/2)|. The right factor transfers to the reference as R G^T R† in the paper's reference convention; parity and determinant equality survive transpose and parity-preserving conjugation. Output noise, even with unequal rates, commutes with this reference-side action. The Majorana-conjugation support and magnitudes in Allison–Coffman Eqs. (B30)–(B33) do not use the weights: in the canonical gate form, conjugation sends a Pauli label Q to a linear combination of Q and Q(ZZ), up to phases, with diagonal magnitude η and partner magnitude √(1−η²). The weighted blocks have squared Frobenius norm η²(u²+v²)+2uv(1−η²) and determinant modulus uv. These yield the asserted s± with full-state sector weights as in Eqs. (B22)–(B24). For the first two even blocks the products coincide; the first difference is greater or equal since ai≥bi, so it supplies the largest singular value including degeneracies. The two other even blocks contribute four b1b2 singular values. Each odd block type occurs twice and the largest cannot exceed the sum of the rest. The bound A≥|D| makes the concurrence nondecreasing in η by the derivative of the bracket or continuity at zeros. At η=1 the second block sum becomes a1b2+b1a2, giving the stated polynomial and product-noise boundary. The minimum total budget and asymmetry examples are for η=1, not for weak or Gaussian gates; only Choi-state convex-Gaussianity is tested. Replay: RESULT.md lines 63–149 and the formulas at lines 18–56, with the source block calculation. The frozen VERIFICATION.md and artifacts/verify.py were inspected but not executed; the finite phase/rate grid is corroboration, not the proof.

## originality

FAIL

The cited paper prints the final common-rate curve only, but its Appendix B already provides the same complete block pairing and the singular values as functions of the two arbitrary weights of each block. Replacing the product weights by their unequal-rate values and sorting the resulting singular values in the published concurrence prescription mechanically gives the frozen surface. This is verified stronger formula coverage, not a conclusion drawn from a matching symmetric threshold or a failed search.

## value

FAIL

Unequal noise budgets are physically meaningful and the closed formula is convenient. Nevertheless the precise state classification is a direct evaluation of the prior explicit generic spectrum, and the budget and fixed-mean comparisons require only the resulting bilinear inequality. The frozen record does not solve a nonmechanical remaining question, such as an independently justified channel-level criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
