---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The two Leibniz equations on distinct and equal basis elements are sufficient by bilinearity. The squares for different parts are linearly independent in pairs (each has a nonzero projection onto the other's part, where that other's square has zero projection), forcing block diagonality. In characteristic two the blocks are symmetric with the ones vector in the radical, even when the part size is zero in the field. In odd characteristic write the i-th block as alpha_i I plus an alternating matrix H_i, using equality of the diagonal entries within each part. The equation for neighboring parts is H_j 1 = (2 alpha_i - alpha_j) 1. Multiplication by 1^T and the unit size n_j imply alpha_j=2 alpha_i for all i!=j. For s=2 this forces both scalars to vanish since 3 is a unit; for s>=3 it also forces all scalars equal and then zero. The converse is immediate. Congruence with a basis starting at the ones vector, not an orthogonal splitting, gives arbitrary symmetric or alternating forms on m_i=n_i-1 coordinates, preserving rank. Counting by the radical gives the Gaussian factor, and division of GL(2j,q) by the symplectic group gives the nonsingular alternating factor. For symmetric forms one border of a nonsingular or corank-one block yields q^r(q-1) choices, whereas a larger radical cannot be repaired, giving the stated symmetric recursion and product. Normalizing by all forms and writing the Gaussian coefficient as a product yields the displayed finite masses. Their summable quadratic envelopes prove total variation including along fixed parity, and independent finite blocks give convergence of the sum to the convolution. The defect used is relative to sum m_i, so ambient corank is larger by s. Direct bounded replay built the full Leibniz system for K_{3,2}, enumerated the kernel over the prime field and row-reduced each derivation for rank: F_2 gave 1+4t+7t^2+4t^3, F_5 gave 1+4t^2. This checks two cases, not the extension-field or limit claims; the frozen verify.py was inspected but not executed. No result is inferred for the excluded odd cases.

## originality

FAIL

This is not a verbatim previous multipartite rank-polynomial statement, but the whole claimed census and limit are mechanically implied by Reis–Cadavid's general derivation criterion and Fulman–Goldstein's exact finite rank and stronger total-variation estimates for the two unrestricted matrix families. The remaining work is finding the twin classes, eliminating the scalar diagonals by the two-line unit-size argument, passing to the quotient by the ones vector, and taking independent products. No new corank law or rank-counting problem remains after these translations.

## value

FAIL

Ranks of derivations give a sensible additional invariant, and the contrasting parity is a useful illustration. Under precisely the hypotheses where no scalar-diagonal coupling survives, however, the exact facts claimed are just the independent product and convolution of established laws. A finite-field re-expression of those laws does not supply a distinct substantive result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
