---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

In the cubic model a repeated root requires u^5=2/3 and t=-5u^3/2, hence t^5=6. For each such t the repeated root is unique (u^3 and u^5 determine u), and N'' is nonzero there, so the normalized genus drops to four. Else the valuations -1, five +1's and -4 give seven tame total branch points, connectedness and genus five. The valuation checks at zero, infinity and the finite roots give the five regular differentials; their distinct monomials within two character spaces give independence. Cartier with exponent e=(11j'-j)/3 swaps the characters and extracts terms of exponent 11(q+1)-1. Replay python3 -B /workspace/checks/cartier.py enumerates trinomial words to recover the matrix and computes actual iterates by applying inverse Frobenius to each matrix action over F_11[t]/(t^5-2). It finds ranks [4,3,2,2,2,2,2,2,2,2], and the rooted tenfold map is idempotent, with Frobenius equal to the displayed P10. For all nonzero t the two blocks have rank two. The upper block selects the last two rows of the twisted lower block, whose determinant before twisting is -4t^3(t^5-2). Away from that zero, the two-step map is invertible on the two-dimensional character space and its transported two-dimensional image; thus stable rank is four, not just rank four at the first step. At t=0 the matrix vanishes. Frobenius on roots of t^5=2 and t^5=6 multiplies by 4 and 3 respectively, each of order five, giving both splitting counts. Fifth-root rescaling of u with a cube-root scaling of v proves the geometric isomorphism-orbit assertion.

## originality

PASS

Pass is for the marked nonzero-parameter stratification through the degree-five rank-drop locus and the resulting coefficient counts. The central superspecial fiber and the general Hasse–Witt/Cartier machinery are known; so is the type of character-space bound, which cannot determine a jump divisor.

## value

PASS

This is a motivated deformation of a known superspecial center preserving the seven-point cubic-cover structure. The a-number stays one on all nonzero genus-five fibers, while the stable Cartier rank drops on exactly one degree-five closed point. Locating that distinction and the excluded points gives a complete, arithmetic family invariant rather than a few finite-field examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
