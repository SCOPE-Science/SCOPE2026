# Failed attempt

Date: 2026-09-30

The published claim did not satisfy the acceptance rule requiring PASS on correctness, originality, and value.

Final claim: For two-qubit Werner states, under rank-1 qubit projective measurements in the stated Collins-Gisin normalization, the I3322 critical visibility is exactly 4/5, with maximal value -1+5v/4, so this restricted I3322 test is weaker than CHSH on the Werner line.

Non-passing axes: originality, value.

Correctness: PASS. The optimization in RESULT.md was reconstructed. Eliminating Bob's Bloch vectors reduces the pure singlet part to a one-variable bound whose maximum is 5 at the stated planar configuration; an independent dense numerical check peaks at t approximately sqrt(3), and the exact identity in the package proves the bound. The affine Werner-state expression then gives threshold 4/5. The scope restriction to rank-1 qubit projectors is essential.

Originality: FAIL. The core optimizer is already covered by Vidick and Wehner: their Theorem 1 proves that the maximally entangled state in every finite dimension has I3322 value at most 1/4, and notes that a single EPR pair attains 1/4. A rank-1 qubit projective strategy is a special case. For the Werner mixture in this normalization, the maximally mixed contribution is fixed, so the stated affine formula and visibility 4/5 are an immediate corollary rather than a new theorem.

Value: FAIL. Although the exact proof is correct and compact, the final claim is a direct restricted corollary of a stronger published optimizer theorem. Re-proving that special case does not meet the value bar for a new mathematical finding.

The original scientific files and evidence must be preserved with this failed package. No disclaimer converts a covered, low-value, or unresolved claim into a passing result.
