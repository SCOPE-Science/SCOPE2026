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

The simple weighted Laplacian on the mean-zero space is injective in the conductances; the trace Hessians for x^(-1) and x^(-2) have strictly positive divided-difference coefficients, using f'' whenever eigenvalues coincide, so both objectives are strictly convex. Approaching disconnected support makes the inverse moment diverge. Uniqueness under dihedral symmetry forces two orbit weights; a zero weight on either entire orbit disconnects the sunlet. For each nonzero cycle mode the 2x2 block has trace a*lambda+2b and determinant a*b*lambda, so its inverse-square trace is (trace/det)^2−2/det. The zero mode contributes only (2b)^(-2); summing gives A/b^2+B/(ab)+C/a^2 by the csc^2 and csc^4 cycle identities. With t=a/b under n(a+b)=1, the derivative has the sign of the stated cubic, which has one positive zero by Descartes and the opposite endpoint signs. The first-order derivative gives t_1=sqrt(B/E) with E=n−1/2. At t_1, E times the cubic is B(n−1)t_1−Q with Q=2CE−B^2. Independently reproduced the positive cofactor of Q and the positive-coefficient certificate for EQ^2−B^3(n−1)^2 using exact SymPy arithmetic; replay python3 /workspace/frozen_review_arithmetic.py. This yields the strict sign for every n>=3, not just a numerical ordering. At t=s*n, the rescaled cubic tends to 2s^3+s^2/6−1/90 and positive-root bracketing gives t_2/n→c. The term n^2 C(1+1/t)^2 dominates F_2 at both designs. At t_1 the cross term 2n^2 C/t_1 gives (sqrt(6)/90)n^(11/2); every other correction is O(n^5), as are the optimal corrections at t_2. This proves the absolute regret and vanishing relative regret in the raw trace. The frozen RESULT.md, verification note and diagnostic script were read; the source script was not executed and finite tests cannot prove global or infinite-domain claims.

## originality

PASS

Available prior statements cover the underlying design framework, other spectral objectives on exactly this graph, and coherence/spectral formulas. They do not supply the fixed-budget order-two cubic optimizer, its strict mismatch with the first-order allocation at every size, or the resulting sharp cross-objective regret. The pendant exponent n^(-2) alone is not a distinctive sunlet design phenomenon: it also occurs under a different, checked spectral-gap objective. Acceptance concerns the actual squared-inverse trace optimum and comparison under the stated equal-cost assumptions, not a claim of physical equivalence across noise models or historical priority.

## value

PASS

For a standard cycle-with-leaves graph, the result resolves a genuine design question: the edge weights optimal for first-order coherence always overinvest in pendant conductance when assessed by the twice-inverted trace. The exact cubic permits design for any size, with unrestricted uniqueness and a strict all-size comparison rather than large-size advice alone. The comparison quantifies a divergent absolute penalty and a vanishing fractional penalty under the stated normalization; it does not claim a constant-factor loss.

The dated certificate retains the supplied scientific assessment, sources and limitations.
