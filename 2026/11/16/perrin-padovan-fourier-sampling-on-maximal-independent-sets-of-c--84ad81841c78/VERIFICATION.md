---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For all labelled C_n, n>=3, the circular 3-state 00/01/10 transfer has characteristic polynomial t^3-t-1 and trace P_n, the Perrin count. A return to state 01 over d steps is a_d, giving exact two-point counts a_d*a_(n-d); centering and diagonalizing the circulant covariance yields the stated complete Fourier eigenvalues. A 2,3 cyclic gap interchange forces every constant-on-sample linear statistic to have all equal coefficients for n=5 and n>=7; different maximal set cardinalities remove that last kernel for n>=8. The five small exceptional ranks and n=6 nonconstant k=1,5 nulls follow from exact small configurations. The renewal root expansion has rate rho=alpha^(-3/2), giving O(n*rho^n) error uniformly in grid frequency; its density simplifies to p*A*B/Q(cos(theta)), and the strictly convex Q puts maximum at the unique interior negative cosine and minimum at theta=0, yielding the sharp ratio 43.42455574592406... Independent exact rational moment/covariance ranks for n=3..12 match the recurrence and stated classification; these finite computations are not the proof for all n.

## originality

PASS

Best-of-knowledge: actual proof and cited primary/read indexed comparisons distinguish the specific result from older general tools and different objects; this is not a guarantee of priority.

## value

PASS

Uniform labelled maximal-independent-set sampling on cycles is a natural Perrin-combinatorial ensemble. Its full coordinate-Walsh identifiability threshold, exceptional null modes, and sharp nonalternating asymptotic conditioning quantify which harmonic statistics are recoverable, providing independently useful exact finite and asymptotic facts rather than only a rephrased Perrin count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
