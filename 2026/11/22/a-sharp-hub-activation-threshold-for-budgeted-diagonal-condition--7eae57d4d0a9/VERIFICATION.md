---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For every feasible loading, positive definiteness follows from a>0. For fixed hub load, let the comparison matrix have the mean load on every leaf. Its extreme eigenvectors can be chosen in the hub/uniform-leaf space: the symmetric 2-by-2 quotient eigenvalues strictly straddle the repeated leaf diagonal (the quotient characteristic polynomial evaluated there is -m). Each such vector has exactly the same Rayleigh value on the original loading. The bottom eigenvector has a nonzero uniform leaf coordinate, so equality in the minimum Rayleigh bound forces every original leaf load to equal its mean, by the leaf equations. This proves strict improvement for every asymmetric loading, not just existence of a symmetric minimizer. Put D=m-1+B-(m+1)x and K=a(m+1)+2m+B. The quotient trace is (2K+(m-1)D)/(m+1); the derivative of (D²+4m)/trace² in D has the sign of 2KD-4m(m-1) throughout the feasible interval. This recovers the stated x_free and its one-sided clipping, with x_free>0. At x=B/m the zero of that derivative yields B²+[a(m+1)+3m-m²]B-am(m-1)(m+1)=0, with exactly one positive root. At equality the unique optimum still has zero hub load, and B=0 is a singleton. The exact example gives B_c=1 and, at B=2, loads (8/27,23/27,23/27). The proof relies on neither a grid nor an eigensolver. VERIFICATION.md and verify.py were inspected only; the frozen package's optional replay path is python3 verify.py from its directory.

## originality

PASS

No equivalently strong solution was identified in the inspected sources. The close four-site path result has the same additive budget and objective but not the star feasible spectral family; a star trace-inverse result has the same graph/budget but a different objective and a different support law. Generic spectral feasibility does not supply strict leaf equality, the minimizer, or the hub threshold. Historical priority remains provisional.

## value

PASS

The exact boundary answers when hub stabilization first pays off under a fixed additive budget. The explicit optimizer and strict dominance over asymmetric designs provide a useful check of numerical diagonal-loading solvers and cannot be replaced by generic SDP solvability. This is a unit-star theorem only; it makes no claim for weighted stars, general graphs, or other objectives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
