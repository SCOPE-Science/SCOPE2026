---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

With the specified unscaled atoms, Parseval on the entire modulation basis, followed by summing over heat-window centers, gives S=diag(exp(-2tL)_{vv}). Degree distinguishes the two vertex orbits (13k-1 and 12k-1); clique permutations give transitivity within each group. The orthogonal decomposition into constants, component-constant contrasts within A and B, within-clique zero sums in A and B, and the A/B contrast has Laplacian eigenvalues 0,8k,10k,13k,12k,18k with multiplicities 1,1,3,10k-2,8k-4,1. The within-group contrast weights are their ranks divided by group sizes; the final contrast has weights (8k)/(10k*18k) and (10k)/(8k*18k). This gives both heat diagonals and all optimal bounds in the stated squared-norm inequality. Both diagonals are one at t=0 and strictly positive at all finite times. Subtraction yields x^8(1-x)Q_k(x)/(40k) at x=exp(-2kt); the stated substitution y=x/(1-x) and multiplication by (1+y)^9 give the displayed polynomial. At k=1 the coefficients through y^5 are positive, and from y^6 onward negative. At k>=2 the coefficients from y^5 onward are negative and only the preceding y^4 coefficient can change sign or vanish. In every case there is one sign change and the polynomial goes from positive to negative, so by Descartes there is exactly one positive simple y-root. Q_k(0)=4 and Q_k(1)=-40k set the crossing direction because x decreases with t. For fixed 0<epsilon<1, P_k(epsilon) goes to minus infinity; the unique root lies below epsilon for large k. Rearrangement gives 40k x_k^4(1-x_k)=4+O(x_k^2), yielding both asymptotics. Independent symbolic checks and direct matrix/atom checks at k=1,2 agreed; bisection gave t_1=0.34663861547152 and a common bound about 0.05604343479159354.

## originality

PASS

The distinct supported claim is the single isolated positive tightness time and crossing law for these irregular combinatorial-Laplacian clique joins, not the diagonal frame-operator criterion or the broad concept of uniform matrix-exponential diagonal at special parameters. The most relevant inspected earlier results treat all-time tightness within different graph classes or exponential adjacency centrality rather than this Laplacian heat law.

## value

PASS

The natural question is whether the heat-window frame can be exactly tight at an isolated positive scale even when equality at every scale is ruled out by unequal degrees. This explicit irregular family realizes that boundary case with unmodified atoms. Its exact uniqueness, direction of the exchange of the sharp bounds, and scale as the family grows specify when heat returns (and thus the frame bounds) actually coincide, going beyond an existence-by-continuity example or numerical near-tightness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
